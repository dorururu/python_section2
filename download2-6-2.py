from bs4 import BeautifulSoup

fp = open("food-list.html",encoding="utf-8")
soup = BeautifulSoup(fp, 'html.parser')

print(soup)

print("1", soup.select("li:nth-of-type(4)")[1].string) #각 li태그 그룹의 4번째 요소
print("2", soup.select_one("#ac-list > li:nth-of-type(4)").string)
print("3", soup.select("#ac-list > li[data-lo='cn']")[0].string)
print("4", soup.select("#ac-list > li.alcohol.high")[0].string)

param = {"data-lo": "cn", "class": "alcohol"}
print("5", soup.find("li", param).string)
print("6", soup.find(id="ac-list").find("li",param).string)
#6이 더 정확하지만 5번이 더 가독성 좋다(위에 param에 정보가 많으므로)

for ac in soup.find_all("li"):
    if ac['data-lo'] == 'us':
        print('data-lo == us', ac.string)
