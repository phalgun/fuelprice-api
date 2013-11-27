import requests
import lxml.html
import re
import urls

def scrape_latest_petrol_price(url):
    r = requests.get(url)
    data = r.text
    
    tree = lxml.html.fromstring(data)
    complete_string = tree.xpath('//table[contains(@class, "DDGridView")]/tr[1]/td/span/text()')
    stripped_string = str(list(complete_string)[0].strip())
    
    matchObj = re.search(r'Price = (.*)', stripped_string, re.M | re.I)
    
    return matchObj.group(1)
 

def scrape_all_petrol_prices():
    url_dict = urls.petrol_urls()
    petrol_prices = {}
    
    for city in url_dict:
        petrol_prices[(city).title()] = scrape_latest_petrol_price(url_dict[city])
    
    return petrol_prices

def scrape_all_city_and_urls():
    r = requests.get('http://www.mypetrolprice.com/petrol-price-in-india.aspx')
    data = r.text
    
    tree = lxml.html.fromstring(data)
    urls = tree.xpath('//td/ul[contains(@id, "BC_blPerolPrices")]/li/a/@href')

    return urls
    
