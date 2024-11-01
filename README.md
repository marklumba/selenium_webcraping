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
   pip install selenium pandas xlwings
