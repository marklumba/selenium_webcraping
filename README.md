# Selenium Web Scraping - BackRack Applications

This Python script utilizes Selenium to scrape application data for BackRack products from [Summit Racing](https://www.summitracing.com/).

## 🌟 Features

- 🔍 Scrapes applications for a defined list of BackRack part numbers
- 🤖 Handles CAPTCHAs by implementing a wait time (manual intervention might be required)
- 📊 Extracts various details like Make, Model, and Year from the "Applications" section
- 💾 Saves the extracted data to an Excel file with formatted column widths

## 🛠️ Requirements

- Python 3
- Selenium library (`pip install selenium`)
- Pandas library (`pip install pandas`)
- xlwings library (`pip install xlwings`)
- ChromeDriver ([download from official site](https://developer.chrome.com/docs/chromedriver/downloads))

## 📋 Instructions

1. **Install Required Libraries**
   ```bash
   pip install selenium pandas xlwing
2. Download ChromeDriver

  -Download the appropriate ChromeDriver version for your Chrome browser
  -Place it in your desired location
  -Update the path variable in the script to point to the ChromeDriver executable


3. Prepare Part Numbers

  -Update part_numbers_to_scrape list with BackRack part numbers you want to scrape

4. Run the script

   ```bash
   python main.py

📦 Output
The script generates an Excel file named BackRack_Applications_Scrape_<current_date>.xlsx on your Desktop, containing application data for each BackRack part number.



⚠️ Disclaimer
🚨 Ethical Scraping Practices

Intended for educational purposes only
Adhere to Summit Racing's terms of service
Avoid overwhelming their servers with excessive requests
Captcha handling may require manual intervention
Respect robot exclusion protocols (robots.txt)

🤝 Contributions
Contributions, issues, and feature requests are welcome! Feel free to check issues page.
   



