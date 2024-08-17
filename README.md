Selenium Web Scraping - BackRack Applications

This Python script utilizes Selenium to scrape application data for BackRack products from Summit Racing https://www.summitracing.com/.

Features:

Scrapes applications for a defined list of BackRack part numbers.
Handles CAPTCHAs by implementing a wait time (manual intervention might be required).
Extracts various details like Make, Model, and Year from the "Applications" section.
Saves the extracted data to an Excel file with formatted column widths.
Requirements:

Python 3
Selenium library (pip install selenium)
Pandas library (pip install pandas)
xlwings library (pip install xlwings)
ChromeDriver (download from https://developer.chrome.com/docs/chromedriver/downloads)
Instructions:

Install required libraries: Use pip install <library_name> for each library mentioned above.
Download ChromeDriver: Download the appropriate ChromeDriver version for your Chrome browser from the official link and place it in the desired location. Update the path variable in the script to point to the ChromeDriver executable.
Update part_numbers_to_scrape list: Add or modify the list with the BackRack part numbers you want to scrape data for (URL links to the product pages).
Run the script: Execute the script using a Python interpreter (e.g., python main.py).
Output:

The script creates an Excel file named BackRack_Applications_Scrape_<current_date>.xlsx on your Desktop. The file contains a sheet with the extracted application data for each BackRack part number.
![Screenshot 2024-08-17 144632](https://github.com/user-attachments/assets/7156cd94-5361-4506-8b1f-cb439426d0b3)

Disclaimer:

This script is intended for educational purposes only. Adhere to Summit Racing's terms of service and avoid overwhelming their servers with excessive requests.
Captcha handling might require manual intervention depending on Summit Racing's implementation.
Consider ethical scraping practices and respect robot exclusion protocols (robots.txt).
