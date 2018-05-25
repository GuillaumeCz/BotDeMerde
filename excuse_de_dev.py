import requests
from bs4 import BeautifulSoup

url = "http://www.excusesdedev.com"

def getExcuse():
    resp = requests.get(url)
    html = resp.text
    soup = BeautifulSoup(html, 'html.parser')
    quote_ = soup.find("div", { "class": "quote" }).string.encode('latin1')
    return quote_
