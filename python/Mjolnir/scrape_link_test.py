from core.scraper.crawler import Linker

def display(links):
    for link in links:
        print(link.string)
        print(link.attrs['href'])
        print("--------------------------------------------------------------")

def displayTags(links, tag):
    for link in links:
        print(link.attrs[tag])
        
spr = Linker()

# get links
print("******************************************  1. Get Links ******************************************");
links = spr.getLinks("http://www.cnblogs.com/davidgu", "div", "main_container", "^http://www.cnblogs.com/davidgu/p")
display(links)
print("***************************************************************************************************")
print()

# get links without class attr
print("********************************* 2. Get Links Without Class Attr *********************************");
links = spr.getLinksNegAttr("http://www.cnblogs.com/davidgu", "div", "main_container", "^http://www.cnblogs.com/davidgu/p", "class")
display(links)
print("***************************************************************************************************")
print()

# get links has class
print("********************************* 3. Get Links Has Class Attr *********************************");
links = spr.getLinksHasClass("http://www.cnblogs.com/davidgu", "div", "main_container", "^http://www.cnblogs.com/davidgu/p", "c_b_p_desc_readmore")
display(links)
print("***************************************************************************************************")

