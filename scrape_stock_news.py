from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

# Set up Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run Chrome in headless mode
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Define the Yahoo Finance Stock Market News URL
NEWS_URL = "https://finance.yahoo.com/topic/stock-market-news/"

driver.get(NEWS_URL)
time.sleep(5)  # Wait for page to load completely

# Extract multiple headlines using XPath
headline_elements = driver.find_elements(By.XPATH, "//h3")  # Adjusted to capture all headlines

# Store extracted headlines in a list
headlines = [headline.text for headline in headline_elements if headline.text.strip()]

driver.quit()  # Close the browser

# Save headlines to a CSV file
if headlines:
    df = pd.DataFrame({"Headline": headlines})
    df.to_csv("stock_news.csv", index=False, encoding='utf-8')
    print("✅ Data saved successfully in stock_news.csv")
else:
    print("❌ No headlines found. Please check the XPath or website structure.")
