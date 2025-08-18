from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
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

class WebScraper:
    def __init__(self, url):
        self.url = url
        self.driver = None
        self.soup = None

    def open_website(self):
        try:
            self.driver = webdriver.Firefox()
            self.driver.get(self.url)
            html = self.driver.page_source
            self.soup = BeautifulSoup(html, "html.parser")
            return True
        except Exception:
            self.soup = None
            return False

    def get_title(self):
        if self.soup:
            return self.soup.title.string if self.soup.title else None
        return None

    def get_all_links(self):
        if self.soup:
            return [a.get('href') for a in self.soup.find_all('a', href=True)]
        return []

    def get_text(self):
        if self.soup:
            return self.soup.get_text()
        return ""

    def close(self):
        if self.driver:
            self.driver.quit()

SiteListManager = SiteListManager()
SiteListManager.clearAllSites()
SiteListManager.addSite("https://www.marketwatch.com/markets")
SiteListManager.addSite("https://google.com")

WebScraper = WebScraper(SiteListManager.getSite(2))
if WebScraper.open_website():
    print("Title:", WebScraper.get_title())
    #print("Links:", WebScraper.get_all_links())
    print("Text Content:", WebScraper.get_text()[:200])