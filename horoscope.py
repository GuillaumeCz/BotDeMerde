import requests
import json

url = "https://horoscope-api.herokuapp.com/horoscope/today/"

def getHoroscope(_sign):
    final_url = url + _sign
    resp = requests.get(final_url)
    horoscope = resp.json()
    value_ = horoscope["horoscope"]
    return value_[2:len(value_)-2]


