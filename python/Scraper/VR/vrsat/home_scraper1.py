from urllib.request import urlopen
from bs4 import BeautifulSoup

# scraper
def scraper(url, pageNo):
	scrapeUrl = url
	if pageNo > 1:
		scrapeUrl = url + "page/" + str(pageNo)
	html = urlopen(scrapeUrl)
	bsObj = BeautifulSoup(html.read(), "html.parser")
	newsList = bsObj.findAll("div", {"class":"focus"})
	print("#####################################################################################")
	print("Found Result: %s" % len(newsList))
	print("------------------------------ detail ------------------------------")
	for news in newsList:
		imgList = news.findAll("img")
		for img in imgList:
			print("Title: %s" % img["alt"])
			print("Image: %s" % img["src"])
			print("************************************")

url = "http://www.vrsat.com/"
scraper(url, 1)
scraper(url, 2)
