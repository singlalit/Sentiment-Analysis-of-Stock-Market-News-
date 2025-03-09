# Sentiment-Analysis-of-Stock-Market-News-

# Stock Market News Scraper

## 📌 Project Overview
This project is a **Python-based web scraper** that automatically fetches the latest **stock market news headlines** and saves them into a CSV file. It uses **Selenium** with a headless Chrome browser to scrape data from a financial news website.

## ⚡ Features
- Scrapes multiple **stock market news headlines**
- Saves data to a structured **CSV file**
- **Automated execution** using Windows Task Scheduler
- **Error handling & retries** for better reliability

## 🛠️ Tech Stack
- **Python** (Selenium, Pandas)
- **Selenium WebDriver** for web scraping
- **CSV File Handling** for data storage
- **Windows Task Scheduler** for automation

## 🚀 How to Run the Project
### 1️⃣ Install Dependencies
Make sure you have Python installed, then run:
```bash
pip install selenium pandas
```

### 2️⃣ Download ChromeDriver
Ensure **ChromeDriver** is installed and matches your **Google Chrome version**.
- Download from: [ChromeDriver](https://sites.google.com/chromium.org/driver/)
- Place it in the project directory or set it in the system PATH.

### 3️⃣ Run the Script Manually
```bash
python stock_news_scraper.py
```

### 4️⃣ Automate Execution (Windows Task Scheduler)
1. Open **Task Scheduler** → "Create Basic Task"
2. Set a name (e.g., `Stock News Scraper`)
3. Select "Daily" or "Every X Hours" as per requirement
4. Choose "Start a Program" → Browse `python.exe`
5. In the "Arguments" field, add the script path:
   ```bash
   "C:\path\to\stock_news_scraper.py"
   ```
6. Click "Finish" and enable the task.

## 📂 Output File
All scraped headlines are saved in `stock_news.csv`:
```
Headline
"Stock market surges as AI stocks boom"
"Federal Reserve announces new policy measures"
"Tesla stock drops amid supply chain concerns"
```

## 📌 Future Enhancements
- Store data in **PostgreSQL/MySQL**
- Perform **Sentiment Analysis** on headlines
- Create a **Power BI / Tableau Dashboard**
- Deploy a **Flask or FastAPI Web App**

## 🤝 Contributing
Feel free to fork this repository and improve the script! Pull requests are welcome. 🚀



---

