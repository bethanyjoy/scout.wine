import re
import json
import requests
import random
from bs4 import BeautifulSoup

# sets up empty list to store wine data
wines = []

# Everson Royce
eversonroyce_urls = [

	"https://www.eversonroyce.com/collections/red-wines-from-the-usa",
	"https://www.eversonroyce.com/collections/red-wines-from-the-usa?page=2",
	"https://www.eversonroyce.com/collections/red-wines-from-the-usa?page=3",
	"https://www.eversonroyce.com/collections/red-wines-from-the-usa?page=4",
	"https://www.eversonroyce.com/collections/red-wines-from-the-usa?page=5",
	"https://www.eversonroyce.com/collections/red-wines-from-the-usa?page=6",
	"https://www.eversonroyce.com/collections/red-wines-from-the-usa?page=7",
	"https://www.eversonroyce.com/collections/red-wines-from-the-usa?page=8",
	"https://www.eversonroyce.com/collections/red-wines-from-the-usa?page=9",
	"https://www.eversonroyce.com/collections/red-wines-from-the-usa?page=10",
	"https://www.eversonroyce.com/collections/red-wines-from-the-usa?page=11",
	"https://www.eversonroyce.com/collections/red-wines-from-the-usa?page=12",
	"https://www.eversonroyce.com/collections/red-wines-from-the-usa?page=13",
	"https://www.eversonroyce.com/collections/red-wines-from-the-usa?page=14",

	"https://www.eversonroyce.com/collections/french-reds",
	"https://www.eversonroyce.com/collections/french-reds?page=2",
	"https://www.eversonroyce.com/collections/french-reds?page=3",
	"https://www.eversonroyce.com/collections/french-reds?page=4",
	"https://www.eversonroyce.com/collections/french-reds?page=5",
	"https://www.eversonroyce.com/collections/french-reds?page=6",
	"https://www.eversonroyce.com/collections/french-reds?page=7",
	"https://www.eversonroyce.com/collections/french-reds?page=8",
	"https://www.eversonroyce.com/collections/french-reds?page=9",
	"https://www.eversonroyce.com/collections/french-reds?page=10",
	"https://www.eversonroyce.com/collections/french-reds?page=11",
	"https://www.eversonroyce.com/collections/french-reds?page=12",

	"https://www.eversonroyce.com/collections/italian-reds",
	"https://www.eversonroyce.com/collections/italian-reds?page=2",
	"https://www.eversonroyce.com/collections/italian-reds?page=3",
	"https://www.eversonroyce.com/collections/italian-reds?page=4",
	"https://www.eversonroyce.com/collections/italian-reds?page=5",

	"https://www.eversonroyce.com/collections/spanish-portuguese-reds",
	"https://www.eversonroyce.com/collections/spanish-portuguese-reds?page=2",
	"https://www.eversonroyce.com/collections/spanish-portuguese-reds?page=3",
	"https://www.eversonroyce.com/collections/spanish-portuguese-reds?page=4",

	"https://www.eversonroyce.com/collections/eastern-european-reds",
	"https://www.eversonroyce.com/collections/eastern-european-reds?page=2",

	"https://www.eversonroyce.com/collections/reds-from-the-southern-hemisphere",
	"https://www.eversonroyce.com/collections/reds-from-the-southern-hemisphere?page=2",

	"https://www.eversonroyce.com/collections/whites-wines-from-the-usa",
	"https://www.eversonroyce.com/collections/whites-wines-from-the-usa?page=2",
	"https://www.eversonroyce.com/collections/whites-wines-from-the-usa?page=3",
	"https://www.eversonroyce.com/collections/whites-wines-from-the-usa?page=4",
	"https://www.eversonroyce.com/collections/whites-wines-from-the-usa?page=5",

	"https://www.eversonroyce.com/collections/french-white-wine",
	"https://www.eversonroyce.com/collections/french-white-wine?page=2",
	"https://www.eversonroyce.com/collections/french-white-wine?page=3",
	"https://www.eversonroyce.com/collections/french-white-wine?page=4",
	"https://www.eversonroyce.com/collections/french-white-wine?page=5",

	"https://www.eversonroyce.com/collections/italian-white-wine",
	"https://www.eversonroyce.com/collections/italian-white-wine?page=2",
	"https://www.eversonroyce.com/collections/italian-white-wine?page=3",

	"https://www.eversonroyce.com/collections/spanish-portuguese-whites"
	"https://www.eversonroyce.com/collections/spanish-portuguese-whites?page=2"

	"https://www.eversonroyce.com/collections/eastern-european-whites",
	"https://www.eversonroyce.com/collections/eastern-european-whites?page=2",
	"https://www.eversonroyce.com/collections/eastern-european-whites?page=3",
	"https://www.eversonroyce.com/collections/eastern-european-whites?page=4",

	"https://www.eversonroyce.com/collections/white-wines-from-the-southern-hemisphere",
	"https://www.eversonroyce.com/collections/white-wines-from-the-southern-hemisphere?page=2",

	"https://www.eversonroyce.com/collections/rose",
	"https://www.eversonroyce.com/collections/rose?page=2",
	"https://www.eversonroyce.com/collections/rose?page=3",
	"https://www.eversonroyce.com/collections/rose?page=4",

	"https://www.eversonroyce.com/collections/orange-wine",
	"https://www.eversonroyce.com/collections/orange-wine?page=2",
	"https://www.eversonroyce.com/collections/orange-wine?page=3",
	"https://www.eversonroyce.com/collections/orange-wine?page=4",
	"https://www.eversonroyce.com/collections/orange-wine?page=5",

	"https://www.eversonroyce.com/collections/sparklin-wine",
	"https://www.eversonroyce.com/collections/sparklin-wine?page=2",
	"https://www.eversonroyce.com/collections/sparklin-wine?page=3",
	"https://www.eversonroyce.com/collections/sparklin-wine?page=4",
	"https://www.eversonroyce.com/collections/sparklin-wine?page=5",
	"https://www.eversonroyce.com/collections/sparklin-wine?page=6",

]
for url in eversonroyce_urls:

	# set up soup
	soup = BeautifulSoup(requests.get(url).content, 'html.parser')
	products = soup.find_all("div", class_="prod-block")

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
		if 'sparklin' in url:
			type = 'Sparkling'
		type_class = type.replace("&#233;", "e").lower()

		# region
		if 'usa' in url:
			region = 'United States'
		elif 'french' in url:
			region = 'France'
		elif 'italian' in url:
			region = 'Italy'
		elif 'spanish' in url:
			region = 'Spain + Portugal'
		elif 'portuguese' in url:
			region = 'Spain + Portugal'
		elif 'eastern' in url:
			region = 'Eastern Europe'
		elif 'hemisphere' in url:
			region = 'Southern Hemisphere'
		else:
			region = 'undefined'

		# get title string (used for parsing)
		title_string = product.find("div", class_="title").text.replace(" ", "").lower()

		# title
		title = product.find("div", class_="title").text.strip()

		# price
		price = product.find("div", class_="product-price").text.strip()

		# link
		link = 'http://eversonroyce.com' + product.find("a")['href']

		# image
		imagesoup = product.find('noscript')
		imageurl = imagesoup.find("img", class_="rimage__image")['src']
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
			'Image_type': image_type,
			'Type': type,
			'Type_class': type_class,
			'Store': 'Everson Royce',
			'Store_class': 'eversonroyce',
			'Region': region,
		})

