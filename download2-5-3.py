from bs4 import BeautifulSoup

html = """
<html><body>
    <ul>
        <li><a href="http://www.naver.com">naver</a></li>
        <li><a href="http://www.daum.net">daum</a></li>
        <li><a href="http://www.daum.com">daum</a></li>
        <li><a href="http://www.goolgle.com">google</a></li>
        <li><a href="http://www.tistory.com">tistory</a></li>
    </ul>
</body></html>
"""

soup = BeautifulSoup(html, 'html.parser')

links = soup.find_all("a")
#print(type(links))

a = soup.find_all("a", string="daum")
print('a', a)

#가장 상위 하나만 가져온다
#b = soup.find("a")

#상위 3개 가져온다
b = soup.find_all("a", limit=3)
print('b', b)

#정규표현식 사용해서 어떤 문자 불러올때 유용하게 사용
c = soup.find_all(string=["naver","google"])
print('c', c)

for a in links:
    #print('a', a);
    href = a.attrs['href']
    txt = a.string
    print('txt >> ', txt, 'href >> ', href)
