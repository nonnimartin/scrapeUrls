from bs4 import BeautifulSoup as soupy
import requests
import get_random_query

class getDomains(object):

    def __init__(self):

        self.domains  = []

    def queryAsk(self):

        askPrefix    = "http://www.ask.com/web?q="
        askPostfix   = "&o=0&qo=homepageSearchBox"

        randQueryObj = get_random_query.getRandomQuery()
        randQuery    = randQueryObj.randomQueryTerms()

        queryUrl     = askPrefix + randQuery + askPostfix
        return self.getLinks(queryUrl)

    def remove_prefix(self, text):

        prefixes = ["//"]

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

        for link in soupObj.find_all('a'):
            rawLinks.append(link.get('href'))

        #list features of interest
        markers = ["http", "https", "www"]

        for link in rawLinks:
            if link.startswith(("https", "http", "www", "//www")):
              no_pref_link = self.remove_prefix(link)
              self.domains.append(no_pref_link)

        return self.domains
