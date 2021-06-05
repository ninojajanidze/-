import requests
from bs4 import BeautifulSoup


year1 = input("შეიყვანეთ გამოშვების წელი-დან: ")
year2 = input("შეიყვანეთ გამოშვების წელი-მდე: ")
r = requests.get("https://www.myauto.ge/ka/s/avtomobilebi-" + year1 +"-" + year2 +"?stype=0&year_from=" + year1 + "&year_to=" + year2 + "audi?stype=0&marka=2&price_from=10000&price_to=20000&currency_id=3&det_search=0&ord=7&category_id=m0")

c = r.content
soup = BeautifulSoup(c, "html.parser")

all = soup.find_all("div",{"class": "current-item"})
for item in all:
	print(item.find("h4",{"itemprop":"name"}).text.strip())
	print("ძრავი: " + item.find("div",{"data-info":"ძრავი"}).text.strip())
	print("გარბენი: " + item.find("div",{"data-engin":"გარბენი"}).text.strip())
	print("წელი: " + item.find("p", {"class" : "car-levy car-year"}).text.strip())
	print(item.find_all("span",{"class":"car-price"})[0].text.strip() + "₾")
	print(item.find_all("span",{"class":"car-price"})[1].text.strip() + "$")
	print("\n")