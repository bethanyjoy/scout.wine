import re
import json
import requests
import random
from bs4 import BeautifulSoup
import requests
from mappings import type_mapping, region_mapping, maker_mapping
from fancyfree import ff_urls
from flaskandfield import faf_urls
from heavensmarket import hm_base_urls, hm_pages
from helens import helens_urls
from highlandpark import hlp_base_urls, hlp_pages
from kamp import kamp_urls
from silverlake import sl_base_urls, sl_pages
from sipsnack import ss_base_urls, ss_pages
from vinovore_eaglerock import vver_base_urls, vver_pages
from vinovore_silverlake import vvsl_base_urls, vvsl_pages


# Sets up empty list to store wine data
wines = []


# Global functions

def generate_urls(base_urls, pages):
    urls = []
    for base_url, num_pages in zip(base_urls, pages):
        for i in range(1, num_pages + 1):
            if i == 1:
                urls.append(base_url)
            else:
                urls.append(f"{base_url}?page={i}")
    return urls

def get_soup(url):
    return BeautifulSoup(requests.get(url).content, 'html.parser')

# Product
def get_products(url, tag, classname):
	return get_soup(url).find_all(tag, class_=classname)

# Title

def get_title_soup(product, tag, classname):
	return product.find(tag, class_=classname)

def get_title_string(title_soup):
	return title_soup.text.replace(" ", "").lower()

def get_title(title_soup):
	return title_soup.text.strip().lower()


# Link
def get_link(url):
	return url.split('.com')[0] + '.com' + product.find("a")['href']

# Maker
def lookup_maker(title_string):
	return next((k for k, v in maker_mapping.items() if isinstance(v, list) and any(item in title_string for item in v) or isinstance(v, str) and v in title_string), None)
def get_maker_class(title_string):
	return ''.join(e for e in lookup_maker(title_string) if e.isalpha()).lower() if lookup_maker(title_string) is not None else None

# Region
def lookup_region(url):
	return next((k for k, v in region_mapping.items() if (isinstance(v, list) and any(item in url.lower() for item in v)) or (isinstance(v, str) and v in url.lower())), None)

# Store
def get_store_class(store):
	return ''.join(e for e in store if e.isalpha()).lower()


# Price
def get_price(product, tag, classname):
	return product.find(tag, class_=classname).text.strip()


# Type

def lookup_type(url):
	return next((k for k, v in type_mapping.items() if (isinstance(v, list) and any(item in url.lower() for item in v)) or (isinstance(v, str) and v in url.lower())), None)

def get_type(title_string, url):
    if 'ferment' in title_string:
        return 'Co-Ferment'
    elif 'piquette' in title_string:
        return 'Piquette'
    else:
        return lookup_type(url)

def get_type_class(product_type):
	# return lookup_type(url).replace("&#233;", "e").lower()
	return product_type.replace("&#233;", "e").lower()


# Image

# img element in main code

def get_image(product):
	return product.find("img")

def get_image_src(product, classname=None):
    if classname:
        return product.find("img", class_=classname)['src']
    else:
        return product.find("img")['src']

# img element buried in no script

def get_noscript(product):
	return product.find('noscript')

def get_image_noscript(product):
	return product.find('noscript').find("img")

def get_image_src_noscript(product, classname=None):
    if classname:
        return product.find('noscript').find("img", class_=classname)['src']
    else:
        return product.find('noscript').find("img")['src']





# # TEMPLATE

# XX_urls = generate_urls(XX_base_urls, XX_pages)

# for url in XX_urls:

# 	# Define store
# 	store = 'XX'

# 	# Define how to target a product
# 	products = get_products(url, "div", "classname")

# 	for product in products:

# 		# Define how to target the title (don't need to format)
# 		title_soup = get_title_soup(product, "div", "classname")

# 		# Call up title string function to use for parsing (Don't need to edit)
# 		title_string = get_title_string(title_soup)

# 		# Call up product type (don't need to edit)
# 		product_type =  get_type(title_string, url)