# Fancy Free
fancyfree_urls = [
	"https://www.fancyfreeliquor.com/sparkling",
	"https://www.fancyfreeliquor.com/white",
	"https://www.fancyfreeliquor.com/orange",
	"https://www.fancyfreeliquor.com/rose",
	"https://www.fancyfreeliquor.com/red",
]
for url in fancyfree_urls:

	# set up soup
	soup = BeautifulSoup(requests.get(url).content, 'html.parser')
	products = soup.find_all("div", class_="grid-item")

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
		title_string = product.find("div", class_="grid-title").text.replace(" ", "").lower()

		# title
		title = product.find("div", class_="grid-title").text.strip()

		# price
		price = product.find("div", class_="product-price").text.strip()

		# link
		link = 'http://www.fancyfreeliquor.com' + product.find("a")['href']

		# image
		imageurl = product.find("img")['data-src']
		if 'Temporary' in imageurl:
			image_type = 'noimage'
		elif imageurl is not None:
			image = imageurl
			image_type = 'hasimage'
		else:
			image_type = 'noimage'

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
			'Image_type': image_type,
			'Type': type,
			'Type_class': type_class,
			'Store': 'Fancy Free',
			'Store_class': 'fancyfree',
			'Image_type': image_type,
		})

# Flask & Field
flaskandfield_urls = [

	"https://flaskandfield.com/collections/wine?filter.p.product_type=Red+Wine&filter.p.m.custom.region=Italy",
	"https://flaskandfield.com/collections/wine?filter.p.product_type=Red+Wine&filter.p.m.custom.region=France",
	"https://flaskandfield.com/collections/wine?filter.p.product_type=Red+Wine&filter.p.m.custom.region=Austria",
	"https://flaskandfield.com/collections/wine?filter.p.product_type=Red+Wine&filter.p.m.custom.region=California",
	"https://flaskandfield.com/collections/wine?filter.p.product_type=Red+Wine&filter.p.m.custom.region=Spain",
	"https://flaskandfield.com/collections/wine?filter.p.product_type=Red+Wine&filter.p.m.custom.region=South+Africa",
	"https://flaskandfield.com/collections/wine?filter.p.product_type=Red+Wine&filter.p.m.custom.region=Chile",
	"https://flaskandfield.com/collections/wine?filter.p.product_type=Red+Wine&filter.p.m.custom.region=USA",
	"https://flaskandfield.com/collections/wine?filter.p.product_type=Red+Wine&filter.p.m.custom.region=Argentina",
	"https://flaskandfield.com/collections/wine?filter.p.product_type=Red+Wine&filter.p.m.custom.region=Portugal",
	"https://flaskandfield.com/collections/wine?filter.p.product_type=Red+Wine&filter.p.m.custom.region=Australia",
	"https://flaskandfield.com/collections/wine?filter.p.product_type=Red+Wine&filter.p.m.custom.region=Morocco",

	"https://flaskandfield.com/collections/wine?filter.p.product_type=Rosé+Wine&filter.p.m.custom.region=Italy",
	"https://flaskandfield.com/collections/wine?filter.p.product_type=Rosé+Wine&filter.p.m.custom.region=France",
	"https://flaskandfield.com/collections/wine?filter.p.product_type=Rosé+Wine&filter.p.m.custom.region=Austria",
	"https://flaskandfield.com/collections/wine?filter.p.product_type=Rosé+Wine&filter.p.m.custom.region=California",
	"https://flaskandfield.com/collections/wine?filter.p.product_type=Rosé+Wine&filter.p.m.custom.region=Spain",
	"https://flaskandfield.com/collections/wine?filter.p.product_type=Rosé+Wine&filter.p.m.custom.region=South+Africa",
	"https://flaskandfield.com/collections/wine?filter.p.product_type=Rosé+Wine&filter.p.m.custom.region=Chile",
	"https://flaskandfield.com/collections/wine?filter.p.product_type=Rosé+Wine&filter.p.m.custom.region=USA",
	"https://flaskandfield.com/collections/wine?filter.p.product_type=Rosé+Wine&filter.p.m.custom.region=Argentina",
	"https://flaskandfield.com/collections/wine?filter.p.product_type=Rosé+Wine&filter.p.m.custom.region=Portugal",
	"https://flaskandfield.com/collections/wine?filter.p.product_type=Rosé+Wine&filter.p.m.custom.region=Australia",
	"https://flaskandfield.com/collections/wine?filter.p.product_type=Rosé+Wine&filter.p.m.custom.region=Morocco",

	"https://flaskandfield.com/collections/wine?filter.p.product_type=Skin+Contact+Wine&filter.p.m.custom.region=Italy",
	"https://flaskandfield.com/collections/wine?filter.p.product_type=Skin+Contact+Wine&filter.p.m.custom.region=France",
	"https://flaskandfield.com/collections/wine?filter.p.product_type=Skin+Contact+Wine&filter.p.m.custom.region=Austria",
	"https://flaskandfield.com/collections/wine?filter.p.product_type=Skin+Contact+Wine&filter.p.m.custom.region=California",
	"https://flaskandfield.com/collections/wine?filter.p.product_type=Skin+Contact+Wine&filter.p.m.custom.region=Spain",
	"https://flaskandfield.com/collections/wine?filter.p.product_type=Skin+Contact+Wine&filter.p.m.custom.region=South+Africa",
	"https://flaskandfield.com/collections/wine?filter.p.product_type=Skin+Contact+Wine&filter.p.m.custom.region=Chile",
	"https://flaskandfield.com/collections/wine?filter.p.product_type=Skin+Contact+Wine&filter.p.m.custom.region=USA",
	"https://flaskandfield.com/collections/wine?filter.p.product_type=Skin+Contact+Wine&filter.p.m.custom.region=Argentina",
	"https://flaskandfield.com/collections/wine?filter.p.product_type=Skin+Contact+Wine&filter.p.m.custom.region=Portugal",
	"https://flaskandfield.com/collections/wine?filter.p.product_type=Skin+Contact+Wine&filter.p.m.custom.region=Australia",
	"https://flaskandfield.com/collections/wine?filter.p.product_type=Skin+Contact+Wine&filter.p.m.custom.region=Morocco",

	"https://flaskandfield.com/collections/wine?filter.p.product_type=Sparkling+Wine&filter.p.m.custom.region=Italy",
	"https://flaskandfield.com/collections/wine?filter.p.product_type=Sparkling+Wine&filter.p.m.custom.region=France",
	"https://flaskandfield.com/collections/wine?filter.p.product_type=Sparkling+Wine&filter.p.m.custom.region=Austria",
	"https://flaskandfield.com/collections/wine?filter.p.product_type=Sparkling+Wine&filter.p.m.custom.region=California",
	"https://flaskandfield.com/collections/wine?filter.p.product_type=Sparkling+Wine&filter.p.m.custom.region=Spain",
	"https://flaskandfield.com/collections/wine?filter.p.product_type=Sparkling+Wine&filter.p.m.custom.region=South+Africa",
	"https://flaskandfield.com/collections/wine?filter.p.product_type=Sparkling+Wine&filter.p.m.custom.region=Chile",
	"https://flaskandfield.com/collections/wine?filter.p.product_type=Sparkling+Wine&filter.p.m.custom.region=USA",
	"https://flaskandfield.com/collections/wine?filter.p.product_type=Sparkling+Wine&filter.p.m.custom.region=Argentina",
	"https://flaskandfield.com/collections/wine?filter.p.product_type=Sparkling+Wine&filter.p.m.custom.region=Portugal",
	"https://flaskandfield.com/collections/wine?filter.p.product_type=Sparkling+Wine&filter.p.m.custom.region=Australia",
	"https://flaskandfield.com/collections/wine?filter.p.product_type=Sparkling+Wine&filter.p.m.custom.region=Morocco",

	"https://flaskandfield.com/collections/wine?filter.p.product_type=White+Wine&filter.p.m.custom.region=Italy",
	"https://flaskandfield.com/collections/wine?filter.p.product_type=White+Wine&filter.p.m.custom.region=France",
	"https://flaskandfield.com/collections/wine?filter.p.product_type=White+Wine&filter.p.m.custom.region=Austria",
	"https://flaskandfield.com/collections/wine?filter.p.product_type=White+Wine&filter.p.m.custom.region=California",
	"https://flaskandfield.com/collections/wine?filter.p.product_type=White+Wine&filter.p.m.custom.region=Spain",
	"https://flaskandfield.com/collections/wine?filter.p.product_type=White+Wine&filter.p.m.custom.region=South+Africa",
	"https://flaskandfield.com/collections/wine?filter.p.product_type=White+Wine&filter.p.m.custom.region=Chile",
	"https://flaskandfield.com/collections/wine?filter.p.product_type=White+Wine&filter.p.m.custom.region=USA",
	"https://flaskandfield.com/collections/wine?filter.p.product_type=White+Wine&filter.p.m.custom.region=Argentina",
	"https://flaskandfield.com/collections/wine?filter.p.product_type=White+Wine&filter.p.m.custom.region=Portugal",
	"https://flaskandfield.com/collections/wine?filter.p.product_type=White+Wine&filter.p.m.custom.region=Australia",
	"https://flaskandfield.com/collections/wine?filter.p.product_type=White+Wine&filter.p.m.custom.region=Morocco",

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

		# title
		title = product.find("h3", class_="card__heading").text.strip()

		# price
		price = product.find("span", class_="price-item").text.strip()

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
			'Image_type': image_type,
			'Type': type,
			'Type_class': type_class,
			'Store': 'Flask + Field',
			'Store_class': 'flaskandfield',
			'Region': region,
			'Image_type': image_type,
		})

