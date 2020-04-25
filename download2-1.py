import sys
import io
import urllib.request as dw

imgurl = "http://blogfiles.naver.net/MjAxODEwMzBfMjUx/MDAxNTQwODg1ODI1NjU5.0Pj6SJDJgtxyg6uBccmI7brjOmHsg3EyqwgUIx5GITAg.hzqORsQrUZVQyBIfrTTTovTYewc4IsHcW8m2WPYStiQg.JPEG.s4mjeong12/IMG_8338.jpg"
htmlURL = "http://google.com"


savePath1 = "/Users/hyewon/test1.jpg"
savePath2 = "/Users/hyewon/index.html"

#저장 -> open("r") -> 변수에 할당 -> 파싱 -> 저장
#파싱이 필요없는 데이터 한번에 받을때
dw.urlretrieve(imgurl, savePath1)
dw.urlretrieve(htmlURL, savePath2)

print("다운로드 완료!")
