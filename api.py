import flask
import flask_cors
import pandas as pd
import requests
import time
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
def to_json(data):
    json_data = {}
    first = True
    for row in data:
        if first: 
            first = not first
            continue
        if "+" in row[2]:continue
        json_data[row[2].replace("\u200b","")] = {
            "profit":{
                "percent":row[1].split("  ")[0],
                "interval":row[1].split("  ")[1]},
            "datetime":row[3],
            "event":row[4],
            "market":row[5],
            "odds":row[6],
        }
    return json_data
def scrape1xbet():
    df=pd.DataFrame(columns=["teams","team 1 odds","team 2 odds","website"])
    browser = webdriver.Edge()
    browser.get('https://1x-bet.in/en/live/cricket')
    time.sleep(5)
    data=browser.find_element(By.CSS_SELECTOR, '.ui-dashboard')
    soup = BeautifulSoup(data.get_attribute('innerHTML'), 'html.parser')
    matches = soup.findAll(class_='ui-dashboard-champ dashboard-champ dashboard__champ ui-dashboard-champ--theme-gray')
    for match in matches:
        a=match.findAll(class_="market__value")
        name=match.findAll(class_="dashboard-game-team-info dashboard-game-block__team")
        df=df.append({"teams":name[0].text+" vs "+name[1].text,"team 1 odds":a[0].text,"team 2 odds":a[1].text,"website":"1xbet"},ignore_index=True)
    browser.quit()
    return df
def scrapeparimatch():
    df=pd.DataFrame(columns=["teams","team 1 odds","team 2 odds","website"])
    browser = webdriver.Edge()
    browser.get('https://parimatch-in.com/en/cricket/live')
    time.sleep(10)
    data=browser.find_element(By.CSS_SELECTOR, '#line-holder > div.EC_AI')
    soup = BeautifulSoup(data.get_attribute('innerHTML'), 'html.parser')
    matches = soup.findAll("div",class_='EC_BP')
    for match in matches:
        a=match.findAll(class_="styles_odd__1vusX")
        name=match.findAll("styles_name__2QIKf styles_name-horizontal__217P1")
        df=df.append({"teams":name[0],"team 1 odds":a[0].text,"team 2 odds":a[1].text,"website":"parimatch"},ignore_index=True)
    browser.quit()
    return df

def scrapemagapari():
    df=pd.DataFrame(columns=["teams","team 1 odds","team 2 odds","website"])
    browser = webdriver.Edge()
    browser.get('https://megapari.com/live/cricket')
    time.sleep(10)
    data=browser.find_element(By.CSS_SELECTOR, '#games_content')
    soup = BeautifulSoup(data.get_attribute('innerHTML'), 'html.parser')
    matches = soup.findAll("div",class_='dashboard-champ-content')
    for match in matches:
        a=match.findAll("span",class_="c-bets__inner")
        name=match.findAll("div",class_="c-events__team")
        df=df.append({"teams":name[0].text,"team 1 odds":a[0].text,"team 2 odds":a[1].text,"website":"megapari"},ignore_index=True)
    browser.quit()
    return df

def scrapebetway():
    df=pd.DataFrame(columns=["teams","team 1 odds","team 2 odds","website"])
    browser = webdriver.Edge()
    browser.get('https://1x-bet.in/en/live/cricket')
    time.sleep(5)
    data=browser.find_element(By.CSS_SELECTOR, '.ui-dashboard')
    soup = BeautifulSoup(data.get_attribute('innerHTML'), 'html.parser')
    matches = soup.findAll(class_='ui-dashboard-champ dashboard-champ dashboard__champ ui-dashboard-champ--theme-gray')
    for match in matches:
        a=match.findAll(class_="market__value")
        name=match.findAll(class_="dashboard-game-team-info dashboard-game-block__team")
        df=df.append({"teams":name[0].text+" vs "+name[1].text,"team 1 odds":a[0].text,"team 2 odds":a[1].text,"website":"1xbet"},ignore_index=True)
    browser.quit()
    return df
def scrapebet365():
    df=pd.DataFrame(columns=["teams","team 1 odds","team 2 odds","website"])
    browser = webdriver.Edge()
    browser.get('https://1x-bet.in/en/live/cricket')
    time.sleep(5)
    data=browser.find_element(By.CSS_SELECTOR, '.ui-dashboard')
    soup = BeautifulSoup(data.get_attribute('innerHTML'), 'html.parser')
    matches = soup.findAll(class_='ui-dashboard-champ dashboard-champ dashboard__champ ui-dashboard-champ--theme-gray')
    for match in matches:
        a=match.findAll(class_="market__value")
        name=match.findAll(class_="dashboard-game-team-info dashboard-game-block__team")
        df=df.append({"teams":name[0].text+" vs "+name[1].text,"team 1 odds":a[0].text,"team 2 odds":a[1].text,"website":"1xbet"},ignore_index=True)
    browser.quit()
    return df
def scrapebetfair():
    df=pd.DataFrame(columns=["teams","team 1 odds","team 2 odds","website"])
    browser = webdriver.Edge()
    browser.get('https://1x-bet.in/en/live/cricket')
    time.sleep(5)
    data=browser.find_element(By.CSS_SELECTOR, '.ui-dashboard')
    soup = BeautifulSoup(data.get_attribute('innerHTML'), 'html.parser')
    matches = soup.findAll(class_='ui-dashboard-champ dashboard-champ dashboard__champ ui-dashboard-champ--theme-gray')
    for match in matches:
        a=match.findAll(class_="market__value")
        name=match.findAll(class_="dashboard-game-team-info dashboard-game-block__team")
        df=df.append({"teams":name[0].text+" vs "+name[1].text,"team 1 odds":a[0].text,"team 2 odds":a[1].text,"website":"1xbet"},ignore_index=True)
    browser.quit()
    return df
app = flask.Flask(__name__)
flask_cors.CORS(app)

@app.route('/api/v1/surebets', methods=['post'])
def scrapeall():
    df=scrape1xbet()
    df=df.append(scrapeparimatch(),ignore_index=True)
    df=df.append(scrapemagapari(),ignore_index=True)
    df=df.append(scrapebetway(),ignore_index=True)
    df=df.append(scrapebet365(),ignore_index=True)
    df=df.append(scrapebetfair(),ignore_index=True)
    return df.to_json(orient='records')
if __name__ == '__main__':
    app.run(debug=True)

