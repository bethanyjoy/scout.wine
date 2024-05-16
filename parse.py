import re
import json
import requests
import random
from bs4 import BeautifulSoup
import requests
from mappings import type_mapping, region_mapping, maker_mapping, origin_mapping
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


# Generate urls with pagination

def generate_urls(base_urls, pages):
    urls = []
    for base_url, num_pages in zip(base_urls, pages):
        for i in range(1, num_pages + 1):
            if i == 1:
                urls.append(base_url)
            else:
                urls.append(f"{base_url}?page={i}")
    return urls

# Get soup
def get_soup(url):
    return BeautifulSoup(requests.get(url).content, 'html.parser')

# Product
def get_products(url, tag, classname):
    return get_soup(url).find_all(tag, class_=classname)

# Link
def get_link(url):
    return url.split('.com')[0] + '.com' + product.find("a")['href']

# Maker
def lookup_maker(title_string):
    return next((k for k, v in maker_mapping.items() if isinstance(v, list) and any(item in title_string for item in v) or isinstance(v, str) and v in title_string), None)
def get_maker_class(title_string):
    return ''.join(e for e in maker if e.isalpha()).lower() if maker is not None else None

# Region
def lookup_region_url(url):
    return next((k for k, v in region_mapping.items() if (isinstance(v, list) and any(item in url.lower() for item in v)) or (isinstance(v, str) and v in url.lower())), None)

def lookup_region_maker(maker):
    return origin_mapping.get(maker)

def lookup_region(maker, url):
    if maker is not None:
        return lookup_region_maker(maker)
    else:
        return lookup_region_url(url)

# Store
def get_store_class(store):
    return ''.join(e for e in store if e.isalpha()).lower()

# Price
def get_price(product, tag, classname):
    price = product.find(tag, class_=classname).text.strip()
    if '.' not in price:
        price += ".00"
    return price

# Doesn't fail if price is missing (below)
# def get_price(product, tag, classname):
#     element = product.find(tag, class_=classname)
#     if element is not None:
#         price = element.text.strip()
#         if '.' not in price:
#             price += ".00"
#         return price
#     else:
#         return None

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

# Title

# Name + maker combines

def get_title_soup(product, tag, classname):
    return product.find(tag, class_=classname)

# Name separate

def get_name_soup(product, tag, classname):
    return product.find(tag, class_=classname)

def get_name_string(name_soup):
    return name_soup.text.replace(" ", "").lower()

def get_name(name_soup):
    return name_soup.text.strip().lower()

# Maker seprate

def get_maker_soup(product, tag, classname):
    return product.find(tag, class_=classname)

def get_maker_string(maker_soup):
    return maker_soup.text.replace(" ", "").lower()

def get_maker(maker_soup):
    return maker_soup.text.strip().lower()

# Get title

def get_title_string(input1, input2=None):
    if input2 is None:
        # Assume input1 is title_soup
        return input1.text.replace(" ", "").lower()
    else:
        # Assume input1 is maker_string and input2 is name_string
        return input1 + input2

def get_title(input1, input2=None):
    if input2 is None:
        # Assume input1 is title_soup
        return input1.text.strip().lower()
    else:
        # Assume input1 is maker and input2 is name
        return input1 + " " + input2

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

# Process image

def process_image_src(image_src):
    if any(keyword in image_src for keyword in ['Temporary', 'no-image', 'placeholder', 'comingsoon']):
        image_type = 'noimage'
        image = None
    elif image_src is not None:
        image = image_src if 'https:' in image_src else 'https:' + image_src
        image_type = 'hasimage'
    else:
        image_type = 'noimage'
        image = None

    return image, image_type




# Process Items

# List of non-wine items to exclude

non_wine_items = ['wineclass', 'giftbox', 'giftbag', 'bouquet', 'stopper', 'tasting', 'alcoholic', 'cider', 'aperitif', 'sake', 'takju', 'selects', 'speitz']

# Default way to process items with a combined title

# def process_item(title_string, url, image, image_type, price, store, product_type, title_soup):
#     if any(item in title_string for item in non_wine_items):
#         return None

#     return {
#         'Image': image,
#         'Image_type': image_type,
#         'Link': get_link(url),
#         'Maker': lookup_maker(title_string),
#         'Maker_class': get_maker_class(title_string),
#         'Price': price,
#         'Region': lookup_region(url),
#         'Store': store,
#         'Store_class': get_store_class(store),
#         'Title': get_title(title_soup),
#         'Type': product_type,
#         'Type_class': get_type_class(product_type)
#     }

# Default way to process items with a combined title

