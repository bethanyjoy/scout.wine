import re
import json
import requests
import random
from bs4 import BeautifulSoup

# sets up empty list to store wine data
wines = []

# Flask & Field
flaskandfield_urls = [

	"https://flaskandfield.com/collections/wine?filter.p.product_type=Red+Wine&page=2",

]

for url in flaskandfield_urls:

	# set up soup
	soup = BeautifulSoup(requests.get(url).content, 'html.parser')
	products = soup.find_all("li", class_="grid__item")

	for product in products:

		# type
		if 'Red' in url:
			type = 'Red'
		if 'White' in url:
			type = 'White'
		if 'Contact' in url:
			type = 'Orange'
		if 'Ros' in url:
			type = 'Ros&#233;'
		if 'Sparkling' in url:
			type = 'Sparkling'
		type_class = type.replace("&#233;", "e").lower()

		# region
		if 'Italy' in url:
			region = 'Italy'
		elif 'France' in url:
			region = 'France'
		elif 'Austria' in url:
			region = 'Austria'
		elif 'California' in url:
			region = 'California'
		elif 'Spain' in url:
			region = 'Spain + Portugal'
		elif 'South+Africa' in url:
			region = 'South Africa'
		elif 'Chile' in url:
			region = 'Chile'
		elif 'USA' in url:
			region = 'United States'
		elif 'Argentina' in url:
			region = 'Argentina'
		elif 'Portugal' in url:
			region = 'Spain + Portugal'
		elif 'Australia' in url:
			region = 'Australia'
		elif 'Morocco' in url:
			region = 'Morocco'
		else:
			region = 'undefined'

		# get title string (used for parsing)
		title_string = product.find("h3", class_="card__heading").text.replace(" ", "").lower()

		badge_check = product.find("div", class_="card__badge").find("img")

		if 'selects' in title_string:
			print()
		if badge_check:
			print()

		else:

			# title
			title = product.find("h3", class_="card__heading").text.strip().lower()

			# price
			pricesoup = product.find("span", class_="price-item").text.strip()

			# link
			link = 'http://flaskandfield.com' + product.find("a")['href']

			# image
			imagecheck = product.find("img")
			imageurl = product.find("img")['src']
			if 'placeholder' in imageurl:
				image_type = 'noimage'
			elif imageurl is not None:
				image = 'https:' + imageurl
				image_type = 'hasimage'
			else:
				image_type = 'noimage'

			print(title)
