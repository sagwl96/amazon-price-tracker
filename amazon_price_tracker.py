import requests
from bs4 import BeautifulSoup as BS
import sys
import time
from datetime import datetime
import random

#creating variable to hold url
url = ""

#checking if argument is passed during runtime. If not then use default value
if len(sys.argv) <= 1:
	url = "https://www.amazon.de/Aktivit%C3%A4ts-Tracker-6-monatiger-Premium-Mitgliedschaft-Akkulaufzeit-Tagesform-Index/dp/B09BXQ4HMB"
else:
	url = sys.argv[1]

#initial price threshold. Keep this more than the current price of the item
threshold = 1000

while True:
	#getting the page
	page = requests.get(url ,headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36"})

	soup = BS(page.content, "html.parser")
	price = float(soup.find("span", class_="a-price-whole").text.replace(",","") + "." + soup.find("span", class_="a-price-fraction").text.replace(",",""))

	if price<threshold:
		print("€{} @ {}".format(price, datetime.now()))
		print("The previous price was €{}".format(threshold))
		threshold = price

	time.sleep(random.randint(30,40))