# Heaven's Market
heavensmarket_urls = [

	"https://www.heavensmarketla.com/collections/red",
	"https://www.heavensmarketla.com/collections/red?page=2",
	"https://www.heavensmarketla.com/collections/red?page=3",
	"https://www.heavensmarketla.com/collections/red?page=4",
	"https://www.heavensmarketla.com/collections/red?page=5",

	"https://www.heavensmarketla.com/collections/white",
	"https://www.heavensmarketla.com/collections/white?page=2",
	"https://www.heavensmarketla.com/collections/white?page=3",
	"https://www.heavensmarketla.com/collections/white?page=4",

	"https://www.heavensmarketla.com/collections/rose",
	"https://www.heavensmarketla.com/collections/rose?page=2",

	"https://www.heavensmarketla.com/collections/skin-contact",
	"https://www.heavensmarketla.com/collections/skin-contact?page=2",
	"https://www.heavensmarketla.com/collections/skin-contact?page=3",
	"https://www.heavensmarketla.com/collections/skin-contact?page=4",

	"https://www.heavensmarketla.com/collections/sparkling",
	"https://www.heavensmarketla.com/collections/sparkling?page=2",
	"https://www.heavensmarketla.com/collections/sparkling?page=3",
	"https://www.heavensmarketla.com/collections/sparkling?page=4",

]
for url in heavensmarket_urls:

	# set up soup
	soup = BeautifulSoup(requests.get(url).content, 'html.parser')
	products = soup.find_all("li", class_="grid__item")

	for product in products:

		# type
		if 'red' in url:
			type = 'Red'
		if 'white' in url:
			type = 'White'
		if 'contact' in url:
			type = 'Orange'
		if 'rose' in url:
			type = 'Ros&#233;'
		if 'sparkling' in url:
			type = 'Sparkling'
		type_class = type.replace("&#233;", "e").lower()

		# get title string (used for parsing)
		title_string = product.find("span", class_="visually-hidden").text.replace(" ", "").lower()

		# title
		title = product.find("span", class_="visually-hidden").text.strip()

		# ignore non-wine items
		if 'wineclass' in title_string:
			print()

		# parse wine items
		else:

			#price
			price = product.find("span", class_="price-item").text.strip()

			#link
			link = 'http://heavensmarketla.com' + product.find("a", class_="grid-view-item__link")['href']

			# image
			imagesoup = product.find('noscript')
			imageurl = imagesoup.find("img", class_="grid-view-item__image")['src']
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
				'Image_type': image_type,
				'Image_type': image_type,
				'Type': type,
				'Type_class': type_class,
				'Store': 'Heaven&#39;s Market',
				'Store_class': 'heavensmarket',
			})

