from bs4 import BeautifulSoup
import urllib.request as req


url = ""
res = req.urlopen(url).read()
soup = BeautifulSoup(res, "html.parser")

top10 = soup.select("#siselist_tab_0 > tr")

i = 1
for e in top10:
    if e.find("a") is not None:
        print(i,e.select_one(".tltle").string)
        i += 1
        
