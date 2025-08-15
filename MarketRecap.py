import requests
from bs4 import BeautifulSoup

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
        self.soup = None

    def open_website(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            self.soup = BeautifulSoup(response.text, "html.parser")
            return True
        except requests.RequestException:
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

    
SiteListManager = SiteListManager()
SiteListManager.addSite("https://www.marketwatch.com/markets")

WebScraper = WebScraper(SiteListManager.getSite(1))

if WebScraper.open_website():
    print("Title:", WebScraper.get_title())
    print("Links:", WebScraper.get_all_links())
    print("Text:", WebScraper.get_text())