# Helen's Wine
helens_urls = [
	"https://helenswines.com/collections/sparkling/australia",
	"https://helenswines.com/collections/sparkling/austria",
	"https://helenswines.com/collections/sparkling/chile",
	"https://helenswines.com/collections/sparkling/corsica",
	"https://helenswines.com/collections/sparkling/domestic",
	"https://helenswines.com/collections/sparkling/france",
	"https://helenswines.com/collections/sparkling/france?page=2",
	"https://helenswines.com/collections/sparkling/germany",
	"https://helenswines.com/collections/sparkling/italy",
	"https://helenswines.com/collections/sparkling/portugal",
	"https://helenswines.com/collections/sparkling/spain",
	"https://helenswines.com/collections/white/australia",
	"https://helenswines.com/collections/white/austria",
	"https://helenswines.com/collections/white/austria?page=2",
	"https://helenswines.com/collections/white/chile",
	"https://helenswines.com/collections/white/corsica",
	"https://helenswines.com/collections/white/domestic",
	"https://helenswines.com/collections/white/domestic?page=2",
	"https://helenswines.com/collections/white/france",
	"https://helenswines.com/collections/white/france?page=2",
	"https://helenswines.com/collections/white/france?page=3",
	"https://helenswines.com/collections/white/germany",
	"https://helenswines.com/collections/white/italy",
	"https://helenswines.com/collections/white/italy?page=2",
	"https://helenswines.com/collections/white/portugal",
	"https://helenswines.com/collections/white/spain",
	"https://helenswines.com/collections/rose/australia",
	"https://helenswines.com/collections/rose/austria",
	"https://helenswines.com/collections/rose/chile",
	"https://helenswines.com/collections/rose/corsica",
	"https://helenswines.com/collections/rose/domestic",
	"https://helenswines.com/collections/rose/france",
	"https://helenswines.com/collections/rose/germany",
	"https://helenswines.com/collections/rose/italy",
	"https://helenswines.com/collections/rose/portugal",
	"https://helenswines.com/collections/rose/spain",
	"https://helenswines.com/collections/red/australia",
	"https://helenswines.com/collections/red/austria",
	"https://helenswines.com/collections/red/chile",
	"https://helenswines.com/collections/red/corsica",
	"https://helenswines.com/collections/red/domestic",
	"https://helenswines.com/collections/red/domestic?page=2",
	"https://helenswines.com/collections/red/france",
	"https://helenswines.com/collections/red/france?page=2",
	"https://helenswines.com/collections/red/france?page=3",
	"https://helenswines.com/collections/red/germany",
	"https://helenswines.com/collections/red/italy",
	"https://helenswines.com/collections/red/italy?page=2",
	"https://helenswines.com/collections/red/italy?page=3",
	"https://helenswines.com/collections/red/portugal",
	"https://helenswines.com/collections/red/spain",
	"https://helenswines.com/collections/orange/australia",
	"https://helenswines.com/collections/orange/austria",
	"https://helenswines.com/collections/orange/chile",
	"https://helenswines.com/collections/orange/corsica",
	"https://helenswines.com/collections/orange/domestic",
	"https://helenswines.com/collections/orange/france",
	"https://helenswines.com/collections/orange/france?page=2",
	"https://helenswines.com/collections/orange/germany",
	"https://helenswines.com/collections/orange/italy?page=2",
	"https://helenswines.com/collections/orange/italy",
	"https://helenswines.com/collections/orange/portugal",
	"https://helenswines.com/collections/orange/spain",
]
for url in helens_urls:

	# set up soup
	soup = BeautifulSoup(requests.get(url).content, 'html.parser')
	products = soup.find_all("div", class_="grid-product")

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

		# region
		if 'australia' in url:
			region = 'Australia'
		elif 'austria' in url:
			region = 'Austria'
		elif 'chile' in url:
			region = 'Chile'
		elif 'corsica' in url:
			region = 'Corsica'
		elif 'domestic' in url:
			region = 'United States'
		elif 'france' in url:
			region = 'France'
		elif 'germany' in url:
			region = 'Germany'
		elif 'italy' in url:
			region = 'Italy'
		elif 'portugal' in url:
			region = 'Spain + Portugal'
		elif 'spain' in url:
			region = 'Spain + Portugal'
		else:
			region = 'undefined'

		# get title string (used for parsing)
		title_string = product.find("div", class_="grid-product__title--body").text.replace(" ", "").lower()

		# title
		title = product.find("div", class_="grid-product__title--body").text.strip()

		# price
		price = product.find("div", class_="grid-product__price").text.strip()

		# link
		link = 'http://helenswines.com' + product.find("a")['href']

		# image
		imagesoup = product.find('noscript')
		imageurl = imagesoup.find("img", class_="grid-product__image")['src']
		if 'comingsoon' in imageurl:
			image_type = 'noimage'
		elif imageurl is not None:
			image = 'https:' + imageurl
			image_type = 'hasimage'
		else:
			image_type = 'noimage'

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
			'Image_type': image_type,
			'Type': type,
			'Type_class': type_class,
			'Store': 'Helen&#39;s Wines',
			'Store_class': 'helens',
			'Region': region,
		})

