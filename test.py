import re
import json
import requests
import random
from bs4 import BeautifulSoup

# sets up empty list to store wine data
wines = []

vinovoresilverlake_urls = [

	"https://vinovoresilverlake.com/collections/red",
	# "https://vinovoresilverlake.com/collections/red?page=2",
	# "https://vinovoresilverlake.com/collections/red?page=3",
	# "https://vinovoresilverlake.com/collections/red?page=4",
	# "https://vinovoresilverlake.com/collections/red?page=5",
	#
	# "https://vinovoresilverlake.com/collections/white",
	# "https://vinovoresilverlake.com/collections/white?page=2",
	# "https://vinovoresilverlake.com/collections/white?page=3",
	# "https://vinovoresilverlake.com/collections/white?page=4",
	# "https://vinovoresilverlake.com/collections/white?page=5",
	#
	# "https://vinovoresilverlake.com/collections/rose",
	# "https://vinovoresilverlake.com/collections/rose?page=2",
	# "https://vinovoresilverlake.com/collections/rose?page=3",
	# "https://vinovoresilverlake.com/collections/rose?page=4",
	# "https://vinovoresilverlake.com/collections/rose?page=5",
	#
	# "https://vinovoresilverlake.com/collections/orange",
	# "https://vinovoresilverlake.com/collections/orange?page=2",
	# "https://vinovoresilverlake.com/collections/orange?page=3",
	# "https://vinovoresilverlake.com/collections/orange?page=4",
	# "https://vinovoresilverlake.com/collections/orange?page=5",
	#
	# "https://vinovoresilverlake.com/collections/sparkling",
	# "https://vinovoresilverlake.com/collections/sparkling?page=2",
	# "https://vinovoresilverlake.com/collections/sparkling?page=3",
	# "https://vinovoresilverlake.com/collections/sparkling?page=4",
	# "https://vinovoresilverlake.com/collections/sparkling?page=5",

]
for url in vinovoresilverlake_urls:

	# set up soup
	soup = BeautifulSoup(requests.get(url).content, 'html.parser')
	products = soup.find_all("div", class_="product")

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
		title_string = product.find("h3", class_="product__title").text.replace(" ", "").lower()

		# ignore non-wine items
		if 'giftbox' in title_string:
			print()
		elif 'giftbag' in title_string:
			print()
		elif 'bouquet' in title_string:
			print()
		elif 'stopper' in title_string:
			print()
		elif 'tasting' in title_string:
			print()

		# parse wine items
		else:

			# title
			title = product.find("h3", class_="product__title").text.strip()

			# price
			# pricesoup = product.find("p", class_="product__price")
			# if pricesoup.span:
			# 	price = 'On Sale'
			# else:
			# 	price = pricesoup.text.strip()

			# price
			pricesoup = product.find("p", class_="product__price")
			price = pricesoup.text.strip()

			# link
			link = 'http://vinovoresilverlake.com' + product.find("a")['href']

			# image
			imagesoup = product.find('noscript')
			imageurl = imagesoup.find("img", class_="product__img")['src']
			if 'no-image' in imageurl:
				image_type = 'noimage'
			elif imageurl is not None:
				image = 'https:' + imageurl
				image_type = 'hasimage'
			else:
				image_type = 'noimage'

			# maker
			if 'lewandowski' in title_string:
				maker = 'Ruth Lewandowski'
			# elif 'amevive' in title_string:
			# 	maker = 'Amevive'
			# elif 'amplify' in title_string:
			# 	maker = 'Amplify'
			# elif 'broc' in title_string:
				# 	maker = 'Broc Cellars'
			elif 'cantinagiardino' in title_string:
				maker = 'Cantina Giardino'
			# elif 'cirelli' in title_string:
			# 	maker = 'Cirelli'
			# elif 'dueterre' in title_string:
			# 	maker = 'Due Terre'
			# elif 'florez' in title_string:
			# 	maker = 'Florez'
			# elif 'folkmachine' in title_string:
			# 	maker = 'Folk Machine'
			elif 'furlani' in title_string:
				maker = 'Furlani'
			# elif 'gentle folk' in title_string:
			# 	maker = 'Gentle Folk'
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
			# elif 'oldwestminster' in title_string:
			# 	maker = 'Old Westminster'
			elif 'patricksullivan' in title_string:
				maker = 'Patrick Sullivan'
			elif 'purity' in title_string:
				maker = 'Purity'
			# elif 'stagiaire' in title_string:
				# 	maker = 'Stagiaire'
			elif 'scottyboy' in title_string:
				maker = 'Scotty Boy'
			elif 'scotty-boy' in title_string:
				maker = 'Scotty Boy'
			# elif 'stagiaire' in title_string:
				# 	maker = 'Stagiaire'
			# elif 'subjecttochange' in title_string:
			# 	maker = 'Subject to Change'
			elif 'swick' in title_string:
				maker = 'Swick'
			elif 'wavywines' in title_string:
				maker = 'Wavy Wines'
			# elif 'wildarcfarm' in title_string:
				# 	maker = 'Wild Arc Farm'
			elif 'wonderwerk' in title_string:
				maker = 'Wonderwerk'
			else:
				maker ='undefined'

			maker_class = maker.strip().lower()

			print(price)