# 		# Define how to target + format the price
# 		price = get_price(product, "div", "classname")

# 		# Define images
		# image_src = get_image_src_noscript(product, "classname")
# 		if 'no-image' in image_src:
# 			image_type = 'noimage'
# 		elif image_src is not None:
# 			image = 'https:' + image_src
# 			image_type = 'hasimage'
# 		else:
# 			image_type = 'noimage'
		
# 		### Don't need to edit code below this point ###

# 		# Add wine to list
# 		wines.append({
# 			'Image': image,
# 			'Image_type': image_type,
# 			'Link': get_link(url),
# 			'Maker': lookup_maker(title_string),
# 			'Maker_class': get_maker_class(title_string),
# 			'Price': price,
# 			'Region': lookup_region(url),
# 			'Store': store,
# 			'Store_class': get_store_class(store),
# 			'Title': get_title(title_soup),
# 			'Type': product_type,
#  			'Type_class': get_type_class(product_type)
# 		})




# Helen's Wine

for url in helens_urls:

	# Define store
	store = 'Helen&#39;s Wines'

	# Define how to target a product
	products = get_products(url, "div", "grid-product")

	for product in products:

		# Define how to target the title (don't need to format)
		title_soup = get_title_soup(product, "div", "grid-product__title--body")

		# Call up title string function to use for parsing (Don't need to edit)
		title_string = get_title_string(title_soup)

		# Call up product type (don't need to edit)
		product_type =  get_type(title_string, url)

		# Define how to target + format the price
		price = get_price(product, "div", "grid-product__price")

		# Define images
		image_src = get_image_src_noscript(product, "grid-product__image")
		if 'comingsoon' in image_src:
			image_type = 'noimage'
		elif image_src is not None:
			image = 'https:' + image_src
			image_type = 'hasimage'
		else:
			image_type = 'noimage'
		
		### Don't need to edit code below this point ###

		# Add wine to list
		wines.append({
			'Image': image,
			'Image_type': image_type,
			'Link': get_link(url),
			'Maker': lookup_maker(title_string),
			'Maker_class': get_maker_class(title_string),
			'Price': price,
			'Region': lookup_region(url),
			'Store': store,
			'Store_class': get_store_class(store),
			'Title': get_title(title_soup),
			'Type': product_type,
  		'Type_class': get_type_class(product_type)
		})





# Heaven's Market

hm_urls = generate_urls(hm_base_urls, hm_pages)

for url in hm_urls:

	# Define store
	store = 'Heaven&#39;s Market'

	# Define how to target a product
	products = get_products(url, "li", "grid__item")

	for product in products:

		# Define how to target the title (don't need to format)
		title_soup = get_title_soup(product, "span", "visually-hidden")

		# Call up title string function to use for parsing (Don't need to edit)
		title_string = get_title_string(title_soup)

		# Call up product type (don't need to edit)
		product_type =  get_type(title_string, url)

		# Ignore non-wine items
		if 'wineclass' in title_string:
			print()

		# Parse wine items
		else:

			# Define how to target + format the price
			price = get_price(product, "span", "price-item")

			# Define images
			image_src = get_image_src_noscript(product, "grid-view-item__image")
			if 'no-image' in image_src:
				image_type = 'noimage'
			elif image_src is not None:
				image = 'https:' + image_src
				image_type = 'hasimage'
			else:
				image_type = 'noimage'
			
			### Don't need to edit code below this point ###

			# Add wine to list
			wines.append({
				'Image': image,
				'Image_type': image_type,
				'Link': get_link(url),
				'Maker': lookup_maker(title_string),
				'Maker_class': get_maker_class(title_string),
				'Price': price,
				'Region': lookup_region(url),
				'Store': store,
				'Store_class': get_store_class(store),
				'Title': get_title(title_soup),
				'Type': product_type,
		   		'Type_class': get_type_class(product_type)
			})




# Silverlake Wine

sl_urls = generate_urls(sl_base_urls, sl_pages)

