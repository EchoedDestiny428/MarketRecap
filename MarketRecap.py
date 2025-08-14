import requests
from bs5 import BeautifulSoup

def addurl(url):
    with open('SiteLists.txt', 'a') as file:
        file.write(url + '\n')

def getSiteNumber(siteNumber):
    with open('siteList.txt', 'r') as file:
        return file.readline(siteNumber).strip('\n')
    

print(getSiteNumber(0))
