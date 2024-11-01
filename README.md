
# 🚀 **Selenium Web Scraping - BackRack Applications**

This Python script leverages **Selenium** to scrape detailed application data for **BackRack** products from [Summit Racing](https://www.summitracing.com/). 

---

## 🌟 **Features**

- **🔍 Comprehensive Data Extraction**: Scrapes applications for a specified list of BackRack part numbers.
- **🤖 Intelligent CAPTCHA Handling**: Implements a wait for CAPTCHA bypass; manual input might be necessary.
- **📊 Detailed Information**: Captures details such as **Make**, **Model**, and **Year** from the "Applications" section.
- **💾 Output Excellence**: Saves results in an Excel file with formatted columns for easy reading.

---

## 🛠️ **Requirements**

Ensure you have the following installed:

- **Python 3**
- **Selenium** (`pip install selenium`)
- **Pandas** (`pip install pandas`)
- **xlwings** (`pip install xlwings`)
- **ChromeDriver** ([Download here](https://developer.chrome.com/docs/chromedriver/downloads))

---

## 📋 **Setup Instructions**

### 1. **Install Required Libraries**
Run the following command in your terminal:
```bash
pip install selenium pandas xlwings
```

### 2. **Download and Set Up ChromeDriver**
- **Download**: Get the version matching your Chrome browser from [here](https://developer.chrome.com/docs/chromedriver/downloads).
- **Setup Path**: Place ChromeDriver in your preferred directory and update the path variable in the script accordingly.

### 3. **Prepare Part Numbers**
- Update the `part_numbers_to_scrape` list in the script with the BackRack part numbers you wish to scrape.

### 4. **Run the Script**
Execute the script using:
```bash
python main.py
```

---

## 📦 **Output**

The script generates an Excel file named:
```
BackRack_Applications_Scrape_<current_date>.xlsx
```
This file will be saved to your **Desktop**, containing the application data for each part number.

---

## ⚠️ **Disclaimer**

### 🚨 **Ethical Scraping Practices**
- This script is intended for **educational purposes only**.
- Always **adhere** to [Summit Racing’s terms of service](https://www.summitracing.com/help/terms) and practice responsible scraping:
  - **Avoid excessive requests** to prevent server overload.
  - CAPTCHA handling may require **manual intervention**.
  - Respect **robots.txt** protocols.

---

## 🤝 **Contributions**

Contributions, issues, and feature requests are highly welcomed! Check out the [issues page](#) to collaborate or report problems.

---

Happy coding and responsible scraping! 🎉