for url in sl_urls:

	# Define store
	store = 'Silverlake Wine'

	# Define how to target a product
	products = get_products(url, "div", "prod-block")

	for product in products:

		# Define how to target the title (don't need to format)
		title_soup = get_title_soup(product, "div", "title")

		# Call up title string function to use for parsing (Don't need to edit)
		title_string = get_title_string(title_soup)

		# Call up product type (don't need to edit)
		product_type =  get_type(title_string, url)

		# Define how to target + format the price
		price = get_price(product, "div", "product-price")

		# Define images
		image_src = get_image_src_noscript(product, "rimage__image")
		if 'no-image' in image_src:
			image_type = 'noimage'
		elif image_src is not None:
			image = 'https:' + image_src
			image_type = 'hasimage'
		else:
			image_type = 'noimage'
		
		### Don't need to edit code below this point ###

		# Add wine to list
		wines.append({
			'Image': image,
			'Image_type': image_type,
			'Link': get_link(url),
			'Maker': lookup_maker(title_string),
			'Maker_class': get_maker_class(title_string),
			'Price': price,
			'Region': lookup_region(url),
			'Store': store,
			'Store_class': get_store_class(store),
			'Title': get_title(title_soup),
			'Type': product_type,
			'Type_class': get_type_class(product_type)
		})



# Highland Park Wine

hlp_urls = generate_urls(hlp_base_urls, hlp_pages)

for url in hlp_urls:

	# Define store
	store = 'Highland Park Wine'

	# Define how to target a product
	products = get_products(url, "div", "prod-block")

	for product in products:

		# Define how to target the title (don't need to format)
		title_soup = get_title_soup(product, "div", "title")

		# Call up title string function to use for parsing (Don't need to edit)
		title_string = get_title_string(title_soup)

		# Call up product type (don't need to edit)
		product_type =  get_type(title_string, url)

		# Define how to target + format the price
		price = get_price(product, "div", "product-price")

		# Define images
		image_src = get_image_src_noscript(product, "rimage__image")
		if 'no-image' in image_src:
			image_type = 'noimage'
		elif image_src is not None:
			image = 'https:' + image_src
			image_type = 'hasimage'
		else:
			image_type = 'noimage'
		
		### Don't need to edit code below this point ###

		# Add wine to list
		wines.append({
			'Image': image,
			'Image_type': image_type,
			'Link': get_link(url),
			'Maker': lookup_maker(title_string),
			'Maker_class': get_maker_class(title_string),
			'Price': price,
			'Region': lookup_region(url),
			'Store': store,
			'Store_class': get_store_class(store),
			'Title': get_title(title_soup),
			'Type': product_type,
			'Type_class': get_type_class(product_type)
		})




# Fancy Free

for url in ff_urls:

	# Define store
	store = 'Fancy Free'

	# Define how to target a product
	products = get_products(url, "div", "grid-item")

	for product in products:

		# Define how to target the title (don't need to format)
		title_soup = get_title_soup(product, "div", "grid-title")

		# Call up title string function to use for parsing (Don't need to edit)
		title_string = get_title_string(title_soup)

		# Call up product type (don't need to edit)
		product_type =  get_type(title_string, url)

		# Define how to target + format the price
		price = get_price(product, "div", "product-price")

		# Define images
		image_src = product.find("img")['data-src']
		if 'Temporary' in image_src:
			image_type = 'noimage'
		elif image_src is not None:
			image = image_src
			image_type = 'hasimage'
		else:
			image_type = 'noimage'
		
		### Don't need to edit code below this point ###

		# Add wine to list
		wines.append({
			'Image': image,
			'Image_type': image_type,
			'Link': get_link(url),
			'Maker': lookup_maker(title_string),
			'Maker_class': get_maker_class(title_string),
			'Price': price,
			'Region': lookup_region(url),
			'Store': store,
			'Store_class': get_store_class(store),
			'Title': get_title(title_soup),
			'Type': product_type,
			'Type_class': get_type_class(product_type)
		})



# Vinovore Eagle Rock

