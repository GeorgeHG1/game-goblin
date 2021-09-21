import requests
import bs4
import re
import flask

discRegex = re.compile(r'\d+%')
priceRegex = re.compile(r'(\$\d+(?:\.\d{1,2})?)')
platformRegex = re.compile(r'\[(.*?)\]')

url = 'https://old.reddit.com/r/GameDeals/hot/'

#Collects site and html data
def getSite(url):
    res = requests.get(url, headers = {'User-Agent': 'Mozilla/5.0'})
    try:
        res.raise_for_status()
    except:
        print('download error')

    html = bs4.BeautifulSoup(res.text, 'html.parser')
    return html

# Collects data from the scrape and creates an entry
def createEntry():
    html = getSite(url)
    listings = []
    for x in html.find_all('a', {'class':['title may-blank', 'title may-blank outbound']}):
        entry = {
            "Text" : x.text,
            "Discount" : discRegex.findall(x.text)[0] if discRegex.findall(x.text) else "",
            "Price" : priceRegex.findall(x.text)[0] if priceRegex.findall(x.text) else "",
            "Platform" : platformRegex.findall(x.text)[0] if platformRegex.findall(x.text) else "",
            "Link" : x['href']
                }
        if len(x['href']) <= 150:
            listings.append(entry)
    
        print(x.text)
        print(discRegex.findall(x.text)[0] if discRegex.findall(x.text) else "")
        print(priceRegex.findall(x.text)[0] if priceRegex.findall(x.text) else "")
        print(platformRegex.findall(x.text)[0] if platformRegex.findall(x.text) else "")

    return listings

createEntry()