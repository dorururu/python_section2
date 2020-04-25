import urllib.request as req
from urllib.parse import urlparse

url = "https://e.kakao.com/"


mem = req.urlopen(url)

#print(type(mem))

#print("geturl", mem.geturl())
#print("status", mem.status) #200 : 정상, 404 : 없음, 403 : 거절, 500 : 서버에러
#print("headers", mem.getheaders())
#print("info", mem.info())
#print("code", mem.getcode())
#print("read", mem.read(50))
#print("read", mem.read(50).decode("utf-8")) #euc-kr 디코드함수 자주 붙여서 쓴다


print(urlparse(url))