def process_item(title_string, image, image_type, url, maker, price, region, store, title, product_type):
    if any(item in title_string for item in non_wine_items):
        return None

    return {
        'Image': image,
        'Image_type': image_type,
        'Link': get_link(url),
        'Maker': maker,
        'Maker_class': get_maker_class(maker),
        'Price': price,
        'Region': region,
        'Store': store,
        'Store_class': get_store_class(store),
        'Title': title,
        'Type': product_type,
        'Type_class': get_type_class(product_type)
    }



# # TEMPLATE

# # Only need to edit orange text and XX instances

# # Generate urls (delete if not needed)
# XX_urls = generate_urls(XX_base_urls, XX_pages)

# for url in XX_urls:

#     # Define store
#     store = 'XX'

#     # Define how to target a product
#     products = get_products(url, "tag", "classname")

#     for product in products:

#         # Define how to target the title (if name + maker separate - use other template)
#         title_soup = get_title_soup(product, "tag", "classname")

#         # Define how to target the price
#         price = get_price(product, "tag", "classname")

#         # Define images (pick one that applies)
#         # -- Img element in main code
#         image_src = get_image_src(product, "classname")
#         # -- Img element in noscript
#         image_src = get_image_src_noscript(product, "classname")

#         # --- Don't need to edit anything below this point --- #

#         # Call up title string to use for parsing
#         title_string = get_title_string(title_soup)

#         # Call up product type
#         product_type =  get_type(title_string, url)

#         # Process the image source
#         image, image_type = process_image_src(image_src)

#         # Call up maker
#         maker = lookup_maker(title_string)

#         # Call up region
#         region = lookup_region(maker, url)

#         # Call up title
#         title = get_title(title_soup)
        
#         # Check if it's a wine item, if so add to wine list
#         wine = process_item(title_string, image, image_type, url, maker, price, region, store, title, product_type)
#         if wine is not None:
#             wines.append(wine)




# # TEMPLATE - Maker and name separate (more accurate)

# # Only need to edit orange text and XX instances

# # Generate urls (delete if not needed)
# XX_urls = generate_urls(XX_base_urls, XX_pages)

# for url in XX_urls:

#     # Define store
#     store = 'XX'

#     # Define how to target a product
#     products = get_products(url, "tag", "classname")

#     for product in products:

#         # Define how to target the name
#         name_soup = get_name_soup(product, "tag", "classname")

#         # Define how to target the maker
#         maker_soup = get_maker_soup(product, "tag", "classname")

#         # Define how to target the price
#         price = get_price(product, "tag", "classname")

#         # Define images (pick one that applies)
#         # -- Img element in main code
#         image_src = get_image_src(product, "classname")
#         # -- Img element in noscript
#         image_src = get_image_src_noscript(product, "classname")

#         # --- Don't need to edit anything below this point --- #

#         # Call up name and maker strings + text
#         name_string = get_name_string(name_soup)
#         name_text = get_name(name_soup)
#         maker_string = get_maker_string(maker_soup)
#         maker_text = get_maker(maker_soup)

#         # Call up product type (don't need to edit)
#         product_type =  get_type(name_string, url)

#         # Process the image source
#         image, image_type = process_image_src(image_src)

#         # Call up title string
#         title_string = get_title_string(maker_string, name_string)

#         # Call up maker
#         maker = lookup_maker(maker_string)

#         # Call up region
#         region = lookup_region(maker, url)

#         # Call up title
#         title = get_title(name_text, maker_text)
        
#         # Check if it's a wine item, if so add to wine list
#         wine = process_item(title_string, image, image_type, url, maker, price, region, store, title, product_type)
#         if wine is not None:
#             wines.append(wine)





# Fancy Free

for url in ff_urls:

    # Define store
    store = 'Fancy Free'

    # Define how to target a product
    products = get_products(url, "div", "grid-item")

    for product in products:

        # Define how to target the title
        title_soup = get_title_soup(product, "div", "grid-title")

        # Define how to target the price
        price = get_price(product, "div", "product-price")

        # Define images
        image_src = product.find("img")['data-src']

        # --- Don't need to edit anything below this point --- #

        # Call up title string to use for parsing
        title_string = get_title_string(title_soup)

        # Call up product type
        product_type =  get_type(title_string, url)

        # Process the image source
        image, image_type = process_image_src(image_src)
        
        # Call up maker
        maker = lookup_maker(title_string)

        # Call up region
        region = lookup_region(maker, url)

        # Call up title
        title = get_title(title_soup)
        
        # Check if it's a wine item, if so add to wine list
        wine = process_item(title_string, image, image_type, url, maker, price, region, store, title, product_type)
        if wine is not None:
            wines.append(wine)



# Flask & Field

