import requests
from bs4 import BeautifulSoup

def get_html(url):
    response = requests.get(url)
    if response.ok:
        return BeautifulSoup(response.content, features="lxml")
    return None