vver_urls = generate_urls(vver_base_urls, vver_pages)

for url in vver_urls:

	# Define store
	store = 'Vinovore Eagle Rock'

	# Define how to target a product
	products = get_products(url, "div", "grid-product")

	for product in products:

		# Define how to target the title (don't need to format)
		title_soup = get_title_soup(product, "div", "grid-product__title")

		# Call up title string function to use for parsing (Don't need to edit)
		title_string = get_title_string(title_soup)

		# Call up product type (don't need to edit)
		product_type =  get_type(title_string, url)

		# Ignore non-wine items
		if 'giftbox' in title_string:
			print()
		elif 'bouquet' in title_string:
			print()
		elif 'stopper' in title_string:
			print()
		elif 'tasting' in title_string:
			print()

		# Parse wine items
		else:

			# Define how to target + format the price
			pricesoup = product.find("div", class_="grid-product__price")
			if pricesoup.span:
				price = 'On Sale'
			else:
				price = pricesoup.text.strip()

			# Define images
			image_src = get_image_src_noscript(product, "grid-product__image")
			if 'no-image' in image_src:
				image_type = 'noimage'
			elif image_src is not None:
				image = 'https:' + image_src
				image_type = 'hasimage'
			else:
				image_type = 'noimage'
			
			### Don't need to edit code below this point ###

			# Add wine to list
			wines.append({
				'Image': image,
				'Image_type': image_type,
				'Link': get_link(url),
				'Maker': lookup_maker(title_string),
				'Maker_class': get_maker_class(title_string),
				'Price': price,
				'Region': lookup_region(url),
				'Store': store,
				'Store_class': get_store_class(store),
				'Title': get_title(title_soup),
				'Type': product_type,
				'Type_class': get_type_class(product_type)
			})




# Vinovore Silverlake

vvsl_urls = generate_urls(vvsl_base_urls, vvsl_pages)

for url in vvsl_urls:

	# Define store
	store = 'Vinovore Silverlake'

	# Define how to target a product
	products = get_products(url, "div", "product")

	for product in products:

		# Define how to target the title (don't need to format)
		title_soup = get_title_soup(product, "h3", "product__title")

		# Call up title string function to use for parsing
		title_string = get_title_string(title_soup)

		# Call up product type (don't need to edit)
		product_type =  get_type(title_string, url)

		# Ignore non-wine items
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

		# Parse wine items
		else:

			# Check if sold out
			stock = get_price(product, "p", "product__price")

			# Define how to target + format the price
			if stock !='Sold Out':
				price = get_price(product, "span", "money")
			else:
				price = 'null'

			# Define images
			image_src = get_image_src_noscript(product, "product__img")
			if 'no-image' in image_src:
				image_type = 'noimage'
			elif image_src is not None:
				image = 'https:' + image_src
				image_type = 'hasimage'
			else:
				image_type = 'noimage'
			
			### Don't need to edit code below this point ###

			# Add wine to list
			wines.append({
				'Image': image,
				'Image_type': image_type,
				'Link': get_link(url),
				'Maker': lookup_maker(title_string),
				'Maker_class': get_maker_class(title_string),
				'Price': price,
				'Region': lookup_region(url),
				'Store': store,
				'Store_class': get_store_class(store),
				'Title': get_title(title_soup),
				'Type': product_type,
				'Type_class': get_type_class(product_type)
			})





# Flask & Field

