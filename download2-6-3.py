from bs4 import BeautifulSoup

fp = open("cars.html",encoding="utf-8")
soup = BeautifulSoup(fp, 'html.parser')

def car_func(seletor):
    print("car_func", soup.select_one(seletor).string)


#람다식
car_lamda = lambda q : print("car_lamda", soup.select_one(q).string)

car_func("#gr")
car_func("li#gr")
car_func("ul > li#gr")
car_func("#cars #gr") #띄어쓰기는 자손
car_func("#cars > #gr") # > 는 자식
car_func("li[id='gr']")

car_lamda("#gr")
car_lamda("li#gr")
car_lamda("ul > li#gr")
car_lamda("#cars #gr") #띄어쓰기는 자손
car_lamda("#cars > #gr") # > 는 자식
car_lamda("li[id='gr']")

print("car_func", soup.select("li")[3].string)
print("car_func", soup.find_all("li")[3].string)
