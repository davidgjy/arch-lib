from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.cnblogs.com")
bsObj = BeautifulSoup(html, "html.parser")
imageLocation = bsObj.find("div", {"id": "logo"}).find("img")["src"]
urlretrieve (imageLocation, "blog_logo.jpg")