for url in faf_urls:

    # Define store
    store = 'Flask + Field'

    # Define how to target a product
    products = get_products(url, "li", "grid__item")

    for product in products:

        # Define how to target the title (don't need to format)
        title_soup = get_title_soup(product, "h3", "card__heading")

        # Define how to target the price
        price = get_price(product, "span", "price-item")

        # Define images
        image_src = get_image_src(product)

        # Define how to locate non-wine products
        item_check = product.find("div", class_="card__badge").find("img")

        # --- Don't need to edit anything below this point --- #

        # Call up title string to use for parsing
        title_string = get_title_string(title_soup)

        # Call up product type
        product_type =  get_type(title_string, url)

        # Process the image source
        image, image_type = process_image_src(image_src)
        
        # Call up maker
        maker = lookup_maker(title_string)

        # Call up region
        region = lookup_region(maker, url)

        # Call up title
        title = get_title(title_soup)

        # Ignore non-wine prouducts
        if item_check:
            continue

        # Continue parsing wine products
        else:
        
            # Check if it's a wine item, if so add to wine list
            wine = process_item(title_string, image, image_type, url, maker, price, region, store, title, product_type)
            if wine is not None:
                wines.append(wine)




# Heaven's Market

hm_urls = generate_urls(hm_base_urls, hm_pages)

for url in hm_urls:

    # Define store
    store = 'Heaven&#39;s Market'

    # Define how to target a product
    products = get_products(url, "li", "grid__item")

    for product in products:

        # Define how to target the title
        title_soup = get_title_soup(product, "span", "visually-hidden")

        # Define how to target
        price = get_price(product, "span", "price-item")

        # Define images
        image_src = get_image_src_noscript(product, "grid-view-item__image")

        # --- Don't need to edit anything below this point --- #

        # Call up title string to use for parsing
        title_string = get_title_string(title_soup)

        # Call up product type
        product_type =  get_type(title_string, url)

        # Process the image source
        image, image_type = process_image_src(image_src)
        
        # Call up maker
        maker = lookup_maker(title_string)

        # Call up region
        region = lookup_region(maker, url)

        # Call up title
        title = get_title(title_soup)
        
        # Check if it's a wine item, if so add to wine list
        wine = process_item(title_string, image, image_type, url, maker, price, region, store, title, product_type)
        if wine is not None:
            wines.append(wine)




# Helen's Wine

for url in helens_urls:

    # Define store
    store = 'Helen&#39;s Wines'

    # Define how to target a product
    products = get_products(url, "div", "grid-product")

    for product in products:

        # Define how to target the title
        title_soup = get_title_soup(product, "div", "grid-product__title--body")

        # Define how to target
        price = get_price(product, "div", "grid-product__price")

        # Define images
        image_src = get_image_src_noscript(product, "grid-product__image")

        # --- Don't need to edit anything below this point --- #

        # Call up title string to use for parsing
        title_string = get_title_string(title_soup)

        # Call up product type
        product_type =  get_type(title_string, url)

        # Process the image source
        image, image_type = process_image_src(image_src)
        
        # Call up maker
        maker = lookup_maker(title_string)

        # Call up region
        region = lookup_region(maker, url)

        # Call up title
        title = get_title(title_soup)
        
        # Check if it's a wine item, if so add to wine list
        wine = process_item(title_string, image, image_type, url, maker, price, region, store, title, product_type)
        if wine is not None:
            wines.append(wine)




# Highland Park Wine

hlp_urls = generate_urls(hlp_base_urls, hlp_pages)

for url in hlp_urls:

    # Define store
    store = 'Highland Park Wine'

    # Define how to target a product
    products = get_products(url, "div", "prod-block")

    for product in products:

        # Define how to target the title
        title_soup = get_title_soup(product, "div", "title")

        # Define how to target the price
        price = get_price(product, "div", "product-price")

        # Define images
        image_src = get_image_src_noscript(product, "rimage__image")

        # --- Don't need to edit anything below this point --- #

        # Call up title string to use for parsing
        title_string = get_title_string(title_soup)

        # Call up product type
        product_type =  get_type(title_string, url)

        # Process the image source
        image, image_type = process_image_src(image_src)
        
        # Call up maker
        maker = lookup_maker(title_string)

        # Call up region
        region = lookup_region(maker, url)

        # Call up title
        title = get_title(title_soup)
        
        # Check if it's a wine item, if so add to wine list
        wine = process_item(title_string, image, image_type, url, maker, price, region, store, title, product_type)
        if wine is not None:
            wines.append(wine)




# Kamp