# Highland Park Wine
highlandpark_urls = [

	"https://www.highlandparkwine.com/collections/usa-red-wines",
	"https://www.highlandparkwine.com/collections/usa-red-wines?page=2",
	"https://www.highlandparkwine.com/collections/usa-red-wines?page=3",
	"https://www.highlandparkwine.com/collections/usa-red-wines?page=4",
	"https://www.highlandparkwine.com/collections/usa-red-wines?page=5",
	"https://www.highlandparkwine.com/collections/usa-red-wines?page=6",
	"https://www.highlandparkwine.com/collections/usa-red-wines?page=7",

	"https://www.highlandparkwine.com/collections/french-reds",
	"https://www.highlandparkwine.com/collections/french-reds?page=2",
	"https://www.highlandparkwine.com/collections/french-reds?page=3",
	"https://www.highlandparkwine.com/collections/french-reds?page=4",
	"https://www.highlandparkwine.com/collections/french-reds?page=5",
	"https://www.highlandparkwine.com/collections/french-reds?page=6",
	"https://www.highlandparkwine.com/collections/french-reds?page=7",
	"https://www.highlandparkwine.com/collections/french-reds?page=8",

	"https://www.highlandparkwine.com/collections/italian-reds",
	"https://www.highlandparkwine.com/collections/italian-reds?page=2",
	"https://www.highlandparkwine.com/collections/italian-reds?page=3",
	"https://www.highlandparkwine.com/collections/italian-reds?page=4",

	"https://www.highlandparkwine.com/collections/spanish-portuguese-reds",
	"https://www.highlandparkwine.com/collections/spanish-portuguese-reds?page=2",
	"https://www.highlandparkwine.com/collections/spanish-portuguese-reds?page=3",

	"https://www.highlandparkwine.com/collections/eastern-european-reds",
	"https://www.highlandparkwine.com/collections/eastern-european-reds?page=2",
	"https://www.highlandparkwine.com/collections/eastern-european-reds?page=3",

	"https://www.highlandparkwine.com/collections/reds-from-the-southern-hemisphere",
	"https://www.highlandparkwine.com/collections/reds-from-the-southern-hemisphere?page=2",
	"https://www.highlandparkwine.com/collections/reds-from-the-southern-hemisphere?page=3",
	"https://www.highlandparkwine.com/collections/reds-from-the-southern-hemisphere?page=4",

	"https://www.highlandparkwine.com/collections/white-wines-from-the-usa",
	"https://www.highlandparkwine.com/collections/white-wines-from-the-usa?page=2",
	"https://www.highlandparkwine.com/collections/white-wines-from-the-usa?page=3",
	"https://www.highlandparkwine.com/collections/white-wines-from-the-usa?page=4",

	"https://www.highlandparkwine.com/collections/french-white-wine",
	"https://www.highlandparkwine.com/collections/french-white-wine?page=2",
	"https://www.highlandparkwine.com/collections/french-white-wine?page=3",
	"https://www.highlandparkwine.com/collections/french-white-wine?page=4",
	"https://www.highlandparkwine.com/collections/french-white-wine?page=5",

	"https://www.highlandparkwine.com/collections/italian-white-wine",
	"https://www.highlandparkwine.com/collections/italian-white-wine?page=2",
	"https://www.highlandparkwine.com/collections/italian-white-wine?page=2",
	"https://www.highlandparkwine.com/collections/italian-white-wine?page=3",
	"https://www.highlandparkwine.com/collections/italian-white-wine?page=4",

	"https://www.highlandparkwine.com/collections/spanish-portuguese-whites",
	"https://www.highlandparkwine.com/collections/spanish-portuguese-whites?page=2",
	"https://www.highlandparkwine.com/collections/spanish-portuguese-whites?page=3",

	"https://www.highlandparkwine.com/collections/eastern-european-whites",
	"https://www.highlandparkwine.com/collections/eastern-european-whites?page=2",
	"https://www.highlandparkwine.com/collections/eastern-european-whites?page=3",
	"https://www.highlandparkwine.com/collections/eastern-european-whites?page=4",

	"https://www.highlandparkwine.com/collections/white-wines-from-the-southern-hemisphere",
	"https://www.highlandparkwine.com/collections/white-wines-from-the-southern-hemisphere?page=2",

	"https://www.highlandparkwine.com/collections/rose",
	"https://www.highlandparkwine.com/collections/rose?page=2",
	"https://www.highlandparkwine.com/collections/rose?page=3",
	"https://www.highlandparkwine.com/collections/rose?page=4",
	"https://www.highlandparkwine.com/collections/rose?page=5",

	"https://www.highlandparkwine.com/collections/orange-wine",
	"https://www.highlandparkwine.com/collections/orange-wine?page=2",
	"https://www.highlandparkwine.com/collections/orange-wine?page=3",
	"https://www.highlandparkwine.com/collections/orange-wine?page=4",

	"https://www.highlandparkwine.com/collections/sparkling-wine",
	"https://www.highlandparkwine.com/collections/sparkling-wine?page=2",
	"https://www.highlandparkwine.com/collections/sparkling-wine?page=3",
	"https://www.highlandparkwine.com/collections/sparkling-wine?page=4",
	"https://www.highlandparkwine.com/collections/sparkling-wine?page=5",
	"https://www.highlandparkwine.com/collections/sparkling-wine?page=6",

]
for url in highlandpark_urls:

	# set up soup
	soup = BeautifulSoup(requests.get(url).content, 'html.parser')
	products = soup.find_all("div", class_="prod-block")

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

		# region
		if 'usa' in url:
			region = 'United States'
		elif 'french' in url:
			region = 'France'
		elif 'italian' in url:
			region = 'Italy'
		elif 'spanish' in url:
			region = 'Spain + Portugal'
		elif 'portuguese' in url:
			region = 'Spain + Portugal'
		elif 'eastern' in url:
			region = 'Eastern Europe'
		elif 'hemisphere' in url:
			region = 'Southern Hemisphere'
		else:
			region = 'undefined'

		# get title string (used for parsing)
		title_string = product.find("div", class_="title").text.replace(" ", "").lower()

		# title
		title = product.find("div", class_="title").text.strip()

		# price
		price = product.find("div", class_="product-price").text.strip()

		# link
		link = 'http://highlandparkwine.com' + product.find("a")['href']

		# image
		imagesoup = product.find('noscript')
		imageurl = imagesoup.find("img", class_="rimage__image")['src']
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
			'Image_type': image_type,
			'Type': type,
			'Type_class': type_class,
			'Store': 'Highland Park Wine',
			'Store_class': 'highlandpark',
			'Region': region,
		})

