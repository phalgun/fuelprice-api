import urllib2
import scrapy

def pretty(d, indent=0):
    for key, value in d.iteritems():
        print '\t' * indent + '\'' + str(key) + '\':'
        if isinstance(value, dict):
            pretty(value, indent + 1)
        else:
            print '\t' * (indent + 1) + '\'' + str(value) + '\','


'''
    Method to remove URL characters like %20 (space) in the city name 
'''
def cleanse(city_name):
    return urllib2.unquote(city_name)


def construct_map(urls):
    domain = 'http://www.mypetrolprice.com/'
    url_dict = {}
    for url in urls:
        city_name = (url.split('-')[-1]).lower()
        city_name = cleanse(city_name) 
        url_dict[city_name] = domain + url
        
    pretty(url_dict)
    return url_dict

construct_map(scrapy.scrape_all_city_and_urls_diesel())