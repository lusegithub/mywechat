import requests
from bs4 import BeautifulSoup


def getjoke():
    url = "http://www.qiushibaike.com/hot/"
    html = requests.get(url).text
    soup = BeautifulSoup(html, "lxml")
    joke = []
    for i in soup.findAll('div', class_='content'):
        joke.append(i.span.text)
    return joke