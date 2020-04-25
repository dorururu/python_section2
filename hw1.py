import urllib.request as req
from urllib.parse import urlencode


API = "https://nv.veta.naver.com/fxshow"

values = {
    'su' : 'SU10079',
    'nrefreshx' : '0'
}


print('before', values)
params = urlencode(values)
print('after', params)


url = API + "?" + params
print("요청 url", url)

reqData = req.urlopen(url).read()

savePath = "/Users/hyewon/homework/mainAD.jpg"

with open(savePath, 'wb') as saveFile:
    saveFile.write(reqData)

print("다운로드 완료!")
