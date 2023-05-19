from selenium import webdriver
from datetime import datetime
from selenium.webdriver.common.by import By
import time
import pandas as pd
browser = webdriver.Firefox()
def scrape_surebets():
    browser = webdriver.Firefox()
    browser.get('https://en.surebet.com/surebets')
    html=browser.page_source
    time.sleep(10)
    table = browser.find_element(By.CSS_SELECTOR, "#surebets-table")
    table_html = table.get_attribute('outerHTML')
    df = pd.read_html(table_html)[0]
    df.drop(columns=["▼Profit","Unnamed: 7","Unnamed: 8"])
    browser.close()
    return df
def scrape_surebets():
    browser = webdriver.Firefox()
    browser.get('https://en.surebet.com/surebets')
    html=browser.page_source
    time.sleep(10)
    table = browser.find_element(By.CSS_SELECTOR, "#.content-inner")
    table_html = table.get_attribute('outerHTML')
    df = pd.read_html(table_html)[0]
    browser.close()
    return df
scrape_surebets()


