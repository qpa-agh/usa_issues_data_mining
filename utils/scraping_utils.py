import requests
from bs4 import BeautifulSoup


session = requests.Session()
def get_html(url):
    response = session.get(url)
    if response.ok:
        return BeautifulSoup(response.content, features="lxml")
    return None