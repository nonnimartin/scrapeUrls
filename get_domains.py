from bs4 import BeautifulSoup as soupy
import requests

def remove_prefix(text, prefix):

    prefixes = ["/search?ie=UTF-8&q=related:", "/url?q="]

    #if text.startswith(prefixes):
    for prefix in prefixes:
        if text.startswith(prefix):
            split_text = text.split(prefix)
            return split_text[1]
    else:
        return text

def getLinks(url):

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

                   "https://www.google.com/search?hl=en&tbm=isch&source=og&tab=wi",
                   "https://maps.google.com/maps?hl=en&tab=wl",
                   "https://play.google.com/?hl=en&tab=w8",
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

    for link in rawLinks:
        for marker in markers:
            if marker in link and not any(substring in link for substring in defaultGoogle):
                no_pref_link = remove_prefix(link, "/url?q=")
                links.append(no_pref_link)

    return links

allLinks = getLinks("https://www.google.com/search?q=test&oq=test&aqs=chrome..69i57j0l5.445j0j8&sourceid=chrome&ie=UTF-8")

for i in allLinks:
    print i