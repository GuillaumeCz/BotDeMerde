import requests
from bs4 import BeautifulSoup

url = "http://enneagon.org/phrases"

def getSentence(_nb):
    data = {'nb': _nb, 'sok': 'Lancer+!'}

    response = requests.post(url, data) 
    html = response.text
    soup = BeautifulSoup(html, "html.parser")

    sentence_ = soup.find("div", {"class": "main"}).find("p").string.encode('UTF-8', 'ignore')
    return sentence_
