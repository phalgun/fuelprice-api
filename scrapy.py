import requests
import lxml.html
import re

def get_latest_petrol_price(url):
    r = requests.get(url)
    data = r.text
    
    tree = lxml.html.fromstring(data)
    complete_string = tree.xpath('//table[contains(@class, "DDGridView")]/tr[1]/td/span/text()')
    stripped_string = str(list(complete_string)[0].strip())
#     print stripped_string
    
    matchObj = re.search(r'Price = (.*)', stripped_string, re.M | re.I)
    return matchObj.group(1)
 
# url = "http://www.mypetrolprice.com/2/Petrol-price-in-Delhi"
# print get_latest_petrol_price(url)

def pretty(d, indent=0):
    for key, value in d.iteritems():
        print '\t' * indent + '\'' + str(key) + '\':'
        if isinstance(value, dict):
            pretty(value, indent + 1)
        else:
            print '\t' * (indent + 1) + '\'' + str(value) + '\','


def construct_map(urls):
    domain = 'http://www.mypetrolprice.com/'
    url_dict = {}
    for url in urls:
        url_dict[(url.split('-')[-1]).lower()] = domain + url
        
    pretty(url_dict)
    return url_dict

def get_all_city_and_urls():
    r = requests.get('http://www.mypetrolprice.com/petrol-price-in-india.aspx')
    data = r.text
    
    tree = lxml.html.fromstring(data)
    urls = tree.xpath('//td/ul[contains(@id, "BC_blPerolPrices")]/li/a/@href')
#     for url in urls:
#         print url
#     
    construct_map(urls)

get_all_city_and_urls() 
