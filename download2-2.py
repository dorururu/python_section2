import sys
import io
import urllib.request as dw

imgurl = "http://blogfiles.naver.net/MjAxODEwMzBfMjUx/MDAxNTQwODg1ODI1NjU5.0Pj6SJDJgtxyg6uBccmI7brjOmHsg3EyqwgUIx5GITAg.hzqORsQrUZVQyBIfrTTTovTYewc4IsHcW8m2WPYStiQg.JPEG.s4mjeong12/IMG_8338.jpg"
htmlURL = "http://google.com"


savePath1 = "/Users/hyewon/test1.jpg"
savePath2 = "/Users/hyewon/index.html"

#변수 할당 -> 파싱 -> 저장(db)
f = dw.urlopen(imgurl).read()
f2 = dw.urlopen(htmlURL).read()


#방법1
saveFile1 = open(savePath1, 'wb') # w : write , r ; read , a : add
saveFile1.write(f)
saveFile1.close

#방법2 - 얘 사용하는게 낫다
with open(savePath2, 'wb') as saveFile2:
    saveFile2.write(f2)

print("다운로드 완료!")
