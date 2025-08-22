from polygon import RESTClient
from selenium import webdriver
from bs4 import BeautifulSoup
from io import BytesIO

import requests

import pycurl
import json

import time

class SiteListManager:
    def __init__(self, filename="SiteLists.txt"):
        self.filename = filename

    def addSite(self, site_url):
        with open(self.filename, "a") as f:
            f.write(site_url + "\n")

    def getAllSites(self):
        with open(self.filename, "r") as f:
            sites = [line.strip() for line in f if line.strip()]
        return sites
    
    def getSite(self, index):
        with open(self.filename, "r") as f:
            sites = [line.strip() for line in f if line.strip()]
        return sites[index-1] if 0 <= (index-1) < len(sites) else None
    
    def removeSite(self, site_url):
        sites = self.getAllSites()
        if site_url in sites:
            sites.remove(site_url)
            with open(self.filename, "w") as f:
                for site in sites:
                    f.write(site + "\n")

    def clearAllSites(self):
        with open(self.filename, "w") as f:
            f.write("")