for url in kamp_urls:

    # Define store
    store = 'Kamp'

    # Define how to target a product
    products = get_products(url, "div", "product--root")

    for product in products:

        # Define how to target the name
        name_soup = get_name_soup(product, "p", "product--title")

        # Define how to target the maker
        maker_soup = get_maker_soup(product, "div", "product--vendor")

        # Define how to target the price
        price = get_price(product, "span", "product--price money")

        # Define images
        image_src = get_image_src_noscript(product)

        # --- Don't need to edit anything below this point --- #

        # Call up name and maker strings + text
        name_string = get_name_string(name_soup)
        name_text = get_name(name_soup)
        maker_string = get_maker_string(maker_soup)
        maker_text = get_maker(maker_soup)

        # Call up product type (don't need to edit)
        product_type =  get_type(name_string, url)

        # Process the image source
        image, image_type = process_image_src(image_src)

        # Call up title string
        title_string = get_title_string(maker_string, name_string)

        # Call up maker
        maker = lookup_maker(maker_string)

        # Call up region
        region = lookup_region(maker, url)

        # Call up title
        title = get_title(name_text, maker_text)
        
        # Check if it's a wine item, if so add to wine list
        wine = process_item(title_string, image, image_type, url, maker, price, region, store, title, product_type)
        if wine is not None:
            wines.append(wine)





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

        # Define how to target + format the price
        price = get_price(product, "div", "product-price")

        # Define images
        image_src = get_image_src_noscript(product, "rimage__image")

        # --- Don't need to edit anything below this point --- #

        # Call up title string function to use for parsing (Don't need to edit)
        title_string = get_title_string(title_soup)

        # Call up product type (don't need to edit)
        product_type =  get_type(title_string, url)

        # Process the image source
        image, image_type = process_image_src(image_src)
        
        # Call up maker
        maker = lookup_maker(title_string)

        # Call up region
        region = lookup_region(maker, url)

        # Call up title
        title = get_title(title_soup)
        
        # Check if it's a wine item, if so add to wine list
        wine = process_item(title_string, image, image_type, url, maker, price, region, store, title, product_type)
        if wine is not None:
            wines.append(wine)



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

        # Define how to target + format the price
        price = get_price(product, "span", "product--price")

        # Define images
        image_src = get_image_src_noscript(product)

        # --- Don't need to edit anything below this point --- #

        # Call up title string function to use for parsing
        title_string = get_title_string(title_soup)

        # Call up product type (don't need to edit)
        product_type =  get_type(title_string, url.split("/")[-1])

        # Process the image source
        image, image_type = process_image_src(image_src)
        
        # Call up maker
        maker = lookup_maker(title_string)

        # Call up region
        region = lookup_region(maker, url)

        # Call up title
        title = get_title(title_soup)
        
        # Check if it's a wine item, if so add to wine list
        wine = process_item(title_string, image, image_type, url, maker, price, region, store, title, product_type)
        if wine is not None:
            wines.append(wine)




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
        
        # Define how to target + format the price
        pricesoup = product.find("div", class_="grid-product__price")
        if pricesoup.span:
            price = 'On Sale'
        else:
            price = pricesoup.text.strip()

        # Define images
        image_src = get_image_src_noscript(product, "grid-product__image")

        # --- Don't need to edit anything below this point --- #

        # Call up title string function to use for parsing (Don't need to edit)
        title_string = get_title_string(title_soup)

        # Call up product type (don't need to edit)
        product_type =  get_type(title_string, url)

        # Process the image source
        image, image_type = process_image_src(image_src)
        
        # Call up maker
        maker = lookup_maker(title_string)

        # Call up region
        region = lookup_region(maker, url)

        # Call up title
        title = get_title(title_soup)
        
        # Check if it's a wine item, if so add to wine list
        wine = process_item(title_string, image, image_type, url, maker, price, region, store, title, product_type)
        if wine is not None:
            wines.append(wine)




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
        
        # Check if sold out
        stock = product.find("p", class_="product__price").text.strip()

        # Define how to target + format the price
        if stock !='Sold Out':
            price = get_price(product, "span", "money")
        else:
            price = 'null'

        # Define images
        image_src = get_image_src_noscript(product, "product__img")

        # --- Don't need to edit anything below this point --- #

        # Call up title string function to use for parsing
        title_string = get_title_string(title_soup)

        # Call up product type (don't need to edit)
        product_type =  get_type(title_string, url)

        # Process the image source
        image, image_type = process_image_src(image_src)
        
        # Call up maker
        maker = lookup_maker(title_string)

        # Call up region
        region = lookup_region(maker, url)

        # Call up title
        title = get_title(title_soup)
        
        # Check if it's a wine item, if so add to wine list
        wine = process_item(title_string, image, image_type, url, maker, price, region, store, title, product_type)
        if wine is not None:
            wines.append(wine)





# Shuffle wine list
random.shuffle(wines)

# Write JSON file
with open("data.json", "w") as writeJSON:
	json.dump({'wine': wines}, writeJSON, ensure_ascii=False)

# Print in terminal (only needed for troubleshooting)    
# print(json.dumps(wines, indent=4))
print('success!')