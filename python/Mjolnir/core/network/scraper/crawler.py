from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

# class linker
class Linker:
        def __init__(self):
                self.links = set()

        # get links
        def getLinks(self, url, parent_tag, parent_id, reg):
                self.links = set()
                html = urlopen(url)
                bsObj = BeautifulSoup(html, "html.parser")
                for link in bsObj.find(parent_tag, {"id": parent_id}).findAll("a", href=re.compile(reg)):
                        if 'href' in link.attrs:
                                self.links.add(link)
                return self.links
        
        # get links without attr
        def getLinksNegAttr(self, url, parent_tag, parent_id, reg, attr):
                self.links = set()
                html = urlopen(url)
                bsObj = BeautifulSoup(html, "html.parser")
                for link in bsObj.find(parent_tag, {"id": parent_id}).findAll("a", href=re.compile(reg)):
                        if 'href' in link.attrs and not(attr in link.attrs):
                                self.links.add(link)
                return self.links

        # get links with attr(exclude class)
        def getLinksWithAttr(self, url, parent_tag, parent_id, reg, attr, attr_value):
                self.links = set()
                html = urlopen(url)
                bsObj = BeautifulSoup(html, "html.parser")
                for link in bsObj.find(parent_tag, {"id": parent_id}).findAll("a", href=re.compile(reg)):
                        if 'href' in link.attrs and attr in link.attrs:
                                if link.attrs[attr] == attr_value:
                                        self.links.add(link)
                return self.links

	# get links has class
        def getLinksHasClass(self, url, parent_tag, parent_id, reg, class_name):
                self.links = set()
                html = urlopen(url)
                bsObj = BeautifulSoup(html, "html.parser")
                for link in bsObj.find(parent_tag, {"id": parent_id}).findAll("a", href=re.compile(reg)):
                        if 'href' in link.attrs and 'class' in link.attrs:
                                if class_name in link.attrs['class']:
                                        self.links.add(link)
                return self.links			
