from bs4 import BeautifulSoup as soupy
import requests

class getDomains(object):

    def __init__(self, query):

        self.domains  = []
        self.query    = query

    def queryGoogle(self):
        googlePrefix = "https://www.google.com/#q="
        queryUrl     = googlePrefix + self.query
        return self.getLinks(queryUrl)

    def remove_prefix(self, text):

        prefixes = ["/search?ie=UTF-8&q=related:", "/url?q="]

        #if text.startswith(prefixes):
        for prefix in prefixes:
            if text.startswith(prefix):
                split_text = text.split(prefix)
                return split_text[1]
        else:
            return text

    def getLinks(self, url):

        #Get http request for URL
        req = requests.get(url)
        #Get text returned from request object
        data = req.text
        #Make BeautifulSoup HTML object
        soupObj = soupy(data, "html.parser")

        #raw image links from bs4
        rawLinks=[]

        #Links with markers of interest
        links = []
        
        #list of normal default Google links that will occur in any basic Google search
        defaultGoogle = [
                       "https://maps.google.com/maps?hl=en&tab=wl",
                       "https://play.google.com/?hl=en&tab=w8",
                       "https://www.youtube.com/results?tab=w1",
                       "https://news.google.com/nwshp?hl=en&tab=wn",
                       "https://mail.google.com/mail/?tab=wm",
                       "https://drive.google.com/?tab=wo",
                       "https://www.google.com/intl/en/options/",
                       "http://www.google.com/history/optout?hl=en"
        ]

        for link in soupObj.find_all('a'):
            rawLinks.append(link.get('href'))
        
        #list features of interest
        markers = ["http", "https", "www"]

        print rawLinks

        for link in rawLinks:
            for marker in markers:
                if marker in link and not any(substring in link for substring in defaultGoogle):
                    no_pref_link = self.remove_prefix(link)
                    self.domains.append(no_pref_link)

        return self.domains

test = getDomains("hey")
print test.queryGoogle()