# Kamp
kamp_urls = [
	"https://shopkamp.com/collections/red/austria",
	"https://shopkamp.com/collections/red/california",
	"https://shopkamp.com/collections/red/france",
	"https://shopkamp.com/collections/red/germany",
	"https://shopkamp.com/collections/red/greece",
	"https://shopkamp.com/collections/red/italy",
	"https://shopkamp.com/collections/red/oregon",
	"https://shopkamp.com/collections/red/spain",
	"https://shopkamp.com/collections/chillable-reds/austria",
	"https://shopkamp.com/collections/chillable-reds/california",
	"https://shopkamp.com/collections/chillable-reds/france",
	"https://shopkamp.com/collections/chillable-reds/germany",
	"https://shopkamp.com/collections/chillable-reds/greece",
	"https://shopkamp.com/collections/chillable-reds/italy",
	"https://shopkamp.com/collections/chillable-reds/oregon",
	"https://shopkamp.com/collections/chillable-reds/spain",
	"https://shopkamp.com/collections/white/austria",
	"https://shopkamp.com/collections/white/california",
	"https://shopkamp.com/collections/white/france",
	"https://shopkamp.com/collections/white/germany",
	"https://shopkamp.com/collections/white/greece",
	"https://shopkamp.com/collections/white/italy",
	"https://shopkamp.com/collections/white/oregon",
	"https://shopkamp.com/collections/white/spain",
	"https://shopkamp.com/collections/rose/austria",
	"https://shopkamp.com/collections/rose/california",
	"https://shopkamp.com/collections/rose/france",
	"https://shopkamp.com/collections/rose/germany",
	"https://shopkamp.com/collections/rose/greece",
	"https://shopkamp.com/collections/rose/italy",
	"https://shopkamp.com/collections/rose/oregon",
	"https://shopkamp.com/collections/rose/spain",
	"https://shopkamp.com/collections/orange/austria",
	"https://shopkamp.com/collections/orange/california",
	"https://shopkamp.com/collections/orange/france",
	"https://shopkamp.com/collections/orange/germany",
	"https://shopkamp.com/collections/orange/greece",
	"https://shopkamp.com/collections/orange/italy",
	"https://shopkamp.com/collections/orange/oregon",
	"https://shopkamp.com/collections/orange/spain",
	"https://shopkamp.com/collections/sparkling/austria",
	"https://shopkamp.com/collections/sparkling/california",
	"https://shopkamp.com/collections/sparkling/france",
	"https://shopkamp.com/collections/sparkling/germany",
	"https://shopkamp.com/collections/sparkling/greece",
	"https://shopkamp.com/collections/sparkling/italy",
	"https://shopkamp.com/collections/sparkling/oregon",
	"https://shopkamp.com/collections/sparkling/spain",
]
for url in kamp_urls:

	# set up soup
	soup = BeautifulSoup(requests.get(url).content, 'html.parser')
	products = soup.find_all("div", class_="product--root")

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
		# if 'chillable' in url:
		# 	type = 'Chillable Red'
		type_class = type.replace("&#233;", "e").replace(" ", "").lower()

		# region
		if 'austria' in url:
			region = 'Austria'
		elif 'california' in url:
			region = 'California'
		elif 'france' in url:
			region = 'France'
		elif 'germany' in url:
			region = 'Germany'
		elif 'greece' in url:
			region = 'Greece'
		elif 'italy' in url:
			region = 'Italy'
		elif 'oregon' in url:
			region = 'Oregon'
		elif 'spain' in url:
			region = 'Spain + Portugal'
		else:
			region = 'undefined'

		# title
		title_name = product.find("p", class_="product--title").text.strip()
		title_maker = product.find("div", class_="product--vendor").text.strip()
		title = title_maker + " " + title_name

		# get title string (used for parsing)
		title_string = title.replace(" ", "").lower()

		# price
		price = product.find("span", class_="product--price money").text.strip()

		# link
		link = 'http://shopkamp.com' + product.find("a")['href']

		# image
		imagesoup = product.find('noscript')
		imagecheck = imagesoup.find("img")
		if imagecheck is not None:
			imageurl = imagesoup.find("img")['src']
			image = 'https:' + imageurl
			image_type = 'hasimage'
		else:
			image_type = 'noimage'

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
			'Image_type': image_type,
			'Type': type,
			'Type_class': type_class,
			'Store': 'Kamp',
			'Store_class': 'kamp',
			'Region': region,
		})

# Silverlake Wine
silverlake_urls = [

	"https://silverlakewine.com/collections/red",
	"https://silverlakewine.com/collections/red?page=2",
	"https://silverlakewine.com/collections/red?page=3",
	"https://silverlakewine.com/collections/red?page=4",
	"https://silverlakewine.com/collections/red?page=5",
	"https://silverlakewine.com/collections/red?page=6",
	"https://silverlakewine.com/collections/red?page=7",
	"https://silverlakewine.com/collections/red?page=8",
	"https://silverlakewine.com/collections/red?page=9",
	"https://silverlakewine.com/collections/red?page=10",
	"https://silverlakewine.com/collections/red?page=11",
	"https://silverlakewine.com/collections/red?page=12",
	"https://silverlakewine.com/collections/red?page=13",
	"https://silverlakewine.com/collections/red?page=14",
	"https://silverlakewine.com/collections/red?page=15",
	"https://silverlakewine.com/collections/red?page=16",
	"https://silverlakewine.com/collections/red?page=17",
	"https://silverlakewine.com/collections/red?page=18",
	"https://silverlakewine.com/collections/red?page=19",
	"https://silverlakewine.com/collections/red?page=20",
	"https://silverlakewine.com/collections/red?page=21",
	"https://silverlakewine.com/collections/red?page=22",
	"https://silverlakewine.com/collections/red?page=23",
	"https://silverlakewine.com/collections/red?page=24",
	"https://silverlakewine.com/collections/red?page=25",
	"https://silverlakewine.com/collections/red?page=26",

	"https://silverlakewine.com/collections/white",
	"https://silverlakewine.com/collections/white?page=2",
	"https://silverlakewine.com/collections/white?page=3",
	"https://silverlakewine.com/collections/white?page=4",
	"https://silverlakewine.com/collections/white?page=5",
	"https://silverlakewine.com/collections/white?page=6",
	"https://silverlakewine.com/collections/white?page=7",
	"https://silverlakewine.com/collections/white?page=8",
	"https://silverlakewine.com/collections/white?page=9",
	"https://silverlakewine.com/collections/white?page=10",
	"https://silverlakewine.com/collections/white?page=11",
	"https://silverlakewine.com/collections/white?page=12",
	"https://silverlakewine.com/collections/white?page=13",
	"https://silverlakewine.com/collections/white?page=14",

	"https://silverlakewine.com/collections/rose",
	"https://silverlakewine.com/collections/rose?page=2",
	"https://silverlakewine.com/collections/rose?page=3",
	"https://silverlakewine.com/collections/rose?page=4",
	"https://silverlakewine.com/collections/rose?page=5",
	"https://silverlakewine.com/collections/rose?page=6",

	"https://silverlakewine.com/collections/orange",
	"https://silverlakewine.com/collections/orange?page=2",
	"https://silverlakewine.com/collections/orange?page=3",
	"https://silverlakewine.com/collections/orange?page=4",
	"https://silverlakewine.com/collections/orange?page=5",
	"https://silverlakewine.com/collections/orange?page=6",

	"https://silverlakewine.com/collections/sparkling",
	"https://silverlakewine.com/collections/sparkling?page=2",
	"https://silverlakewine.com/collections/sparkling?page=3",
	"https://silverlakewine.com/collections/sparkling?page=4",
	"https://silverlakewine.com/collections/sparkling?page=5",
	"https://silverlakewine.com/collections/sparkling?page=6",
	"https://silverlakewine.com/collections/sparkling?page=7",
	"https://silverlakewine.com/collections/sparkling?page=8",

	"https://silverlakewine.com/collections/fruit-wine",

	"https://silverlakewine.com/collections/piquette",

]
for url in silverlake_urls:

	# set up soup
	soup = BeautifulSoup(requests.get(url).content, 'html.parser')
	products = soup.find_all("div", class_="prod-block")

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
		if 'fruit' in url:
			type = 'Co-Fermented'
		if 'piquette' in url:
			type = 'Piquette'
		type_class = type.replace("&#233;", "e").lower()

		# get title string (used for parsing)
		title_string = product.find("div", class_="title").text.replace(" ", "").lower()

		# title
		title = product.find("div", class_="title").text.strip()

		# price
		price = product.find("div", class_="product-price").text.strip()

		# link
		link = 'http://silverlakewine.com' + product.find("a")['href']

		# image
		imagesoup = product.find('noscript')
		imageurl = imagesoup.find("img", class_="rimage__image")['src']
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
			'Image_type': image_type,
			'Type': type,
			'Type_class': type_class,
			'Store': 'Silverlake Wine',
			'Store_class': 'silverlake',
		})

