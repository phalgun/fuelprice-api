import requests
import lxml.html
import re
from urls import get_petrol_urls

def get_latest_petrol_price(url):
    r = requests.get(url)
    data = r.text
    
    tree = lxml.html.fromstring(data)
    complete_string = tree.xpath('//table[contains(@class, "DDGridView")]/tr[1]/td/span/text()')
    stripped_string = str(list(complete_string)[0].strip())
    
    matchObj = re.search(r'Price = (.*)', stripped_string, re.M | re.I)
    return matchObj.group(1)
 

def get_all_petrol_prices():
    url_dict = get_petrol_urls()
    petrol_prices = {}
    
