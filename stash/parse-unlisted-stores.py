import re
import json
import requests
import random
from bs4 import BeautifulSoup

# sets up empty list to store wine data
wines = []

# Domaine LA
domaine_urls = [

	"https://domainela.com/shop/sparkling-wines",
	"https://domainela.com/shop/sparkling-wines?p=2",

	"https://domainela.com/shop/white-wines",
	"https://domainela.com/shop/white-wines?p=2",
	"https://domainela.com/shop/white-wines?p=3",

	"https://domainela.com/shop/orange",

	"https://domainela.com/shop/rose",

	"https://domainela.com/shop/red-wines",
	"https://domainela.com/shop/red-wines?p=2",
	"https://domainela.com/shop/red-wines?p=3",
	"https://domainela.com/shop/red-wines?p=4",

]
for url in domaine_urls:

	# set up soup
	soup = BeautifulSoup(requests.get(url).content, 'html.parser')
	products = soup.find_all("li", class_="product-item")

	for product in products:

		# type
		if 'red' in url:
			type = 'Red'
		if 'white' in url:
			type = 'White'
		if 'orange' in url:
			type = 'Orange'
		if 'rose' in url:
			type = 'Ros&#233;'
		if 'sparkling' in url:
			type = 'Sparkling'
		type_class = type.replace("&#233;", "e").lower()

		# get title string (used for parsing)
		title_string = product.find("a", class_="product-item-link").text.replace(" ", "").lower()

		# title
		title = product.find("a", class_="product-item-link").text.strip()

		# price
		price = product.find("span", class_="price").text.strip()

		# link
		link = product.find("a", class_="product-item-link")['href']

		# image
		imagecheck = product.find("img", class_="product-image-photo")
		if imagecheck is not None:
			image = product.find("img", class_="product-image-photo")['src']
		else:
			image = 'assets/placeholder.png'

		# maker
		if 'lewandowski' in title_string:
			maker = 'Ruth Lewandowski'
		elif 'amevive' in title_string:
			maker = 'Amevive'
		elif 'amplify' in title_string:
			maker = 'Amplify'
		elif 'broc' in title_string:
			maker = 'Broc Cellars'
		elif 'cantinagiardino' in title_string:
			maker = 'Cantina Giardino'
		elif 'cirelli' in title_string:
			maker = 'Cirelli'
		elif 'dueterre' in title_string:
			maker = 'Due Terre'
		elif 'florez' in title_string:
			maker = 'Florez'
		elif 'folkmachine' in title_string:
			maker = 'Folk Machine'
		elif 'furlani' in title_string:
			maker = 'Furlani'
		elif 'gentle folk' in title_string:
			maker = 'Gentle Folk'
		elif 'goodboywine' in title_string:
			maker = 'Good Boy Wine'
		elif 'gutoggau' in title_string:
			maker = 'Gut Oggau'
		elif 'jumbotime' in title_string:
			maker = 'Jumbo Time Wines'
		elif 'kopptisch' in title_string:
			maker = 'Kopptisch'
		elif 'koehnen' in title_string:
			maker = 'Koehnen'
		elif 'lasjaras' in title_string:
			maker = 'Las Jaras'
		elif 'marigny' in title_string:
			maker = 'Marigny'
		elif 'marthastoumen' in title_string:
			maker = 'Martha Stoumen'
		elif 'meinklang' in title_string:
			maker = 'Meinklang'
		elif 'nestarec' in title_string:
			maker = 'Nestarec'
		elif 'oldwestminster' in title_string:
			maker = 'Old Westminster'
		elif 'patricksullivan' in title_string:
			maker = 'Patrick Sullivan'
		elif 'purity' in title_string:
			maker = 'Purity'
		elif 'stagiaire' in title_string:
			maker = 'Stagiaire'
		elif 'scottyboy' in title_string:
			maker = 'Scotty Boy'
		elif 'scotty-boy' in title_string:
			maker = 'Scotty Boy'
		elif 'stagiaire' in title_string:
			maker = 'Stagiaire'
		elif 'subjecttochange' in title_string:
			maker = 'Subject to Change'
		elif 'swick' in title_string:
			maker = 'Swick'
		elif 'wavywines' in title_string:
			maker = 'Wavy Wines'
		elif 'wildarcfarm' in title_string:
			maker = 'Wild Arc Farm'
		elif 'wonderwerk' in title_string:
			maker = 'Wonderwerk'
		else:
			maker ='undefined'

		# add wine to list
		wines.append({
			'Title': title,
			'Maker': maker,
			'Price': price,
			'Link': link,
			'Image': image,
			'Type': type,
			'Type_class': type_class,
			'Store': 'Domaine LA',
			'Store_class': 'domaine',
		})