for url in faf_urls:

	# Define store
	store = 'Flask + Field'

	# Define how to target a product
	products = get_products(url, "li", "grid__item")

	for product in products:

		# Define how to target the title (don't need to format)
		title_soup = get_title_soup(product, "h3", "card__heading")

		# Call up title string function to use for parsing
		title_string = get_title_string(title_soup)

		# Call up product type (don't need to edit)
		product_type =  get_type(title_string, url)

		# Define how to locate non-wine products
		badge_check = product.find("div", class_="card__badge").find("img")

		# Ignore non-wine prouducts
		if 'selects' in title_string:
			print()
		if badge_check:
			print()

		# Continue parsing wine products
		else:

			# Define how to target the price
			price_soup = get_price(product, "span", "price-item")

			# Define how to format the price
			if '.' in price_soup:
				price = price_soup
			else:
				price = price_soup + '.00'

			# Define images
			image_src = get_image_src(product)
			if 'placeholder' in image_src:
				image_type = 'noimage'
			elif image_src is not None:
				image = 'https:' + image_src
				image_type = 'hasimage'
			else:
				image_type = 'noimage'
			
			### Don't need to edit code below this point ###

			# Add wine to list
			wines.append({
				'Image': image,
				'Image_type': image_type,
				'Link': get_link(url),
				'Maker': lookup_maker(title_string),
				'Maker_class': get_maker_class(title_string),
				'Price': price,
				'Region': lookup_region(url),
				'Store': store,
				'Store_class': get_store_class(store),
				'Title': get_title(title_soup),
				'Type': product_type,
				'Type_class': get_type_class(product_type)
			})


# Sip Snack

ss_urls = generate_urls(ss_base_urls, ss_pages)

for url in ss_urls:

	# Define store
	store = 'Sip Snack'

	# Define how to target a product
	products = get_products(url, "div", "product--root")

	for product in products:

		# Define how to target the title (don't need to format)
		title_soup = get_title_soup(product, "h3", "product--title")

		# Call up title string function to use for parsing
		title_string = get_title_string(title_soup)

		# Call up product type (don't need to edit)
		product_type =  get_type(title_string, url.split("/")[-1])

		# Define how to target + format the price
		price = get_price(product, "span", "product--price")

		# Define images
		image_src = get_image_src_noscript(product)
		if 'no-image' in image_src:
			image_type = 'noimage'
		elif image_src is not None:
			image = 'https:' + image_src
			image_type = 'hasimage'
		else:
			image_type = 'noimage'
		
		### Don't need to edit code below this point ###

		# Add wine to list
		wines.append({
			'Image': image,
			'Image_type': image_type,
			'Link': get_link(url),
			'Maker': lookup_maker(title_string),
			'Maker_class': get_maker_class(title_string),
			'Price': price,
			'Region': lookup_region(url),
			'Store': store,
			'Store_class': get_store_class(store),
			'Title': get_title(title_soup),
			'Type': product_type,
			'Type_class': get_type_class(product_type)
		})


# Kamp

for url in kamp_urls:

	# Define store
	store = 'Kamp'

	# Define how to target a product
	products = get_products(url, "div", "product--root")

	for product in products:

		# Define how to target the title (don't need to format)
		title_name = product.find("p", class_="product--title").text.strip().lower()
		title_maker = product.find("div", class_="product--vendor").text.strip().lower()
		title = title_maker + " " + title_name

		# Call up product type (don't need to edit)
		product_type =  get_type(title_name, url)

		# Define how to target + format the price
		price = get_price(product, "span", "product--price money")

		# Define images
		image_check = get_image_noscript(product)
		if image_check is not None:
			image_src = get_image_src_noscript(product)
			image = 'https:' + image_src
			image_type = 'hasimage'
		else:
			image_type = 'noimage'
		
		### Don't need to edit code below this point ###

		# Add wine to list
		wines.append({
			'Image': image,
			'Image_type': image_type,
			'Link': get_link(url),
			'Maker': lookup_maker(title_maker.replace(" ", "")),
			'Maker_class': get_maker_class(title_maker.replace(" ", "")),
			'Price': price,
			'Region': lookup_region(url),
			'Store': store,
			'Store_class': get_store_class(store),
			'Title': title,
			'Type': product_type,
 			'Type_class': get_type_class(product_type)
		})


# Shuffle wine list
random.shuffle(wines)

# Write JSON file
with open("data.json", "w") as writeJSON:
	json.dump({'wine': wines}, writeJSON, ensure_ascii=False)

# Print in terminal (only needed for troubleshooting)    
print(json.dumps(wines, indent=4))
print('success!')