import urllib.request
from bs4 import BeautifulSoup
import time
from selenium import webdriver
import json


def get_html(url):
    headers = {'User-Agent': 'User-Agent:Mozilla/5.0'}
    data1 = urllib.request.Request(url, headers=headers)
    page = urllib.request.urlopen(data1).read()
    return BeautifulSoup(page, features="html.parser")


def get_js(url):
    browser = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
    browser.get(url)
    data = browser.page_source
    browser.close()
    return BeautifulSoup(data, features="html.parser")


def get_subway_url():
    url = {}
    soup = get_js('http://www.szmc.net/ver2/operating/search?scode=0101&xl=1')
    ch = soup.find('ul',attrs={'class':'xianlu'})
    lines = ch.find_all('li')
    for item in lines:
        url[item.span.string] = "http://www.szmc.net/ver2/" + item.a['href']
    return url


def get_subway_station(url):
    stations = []
    soup = get_js(url)
    ch = soup.find('ul', attrs={'class': 'zhan'})
    sta = ch.find_all('li')
    for item in sta:
        stations.append(item.string)
    return stations


def save_as_json(str):
    f = open('subway.txt', 'w')
    f.write(json.dumps(str))
    f.close()


if __name__ == '__main__':
    subway_url = get_subway_url()
    for line, url in subway_url.items():
        subway_url[line] = get_subway_station(url)
    save_as_json(subway_url)