# Buvon's Wines
buvons_urls = [

	"https://www.buvonswine.com/collections/sparkling",
	"https://www.buvonswine.com/collections/sparkling?page=2",
	"https://www.buvonswine.com/collections/sparkling?page=3",
	"https://www.buvonswine.com/collections/sparkling?page=4",
	"https://www.buvonswine.com/collections/sparkling?page=5",
	"https://www.buvonswine.com/collections/sparkling?page=6",
	"https://www.buvonswine.com/collections/sparkling?page=7",
	"https://www.buvonswine.com/collections/sparkling?page=8",

	"https://www.buvonswine.com/collections/champagne",
	"https://www.buvonswine.com/collections/champagne?page=2",
	"https://www.buvonswine.com/collections/champagne?page=3",
	"https://www.buvonswine.com/collections/champagne?page=4",
	"https://www.buvonswine.com/collections/champagne?page=5",

	"https://www.buvonswine.com/collections/rose",
	"https://www.buvonswine.com/collections/rose?page=2",
	"https://www.buvonswine.com/collections/rose?page=3",
	"https://www.buvonswine.com/collections/rose?page=4",
	"https://www.buvonswine.com/collections/rose?page=5",
	"https://www.buvonswine.com/collections/rose?page=6",
	"https://www.buvonswine.com/collections/rose?page=7",

	"https://www.buvonswine.com/collections/macerated-orange",
	"https://www.buvonswine.com/collections/macerated-orange?page=2",
	"https://www.buvonswine.com/collections/macerated-orange?page=3",
	"https://www.buvonswine.com/collections/macerated-orange?page=4",
	"https://www.buvonswine.com/collections/macerated-orange?page=5",
	"https://www.buvonswine.com/collections/macerated-orange?page=6",
	"https://www.buvonswine.com/collections/macerated-orange?page=7",

	"https://www.buvonswine.com/collections/white",
	"https://www.buvonswine.com/collections/white?page=2",
	"https://www.buvonswine.com/collections/white?page=3",
	"https://www.buvonswine.com/collections/white?page=4",
	"https://www.buvonswine.com/collections/white?page=5",
	"https://www.buvonswine.com/collections/white?page=6",
	"https://www.buvonswine.com/collections/white?page=7",
	"https://www.buvonswine.com/collections/white?page=8",
	"https://www.buvonswine.com/collections/white?page=9",
	"https://www.buvonswine.com/collections/white?page=10",
	"https://www.buvonswine.com/collections/white?page=11",
	"https://www.buvonswine.com/collections/white?page=12",

	"https://www.buvonswine.com/collections/red",
	"https://www.buvonswine.com/collections/red?page=2",
	"https://www.buvonswine.com/collections/red?page=3",
	"https://www.buvonswine.com/collections/red?page=4",
	"https://www.buvonswine.com/collections/red?page=5",
	"https://www.buvonswine.com/collections/red?page=6",
	"https://www.buvonswine.com/collections/red?page=7",
	"https://www.buvonswine.com/collections/red?page=8",
	"https://www.buvonswine.com/collections/red?page=9",
	"https://www.buvonswine.com/collections/red?page=10",
	"https://www.buvonswine.com/collections/red?page=11",
	"https://www.buvonswine.com/collections/red?page=12",
	"https://www.buvonswine.com/collections/red?page=13",
	"https://www.buvonswine.com/collections/red?page=14",
	"https://www.buvonswine.com/collections/red?page=15",

]
for url in buvons_urls:

	# set up soup
	soup = BeautifulSoup(requests.get(url).content, 'html.parser')
	products = soup.find_all("div", class_="u-1/2@phab")

	for product in products:

		# type
		if 'red' in url:
			type = 'Red'
		if 'white' in url:
			type = 'White'
		if 'orange' in url:
			type = 'Orange'
		if 'rose' in url:
			type = 'Ros&#233;'
		if 'sparkling' in url:
			type = 'Sparkling'
		if 'champagne' in url:
			type = 'Sparkling'
		type_class = type.replace("&#233;", "e").lower()

		# get title string (used for parsing)
		title_string = product.find("h2", class_="product__title").text.replace(" ", "").lower()

		# title
		title = product.find("h2", class_="product__title").text.strip()

		# price
		price = product.find("span", class_="product__price-price").text.strip()

		# link
		link = 'www.buvonswine.com' + product.find("a")['href']

		# image
		imagecheck = product.find("img")
		if imagecheck is not None:
			image = product.find("img")['src']
		else:
			image = 'assets/placeholder.png'

		# maker
		if 'lewandowski' in title_string:
			maker = 'Ruth Lewandowski'
		elif 'amevive' in title_string:
			maker = 'Amevive'
		elif 'amplify' in title_string:
			maker = 'Amplify'
		elif 'broc' in title_string:
			maker = 'Broc Cellars'
		elif 'cantinagiardino' in title_string:
			maker = 'Cantina Giardino'
		elif 'cirelli' in title_string:
			maker = 'Cirelli'
		elif 'dueterre' in title_string:
			maker = 'Due Terre'
		elif 'florez' in title_string:
			maker = 'Florez'
		elif 'folkmachine' in title_string:
			maker = 'Folk Machine'
		elif 'furlani' in title_string:
			maker = 'Furlani'
		elif 'gentle folk' in title_string:
			maker = 'Gentle Folk'
		elif 'goodboywine' in title_string:
			maker = 'Good Boy Wine'
		elif 'gutoggau' in title_string:
			maker = 'Gut Oggau'
		elif 'jumbotime' in title_string:
			maker = 'Jumbo Time Wines'
		elif 'kopptisch' in title_string:
			maker = 'Kopptisch'
		elif 'koehnen' in title_string:
			maker = 'Koehnen'
		elif 'lasjaras' in title_string:
			maker = 'Las Jaras'
		elif 'marigny' in title_string:
			maker = 'Marigny'
		elif 'marthastoumen' in title_string:
			maker = 'Martha Stoumen'
		elif 'meinklang' in title_string:
			maker = 'Meinklang'
		elif 'nestarec' in title_string:
			maker = 'Nestarec'
		elif 'oldwestminster' in title_string:
			maker = 'Old Westminster'
		elif 'patricksullivan' in title_string:
			maker = 'Patrick Sullivan'
		elif 'purity' in title_string:
			maker = 'Purity'
		elif 'stagiaire' in title_string:
			maker = 'Stagiaire'
		elif 'scottyboy' in title_string:
			maker = 'Scotty Boy'
		elif 'scotty-boy' in title_string:
			maker = 'Scotty Boy'
		elif 'stagiaire' in title_string:
			maker = 'Stagiaire'
		elif 'subjecttochange' in title_string:
			maker = 'Subject to Change'
		elif 'swick' in title_string:
			maker = 'Swick'
		elif 'wavywines' in title_string:
			maker = 'Wavy Wines'
		elif 'wildarcfarm' in title_string:
			maker = 'Wild Arc Farm'
		elif 'wonderwerk' in title_string:
			maker = 'Wonderwerk'
		else:
			maker ='undefined'

		# add wine to list
		wines.append({
			'Title': title,
			'Maker': maker,
			'Price': price,
			'Link': link,
			'Image': image,
			'Type': type,
			'Type_class': type_class,
			'Store': 'Buvon&#39;s',
			'Store_class': 'buvons',
		})

random.shuffle(wines)

# Write JSON file
with open("data.json", "w") as writeJSON:
	json.dump({'wine': wines}, writeJSON, ensure_ascii=False)

# prints data to terminal (only needed for troubleshooting)
# print(json.dumps(wines, indent=4))
print('success!')