# Sip Snack
sipsnack_urls = [

	"https://www.sipsnackshop.com/collections/red-wine-white-wine-bubbles/champagne",
	"https://www.sipsnackshop.com/collections/red-wine-white-wine-bubbles/champagne?page=2",

	"https://www.sipsnackshop.com/collections/red-wine-white-wine-bubbles/chillable-red",
	"https://www.sipsnackshop.com/collections/red-wine-white-wine-bubbles/chillable-red?page=2",

	"https://www.sipsnackshop.com/collections/red-wine-white-wine-bubbles/orange-wine",
	"https://www.sipsnackshop.com/collections/red-wine-white-wine-bubbles/orange-wine?page=2",

	"https://www.sipsnackshop.com/collections/red-wine-white-wine-bubbles/pet-nat",
	"https://www.sipsnackshop.com/collections/red-wine-white-wine-bubbles/pet-nat?page=2",

	"https://www.sipsnackshop.com/collections/red-wine-white-wine-bubbles/red-wine",
	"https://www.sipsnackshop.com/collections/red-wine-white-wine-bubbles/red-wine?page=2",

	"https://www.sipsnackshop.com/collections/red-wine-white-wine-bubbles/rose",
	"https://www.sipsnackshop.com/collections/red-wine-white-wine-bubbles/rose?page=2",

	"https://www.sipsnackshop.com/collections/red-wine-white-wine-bubbles/rose-wine",
	"https://www.sipsnackshop.com/collections/red-wine-white-wine-bubbles/rose-wine?page=2",

	"https://www.sipsnackshop.com/collections/red-wine-white-wine-bubbles/sparkling-wine",
	"https://www.sipsnackshop.com/collections/red-wine-white-wine-bubbles/sparkling-wine?page=2",

	"https://www.sipsnackshop.com/collections/red-wine-white-wine-bubbles/white",
	"https://www.sipsnackshop.com/collections/red-wine-white-wine-bubbles/white?page=2",

	"https://www.sipsnackshop.com/collections/red-wine-white-wine-bubbles/white-wine",
	"https://www.sipsnackshop.com/collections/red-wine-white-wine-bubbles/white-wine?page=2",

]
for url in sipsnack_urls:

	# set up soup
	soup = BeautifulSoup(requests.get(url).content, 'html.parser')
	products = soup.find_all("div", class_="product--root")

	for product in products:

		# type
		if 'champagne' in url:
			type = 'Sparkling'
		if 'pet-nat' in url:
			type = 'Sparkling'
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
		title_string = product.find("h3", class_="product--title").text.replace(" ", "").lower()

		# title
		title = product.find("h3", class_="product--title").text.strip()

		# price
		price = product.find("span", class_="product--price").text.strip()

		# link
		link = 'http://www.sipsnackshop.com' + product.find("a")['href']

		# image
		imagesoup = product.find('noscript')
		imageurl = imagesoup.find("img")['src']
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
			'Image_type': image_type,
			'Type': type,
			'Type_class': type_class,
			'Store': 'Sip Snack',
			'Store_class': 'sipsnack',
		})

