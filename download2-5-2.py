from bs4 import BeautifulSoup

html = """
<html>
<body>
<h1>파이썬 BeautifulSoup 공부</h1>
<p>태그 선택자</p>
<p>css 선택자</p>
</body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')
#print('soup', type(soup));
#print('prettify', soup.prettify())

h1 = soup.html.body.h1
print('h1', type(h1))
print(h1.string)


#next_sibling, previous_sibling 형제들 접근하는건데 코드 수정되면 바꿔줘야되므로 자주 사용하지 않는다.
p1 = soup.html.body.p
print('p1', p1)
p2 = p1.next_sibling.next_sibling #위에서 문자열끝에 \n 있어서
print('p2', p2)
p3 = p1.previous_sibling.previous_sibling
print('p3', p3)

print("h1 >> ", h1.string)
print("p >> ", p1.string)
print("p >> ", p2.string)
