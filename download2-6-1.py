from bs4 import BeautifulSoup
import re #regex 잘 사용하지는 않는다

html = """
<html><body>
    <ul>
        <li><a id="naver" href="http://www.naver.com">naver</a></li>
        <li><a href="http://www.daum.net">daum</a></li>
        <li><a href="http://www.daum.com">daum</a></li>
        <li><a href="https://www.goolgle.com">google</a></li>
        <li><a href="https://www.tistory.com">tistory</a></li>
    </ul>
</body></html>
"""

soup = BeautifulSoup(html, 'html.parser')
print(soup.find(id="naver").string)
#li = soup.find_all(href=re.compile(r"da"))
li = soup.find_all(href=re.compile(r"^https://"))

for e in li:
    print(e.attrs['href'])