# Vinovore Eagle Rock
vinovoreeaglerock_urls = [

	"https://vinovoreeaglerock.com/collections/red",
	"https://vinovoreeaglerock.com/collections/red?page=2",
	"https://vinovoreeaglerock.com/collections/red?page=3",
	"https://vinovoreeaglerock.com/collections/red?page=4",
	"https://vinovoreeaglerock.com/collections/red?page=5",
	"https://vinovoreeaglerock.com/collections/red?page=6",
	"https://vinovoreeaglerock.com/collections/red?page=7",
	"https://vinovoreeaglerock.com/collections/red?page=8",

	"https://vinovoreeaglerock.com/collections/white",
	"https://vinovoreeaglerock.com/collections/white?page=2",
	"https://vinovoreeaglerock.com/collections/white?page=3",
	"https://vinovoreeaglerock.com/collections/white?page=4",
	"https://vinovoreeaglerock.com/collections/white?page=5",
	"https://vinovoreeaglerock.com/collections/white?page=6",

	"https://vinovoreeaglerock.com/collections/orange",
	"https://vinovoreeaglerock.com/collections/orange?page=2",
	"https://vinovoreeaglerock.com/collections/orange?page=3",
	"https://vinovoreeaglerock.com/collections/orange?page=4",

	"https://vinovoreeaglerock.com/collections/rose",
	"https://vinovoreeaglerock.com/collections/rose?page=2",
	"https://vinovoreeaglerock.com/collections/rose?page=3",
	"https://vinovoreeaglerock.com/collections/rose?page=4",

	"https://vinovoreeaglerock.com/collections/sparkling",
	"https://vinovoreeaglerock.com/collections/sparkling?page=2",
	"https://vinovoreeaglerock.com/collections/sparkling?page=3",
	"https://vinovoreeaglerock.com/collections/sparkling?page=4",
	"https://vinovoreeaglerock.com/collections/sparkling?page=5",
	"https://vinovoreeaglerock.com/collections/sparkling?page=6",

]
for url in vinovoreeaglerock_urls:

	# set up soup
	soup = BeautifulSoup(requests.get(url).content, 'html.parser')
	products = soup.find_all("div", class_="grid-product")

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
		title_string = product.find("div", class_="grid-product__title").text.replace(" ", "").lower()

		# ignore non-wine items
		if 'giftbox' in title_string:
			print()
		elif 'bouquet' in title_string:
			print()
		elif 'stopper' in title_string:
			print()

		# parse wine items
		else:

			# title
			title = product.find("div", class_="grid-product__title").text.strip()

			# price
			pricesoup = product.find("div", class_="grid-product__price")
			if pricesoup.span:
				price = 'On Sale'
			else:
				price = pricesoup.text.strip()

			# link
			link = 'http://vinovoreeaglerock.com' + product.find("a")['href']

			# image
			imagesoup = product.find('noscript')
			imageurl = imagesoup.find("img", class_="grid-product__image")['src']
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
				'Image_type': image_type,
				'Type': type,
				'Type_class': type_class,
				'Store': 'Vinovore Eagle Rock',
				'Store_class': 'vinovoreeaglerock',
			})

# Vinovore Silverlake
vinovoresilverlake_urls = [

	"https://vinovoresilverlake.com/collections/red",
	"https://vinovoresilverlake.com/collections/red?page=2",
	"https://vinovoresilverlake.com/collections/red?page=3",
	"https://vinovoresilverlake.com/collections/red?page=4",
	"https://vinovoresilverlake.com/collections/red?page=5",

	"https://vinovoresilverlake.com/collections/white",
	"https://vinovoresilverlake.com/collections/white?page=2",
	"https://vinovoresilverlake.com/collections/white?page=3",
	"https://vinovoresilverlake.com/collections/white?page=4",
	"https://vinovoresilverlake.com/collections/white?page=5",

	"https://vinovoresilverlake.com/collections/rose",
	"https://vinovoresilverlake.com/collections/rose?page=2",
	"https://vinovoresilverlake.com/collections/rose?page=3",
	"https://vinovoresilverlake.com/collections/rose?page=4",
	"https://vinovoresilverlake.com/collections/rose?page=5",

	"https://vinovoresilverlake.com/collections/orange",
	"https://vinovoresilverlake.com/collections/orange?page=2",
	"https://vinovoresilverlake.com/collections/orange?page=3",
	"https://vinovoresilverlake.com/collections/orange?page=4",
	"https://vinovoresilverlake.com/collections/orange?page=5",

	"https://vinovoresilverlake.com/collections/sparkling",
	"https://vinovoresilverlake.com/collections/sparkling?page=2",
	"https://vinovoresilverlake.com/collections/sparkling?page=3",
	"https://vinovoresilverlake.com/collections/sparkling?page=4",
	"https://vinovoresilverlake.com/collections/sparkling?page=5",

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

		# parse wine items
		else:

			# title
			title = product.find("h3", class_="product__title").text.strip()

			# price
			pricesoup = product.find("p", class_="product__price")
			if pricesoup.span:
				price = 'On Sale'
			else:
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
				'Image_type': image_type,
				'Type': type,
				'Type_class': type_class,
				'Store': 'Vinovore Silverlake',
				'Store_class': 'vinovoresilverlake',
			})

# Wine + Eggs
wineandeggs_urls = [

	"https://wineandeggs.com/collections/red-wine",
	"https://wineandeggs.com/collections/white-wine",
	"https://wineandeggs.com/collections/wine-rose",
	"https://wineandeggs.com/collections/skin-contact-wine",
	"https://wineandeggs.com/collections/sparkling-wine",
	"https://wineandeggs.com/collections/co-fermented",
	"https://wineandeggs.com/collections/piquette-wine",

]
for url in wineandeggs_urls:

	# set up soup
	soup = BeautifulSoup(requests.get(url).content, 'html.parser')
	products = soup.find_all("div", class_="product-block")

	for product in products:

		# type
		if 'red' in url:
			type = 'Red'
		if 'white' in url:
			type = 'White'
		if 'contact' in url:
			type = 'Orange'
		if 'rose' in url:
			type = 'Ros&#233;'
		if 'sparkling' in url:
			type = 'Sparkling'
		if 'fermented' in url:
			type = 'Co-Fermented'
		if 'piquette' in url:
			type = 'Piquette'
		type_class = type.replace("&#233;", "e").lower()

		# title
		title_name = product.find("h3", class_="product-block__title").text.strip()
		title_maker = product.find("div", class_="italicized-text").text.strip()
		title = title_maker + " " + title_name

		# get title string (used for parsing)
		title_string = title.replace(" ", "").lower()

		# price
		price = product.find("div", class_="product-block__price").text.strip()

		# link
		link = 'http://wineandeggs.com' + product.find("a")['href']

		# image
		imagesoup = product.find('noscript')
		imagecode = imagesoup.find("div", class_="product-block__image")['style']
		imageurl = imagecode.strip("background-image:url('").strip("');")
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
			'Image_type': image_type,
			'Type': type,
			'Type_class': type_class,
			'Store': 'Wine + Eggs',
			'Store_class': 'wineandeggs',
		})

random.shuffle(wines)

# Write JSON file
with open("data.json", "w") as writeJSON:
	json.dump({'wine': wines}, writeJSON, ensure_ascii=False)

# prints data to terminal (only needed for troubleshooting)
# print(json.dumps(wines, indent=4))
print('success!')
