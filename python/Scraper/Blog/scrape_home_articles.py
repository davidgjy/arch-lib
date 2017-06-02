from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.cnblogs.com/davidgu")
bsObj = BeautifulSoup(html, "html.parser")
for link in bsObj.find("div", {"id":"main_container"}).findAll("a", href=re.compile("^http://www.cnblogs.com/davidgu/p")):
    if 'href' in link.attrs and not('class' in link.attrs):
        print(link.string)
        print(link.attrs['href'])
        print("--------------------------------------------------------------")
        
