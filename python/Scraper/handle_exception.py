from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import sys


def getLogo(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print("url open exception:")
        print(e)
        return None
    
    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        logo = bsObj.body.img
    except AttributeError as e:
        print("parse logo exception:")
        print(e)
        return None
    return logo

#logo = getLogo("http://www.baidu2.com/nopage.html")
logo = getLogo("http://www.pythonscraping.com/pages/page1.html")
if logo == None:
    print("Logo could not be found")
else:
    print(logo)
    
    
