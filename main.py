from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import pandas as pd
import xlwings as xw
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import datetime


# Define the website to scrape and path where the chromedriver is located
website = 'https://www.summitracing.com/search/brand/backrack?GroupBy=ProductName' # starting url point
path = r'C:\Users\Mark Lumba\Documents\Selenium_Webscraping\chromedriver.exe'  # webdriver path


# Create Chrome options and add the argument to ignore certificate errors
chrome_options = Options()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--ignore-ssl-errors")
chrome_options.add_experimental_option("detach", True)

# Assuming 'path' is the path to your chromedriver executable
service = Service(executable_path=path)

# Create a new instance of the Chrome driver with options and service
driver = webdriver.Chrome(service=service, options=chrome_options)


# Navigate to the website
driver.get(website)

# Wait for the "Individual Parts" link to be clickable
individual_parts_locator = (By.CSS_SELECTOR, '#sResultsComp > div.row > div.columns.medium-15.large-16.xlarge-18 > div.results-view-tabs.custom-tabs.row.columns > div:nth-child(1) > a')
individual_parts = WebDriverWait(driver, 200).until(EC.element_to_be_clickable(individual_parts_locator))

time.sleep(2)  # Add a 2-second sleep
# Click the "Individual Parts" link
individual_parts.click()

# Constants
CAPTCHA_WAIT_TIME = 500
ELEMENT_WAIT_TIME = 500
PAGE_LOAD_WAIT_TIME = 500
BUTTON_WAIT_TIME = 500

# Wait for 300 seconds to manually solve the CAPTCHA
time.sleep(CAPTCHA_WAIT_TIME)



# Define a list of part number href values to scrape
part_numbers_to_scrape = [


    "https://www.summitracing.com/parts/bkr-10200",
    "https://www.summitracing.com/parts/bkr-10700",





    # Add more part number href values as needed
]

# Create an empty list to store the extracted information
part_data = []

# Iterate through each part link
for part_link in part_numbers_to_scrape:
    # Navigate to the part details page
    driver.get(part_link)

    # Extract the part number from the URL and convert it to all caps
    part_number = part_link.split('/')[-1].upper()

    # Scroll down to the bottom of the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait for the "Applications" button to appear and click it
    WebDriverWait(driver, BUTTON_WAIT_TIME).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-anchor="applications"]'))
    ).click()

    try:
        check_fit_button = WebDriverWait(driver, BUTTON_WAIT_TIME).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#btnApplicationTab'))
        )
        check_fit_button.click()
    except TimeoutException:
        print("Timed out waiting for the 'Check the Fit' button to appear.")
        continue

    while True:
        try:
            # Wait for the details page to load
            WebDriverWait(driver, PAGE_LOAD_WAIT_TIME).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.attribute-container.application-item.flex-container.flex-wrap'))
            )

            # Extract data from the details page    
            detail_containers = driver.find_elements(By.CSS_SELECTOR, '.attribute-container.application-item.flex-container.flex-wrap')
        
            for container in detail_containers:
                part_detail = {}
                # Add the part number to the part detail at the start
                part_detail['Part Number'] = part_number
                key_value_pairs = container.find_elements(By.TAG_NAME, 'div')
                for i in range(0, len(key_value_pairs), 2):
                    key = key_value_pairs[i].text.strip(':')
                    value = key_value_pairs[i + 1].text.strip() if i + 1 < len(key_value_pairs) else ""
                    part_detail[key] = value
                part_data.append(part_detail)

            # Check if the "Next" page element is present
            next_page_elements = driver.find_elements(By.CSS_SELECTOR, 'li.next-page > a')
            if not next_page_elements:
                # If "Next" page element is not found, break out of the loop
                print("No more pages left to scrape for this part.")
                break

            # Click the "Next" page element
            next_page_elements[0].click()

            # Wait for the new page to load (you might need to adjust the wait time)
            WebDriverWait(driver, ELEMENT_WAIT_TIME).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.attribute-container.application-item.flex-container.flex-wrap'))
            )

        except Exception as e:
            print(f"Error processing part: {e}")
            break

# Print the extracted information
for part in part_data:
    print('Details:')
    for key, value in part.items():
        print(f' {key}: {value}')

# Create a DataFrame from the dictionary of key-value pairs
df_parts = pd.DataFrame(part_data)

# Generate the current date and time as a string
current_datetime = datetime.datetime.now().strftime("%Y-%m-%d")

# Define the output file name with the date and time
output_file_name = f"BackRack_Applications_Scrape_{current_datetime}.xlsx"

# Save the DataFrame to an Excel file
file_path = os.path.join(os.path.expanduser("~"), "Desktop", output_file_name)
df_parts.to_excel(file_path, index=False, freeze_panes=(1, 0))

# Open the Excel file and set all columns width to 15
with xw.App(visible=False) as app:
    wb = xw.Book(file_path)

    # Loop through all worksheets in the workbook
    for ws in wb.sheets:
        # Loop through all columns in the worksheet
        for column in ws.api.UsedRange.Columns:
            column.ColumnWidth = 15

        # Save the workbook if needed
        wb.save()

        # Close the workbook
        wb.close()

# Print a message indicating the successful save
print(f'Data saved to: {file_path}')

# Quit the Chrome browser
driver.quit()

