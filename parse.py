import re
import json
import requests
import random
from bs4 import BeautifulSoup
import requests
import unicodedata
from mappings import type_mapping, region_mapping, maker_mapping, origin_mapping, general_region_mapping
from fancyfree import fancyfree_urls
from flaskandfield import flaskandfield_urls
from heavensmarket import heavensmarket_urls
from highlandpark import highlandpark_urls
from kamp import kamp_urls
from silverlake import silverlake_urls
from sipsnack import sipsnack_urls
from vinovore_eaglerock import vinovore_eaglerock_urls
from vinovore_silverlake import vinovore_silverlake_urls

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
def get_products(url, tag, classname=None):
    return get_soup(url).find_all(tag, class_=classname)

# Link
def get_link(url):
    return url.split('.com')[0] + '.com' + product.find("a")['href']

# Maker
def lookup_maker(title_string):
    return next((k for k, v in maker_mapping.items() if isinstance(v, list) and any(item in title_string for item in v) or isinstance(v, str) and v in title_string), None)

# Region

# Check if the URL contains a region keyword
def lookup_region_url(url):
    return next((k for k, v in region_mapping.items() if (isinstance(v, list) and any(item in url.lower() for item in v)) or (isinstance(v, str) and v in url.lower())), None)

# Check if the title contains a region keyword
def lookup_general_region(title_string):
    return next((k for k, v in general_region_mapping.items() if isinstance(v, list) and any(item in title_string for item in v) or isinstance(v, str) and v in title_string), None)

# Get the region based on the maker
def lookup_region_maker(maker):
    return origin_mapping.get(maker)
    
def lookup_region(maker, url, title_string):
    if maker is not None:
        return lookup_region_maker(maker)
    else:
        region = lookup_region_url(url)
        if region is None:
            return lookup_general_region(title_string)
        else:
            return region

# Price
def get_price(product, tag, classname):
    price = product.find(tag, class_=classname).text.strip()
    if '.' not in price:
        price += ".00"
    return price

# Type

def lookup_type(url):
    return next((k for k, v in type_mapping.items() if (isinstance(v, list) and any(item in url.lower() for item in v)) or (isinstance(v, str) and v in url.lower())), None)

# def get_type(title_string, url):
#     if 'co-ferment' in title_string:
#         return 'Co-Ferment'
#     if 'coferment' in title_string:
#         return 'Co-Ferment'
#     elif 'piquette' in title_string:
#         return 'Piquette'
#     else:
#         return lookup_type(url)
    
def get_type(title_string, url):
    return lookup_type(url)
    
    

# Title

# Name + maker combines

def get_title_soup(product, tag, classname=None):
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

def get_noscript(product):
    return product.find('noscript')

def get_image_noscript(product):
    return product.find('noscript').find("img")

def get_image_src_noscript(product, classname=None):
    if classname:
        return product.find('noscript').find("img", class_=classname)['src']
    else:
        return product.find('noscript').find("img")['src']

# New get image code

def get_image_src(product, datatype, classname=None):
    if product.find('noscript') is None:
        if classname:
            return product.find("img", class_=classname)[datatype]
        else:
            return product.find("img")[datatype]
    else:
        if classname:
            return product.find('noscript').find("img", class_=classname)[datatype]
        else:
            return product.find('noscript').find("img")[datatype]
        

def get_image_src_alt(product, datatype, classname=None):
    noscript = product.find('noscript')
    if noscript is not None:
        img = noscript.find("img", class_=classname) if classname else noscript.find("img")
        if img is not None:
            return img.get(datatype)
    if noscript is None:
        img = product.find("img", class_=classname)
        if img is not None:
            return img.get(datatype)
        

        
    # if product.find('noscript') is None:
    #     if classname:
    #         return product.find("img", class_=classname)[datatype]
    #     else:
    #         return product.find("img")[datatype]
    # else:
    #     if classname:
    #         return product.find('noscript').find("img", class_=classname)[datatype]
    #     else:
        

# def get_image_src(product, datatype, classname=None):
#     noscript = product.find('noscript')
#     if noscript is not None:
#         img = noscript.find("img", class_=classname) if classname else noscript.find("img")
#         if img is not None:
#             return img.get(datatype)
#     return None
        
# NEW NEW image function

def get_image_src_parentdiv(product, classname=None):
    image_div = product.find("div", class_=classname)
    if image_div is not None:
        image = image_div.find("img")
        if image is not None:
            return image.get("src")
    return None

# Process image

# Default method (faster, more efficient)
def process_image_src(image_src):
    if image_src is None:
        return None, 'noimage'
    if any(keyword in image_src for keyword in ['Temporary', 'no-image', 'placeholder', 'comingsoon']):
        return None, 'noimage'
    else:
        image = image_src if 'https:' in image_src else 'https:' + image_src
        return image, 'hasimage'

# Load check method (slower but good for site with bad image links)
def process_image_src_loadcheck(image_src):
    if image_src is None:
        return None, 'noimage'
    if any(keyword in image_src for keyword in ['Temporary', 'no-image', 'placeholder', 'comingsoon']):
        return None, 'noimage'
    else:
        image = image_src if 'https:' in image_src else 'https:' + image_src
        try:
            response = requests.get(image, stream=True)
            if response.status_code == 200:
                return image, 'hasimage'
            else:
                return None, 'noimage'
        except requests.exceptions.RequestException:
            return None, 'noimage'

# Format class

def get_class(input):
    if input is None:
        return None
    input = unicodedata.normalize('NFD', input).encode('ascii', 'ignore').decode("utf-8")
    return ''.join(e for e in input if e.isalpha()).lower()

# Process Items

# List of non-wine items to exclude

non_wine_items = ['alcoholic', 'aperitif', 'bouquet', 'cider', 'giftbag', 'giftbox', 'giftcard', 'sake', 'selects', 'speitz', 'stopper', 'takju', 'tasting', 'vermouth', 'wineclass']

# Process Items

def process_item(title_string, image, image_type, url, maker, price, region, store, title, product_type):
    if any(item in title_string for item in non_wine_items):
        return None

    return {
        'Image': image,
        'Image_type': image_type,
        'Link': get_link(url),
        'Maker': maker,
        'Maker_class': get_class(maker),
        'Price': price,
        'Region': region,
        'Store': store,
        'Store_class': get_class(store),
        'Title': title,
        'Type': product_type,
        'Type_class': get_class(product_type)
    }


# # TEMPLATE - Maker and name separate (more accurate)

# # Only need to edit orange text and XX instances
# # See Kamp for live example

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

#         # Define how to target the image
#         image_src = get_image_src(product, "src")

#         # Define how to target the price
#         price = get_price(product, "tag", "classname")

#         # --- Don't need to edit anything below this point --- #

#         # Call up name and maker strings + text
#         name_string = get_name_string(name_soup)
#         name_text = get_name(name_soup)
#         maker_string = get_maker_string(maker_soup)
#         maker_text = get_maker(maker_soup)

#         # Call up title string
#         title_string = get_title_string(maker_string, name_string)

#         # Call up product type
#         product_type =  get_type(name_string, url)

#         # Call up title
#         title = get_title(name_text, maker_text)

#         # Call up maker
#         maker = lookup_maker(maker_string)

#         # Call up region
#         region = lookup_region(maker, url, title_string)

#         # Process the image source
#         image, image_type = process_image_src(image_src)
        
#         # Check if it's a wine item, if so add to wine list
#         wine = process_item(title_string, image, image_type, url, maker, price, region, store, title, product_type)
#         if wine is not None:
#             wines.append(wine)





# # TEMPLATE

# # Only need to edit orange text and xx instances

# # Test out initial url
# xx_urls = ["https://www.xx.com"]

# # Generate urls (delete if not needed)
# # xx_urls = generate_urls(xx_base_urls, xx_pages)

# for url in xx_urls:

#     # Define store
#     store = 'xx'

#     # Define how to target a product
#     products = get_products(url, "tag", "classname")

#     for product in products:

#         # Define how to target the title 
#         # Note: if name + maker are separate - use other template
#         title_soup = get_title_soup(product, "tag", "classname")

#         # Define how to target the image
#         image_src = get_image_src(product, "src")

#         # Define how to target the price
#         price = get_price(product, "tag", "classname")

#         # --- Don't need to edit anything below this point --- #

#         # Call up title string function to use for parsing
#         title_string = get_title_string(title_soup)

#         # Call up product type
#         product_type =  get_type(title_string, url)

#         # Call up title
#         title = get_title(title_soup)
        
#         # Call up maker
#         maker = lookup_maker(title_string)

#         # Call up region
#         region = lookup_region(maker, url, title_string)

#         # Process the image source
#         image, image_type = process_image_src(image_src)
        
#         # Check if it's a wine item, if so add to wine list
#         wine = process_item(title_string, image, image_type, url, maker, price, region, store, title, product_type)
#         if wine is not None:
#             wines.append(wine)


# /////////// END OF TEMPLATES /////////





# /////////// Los Angeles /////////



# Fancy Free

for url in fancyfree_urls:

    # Define store
    store = 'Fancy Free'

    # Define how to target a product
    products = get_products(url, "div", "grid-item")

    for product in products:

        # Define how to target the title
        title_soup = get_title_soup(product, "div", "grid-title")

        # Define how to target the image
        image_src = get_image_src(product, "data-src")

        # Define how to target the price
        price = get_price(product, "div", "product-price")

        # --- Don't need to edit anything below this point --- #

        # Call up title string function to use for parsing
        title_string = get_title_string(title_soup)

        # Call up product type
        product_type =  get_type(title_string, url)

        # Call up title
        title = get_title(title_soup)

        # Call up maker
        maker = lookup_maker(title_string)

        # Call up region
        region = lookup_region(maker, url, title_string)

        # Process the image source
        image, image_type = process_image_src(image_src)
        
        # Check if it's a wine item, if so add to wine list
        wine = process_item(title_string, image, image_type, url, maker, price, region, store, title, product_type)
        if wine is not None:
            wines.append(wine)
            print(title)




# Flask & Field

# for url in flaskandfield_urls:

#     # Define store
#     store = 'Flask + Field'

#     # Define how to target a product
#     products = get_products(url, "li", "grid__item")

#     for product in products:

#         # Define how to target the title
#         title_soup = get_title_soup(product, "h3", "card__heading")

#         # Define how to target the image
#         image_src = get_image_src(product, "src")

#         # def get_image_src_parentdiv(product, classname=None):

#         # Define how to target the price
#         price = get_price(product, "span", "price-item")

#         # --- Don't need to edit anything below this point --- #

#         # Call up title string function to use for parsing
#         title_string = get_title_string(title_soup)

#         # Call up product type
#         product_type =  get_type(title_string, url)

#         # Call up title
#         title = get_title(title_soup)
        
#         # Call up maker
#         maker = lookup_maker(title_string)

#         # Call up region
#         region = lookup_region(maker, url, title_string)

#         # Process the image source
#         image, image_type = process_image_src(image_src)

#         # Custom code for Flask & Field
#         button = product.find('button')
#         if not button.has_attr('disabled'):
#             # Check if it's a wine item, if so add to wine list
#             wine = process_item(title_string, image, image_type, url, maker, price, region, store, title, product_type)
#             if wine is not None:
#                 wines.append(wine)
#                 print(title)



# Heaven's Market

for url in heavensmarket_urls:

    # Define store
    store = 'Heaven&#39;s Market'

    # Define how to target a product
    products = get_products(url, "li", "grid__item")

    for product in products:

        # Define how to target the title
        title_soup = get_title_soup(product, "span", "visually-hidden")

        # Define how to target the price
        price = get_price(product, "span", "price-item")

        # Define how to target the image
        image_src = get_image_src(product, "src", "grid-view-item__image")
        
        # --- Don't need to edit anything below this point --- #

        # Call up title string function to use for parsing
        title_string = get_title_string(title_soup)

        # Call up product type
        product_type =  get_type(title_string, url)

        # Call up title
        title = get_title(title_soup)
        
        # Call up maker
        maker = lookup_maker(title_string)

        # Call up region
        region = lookup_region(maker, url, title_string)

        # Process the image source
        image, image_type = process_image_src(image_src)

        # Custom code for Heaven's Market
        sold_out = product.find('dl', class_="price--sold-out")
        if not sold_out:
            # Check if it's a wine item, if so add to wine list
            wine = process_item(title_string, image, image_type, url, maker, price, region, store, title, product_type)
            if wine is not None:
                wines.append(wine)
                print(title)






# # Helen's Wine

# for url in helens_urls:

#     # Define store
#     store = 'Helen&#39;s Wines'

#     # Define how to target a product
#     products = get_products(url, "div", "grid-product")

#     for product in products:

#         # Define how to target the title
#         title_soup = get_title_soup(product, "div", "grid-product__title--body")

#         # Define how to target the price
#         price = get_price(product, "div", "grid-product__price")

#         # Define how to target the image
#         image_src = get_image_src(product, "src", "grid-product__image")

#         # --- Don't need to edit anything below this point --- #

#         # Call up title string function to use for parsing
#         title_string = get_title_string(title_soup)

#         # Call up product type
#         product_type =  get_type(title_string, url)

#         # Call up title
#         title = get_title(title_soup)
        
#         # Call up maker
#         maker = lookup_maker(title_string)

#         # Call up region
#         region = lookup_region(maker, url, title_string)

#         # Process the image source
#         image, image_type = process_image_src(image_src)
        
#         # Check if it's a wine item, if so add to wine list
#         wine = process_item(title_string, image, image_type, url, maker, price, region, store, title, product_type)
#         if wine is not None:
#             wines.append(wine)
#             print(title)




# Highland Park Wine

for url in highlandpark_urls:

    # Define store
    store = 'Highland Park Wine'

    # Define how to target a product
    products = get_products(url, "div", "prod-block")

    for product in products:

        # Define how to target the title
        title_soup = get_title_soup(product, "div", "title")

        # Define how to target the price
        price = get_price(product, "div", "product-price")

        # Define how to target the image
        image_src = get_image_src(product, "src", "rimage__image")

        # --- Don't need to edit anything below this point --- #

        # Call up title string function to use for parsing
        title_string = get_title_string(title_soup)

        # Call up product type
        product_type =  get_type(title_string, url)

        # Call up title
        title = get_title(title_soup)
        
        # Call up maker
        maker = lookup_maker(title_string)

        # Call up region
        region = lookup_region(maker, url, title_string)

        # Process the image source
        image, image_type = process_image_src(image_src)
        
        # Check if it's a wine item, if so add to wine list
        wine = process_item(title_string, image, image_type, url, maker, price, region, store, title, product_type)
        if wine is not None:
            wines.append(wine)
            print(title)




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

        # Define how to target the image
        image_src = get_image_src_alt(product, "src")

        # Define how to target the price
        price = get_price(product, "span", "product--price money")

        # --- Don't need to edit anything below this point --- #

        # Call up name and maker strings + text
        name_string = get_name_string(name_soup)
        name_text = get_name(name_soup)
        maker_string = get_maker_string(maker_soup)
        maker_text = get_maker(maker_soup)

        # Call up title string
        title_string = get_title_string(maker_string, name_string)

        # Call up product type
        product_type =  get_type(name_string, url)

        # Call up title
        title = get_title(name_text, maker_text)

        # Call up maker
        maker = lookup_maker(maker_string)

        # Call up region
        region = lookup_region(maker, url, title_string)

        # Process the image source
        image, image_type = process_image_src(image_src)
        
        # Check if it's a wine item, if so add to wine list
        wine = process_item(title_string, image, image_type, url, maker, price, region, store, title, product_type)
        if wine is not None:
            wines.append(wine)
            print(title)



# Silverlake Wine

for url in silverlake_urls:

    # Define store
    store = 'Silverlake Wine'

    # Define how to target a product
    products = get_products(url, "div", "prod-block")

    for product in products:

        # Define how to target the title
        title_soup = get_title_soup(product, "div", "title")

        # Define how to target the image
        image_src = get_image_src(product, "src", "rimage__image")

        # Define how to target the price
        price = get_price(product, "div", "product-price")

        # --- Don't need to edit anything below this point --- #

        # Call up title string function to use for parsing
        title_string = get_title_string(title_soup)

        # Call up product type
        product_type =  get_type(title_string, url)

        # Call up title
        title = get_title(title_soup)
        
        # Call up maker
        maker = lookup_maker(title_string)

        # Call up region
        region = lookup_region(maker, url, title_string)

        # Process the image source
        image, image_type = process_image_src(image_src)
        
        # Check if it's a wine item, if so add to wine list
        wine = process_item(title_string, image, image_type, url, maker, price, region, store, title, product_type)
        if wine is not None:
            wines.append(wine)
            print(title)



# Sip Snack

for url in sipsnack_urls:

    # Define store
    store = 'Sip Snack'

    # Define how to target a product
    products = get_products(url, "div", "product--root")

    for product in products:

        # Define how to target the title
        title_soup = get_title_soup(product, "h3", "product--title")

        # Define how to target the image
        image_src = get_image_src(product, "src")

        # Define how to target the price
        price = get_price(product, "span", "product--price")

        # --- Don't need to edit anything below this point --- #

        # Call up title string function to use for parsing
        title_string = get_title_string(title_soup)

        # Call up product type
        product_type =  get_type(title_string, url.split("/")[-1])

        # Call up title
        title = get_title(title_soup)
        
        # Call up maker
        maker = lookup_maker(title_string)

        # Call up region
        region = lookup_region(maker, url, title_string)

        # Process the image source
        image, image_type = process_image_src(image_src)
        
        # Check if it's a wine item, if so add to wine list
        wine = process_item(title_string, image, image_type, url, maker, price, region, store, title, product_type)
        if wine is not None:
            wines.append(wine)
            print(title)




# Vinovore Eagle Rock

# for url in vinovore_eaglerock_urls:

#     # Define store
#     store = 'Vinovore Eagle Rock'

#     # Define how to target a product
#     products = get_products(url, "div", "grid-product")

#     for product in products:

#         # Define how to target the title
#         title_soup = get_title_soup(product, "div", "grid-product__title")

#         # Define how to target the image
#         image_src = get_image_src(product, "src", "grid-product__image")

#         # ----- Custom price code for Vinovore Eagle Rock -----
        
#         # Define how to target the price
#         pricesoup = product.find("div", class_="grid-product__price")
#         if pricesoup.span:
#             price = 'On Sale'
#         else:
#             price = pricesoup.text.strip()

#         # ----- End custom code -----

#         # --- Don't need to edit anything below this point --- #

#         # Call up title string function to use for parsing
#         title_string = get_title_string(title_soup)

#         # Call up product type
#         product_type =  get_type(title_string, url)

#         # Call up title
#         title = get_title(title_soup)
        
#         # Call up maker
#         maker = lookup_maker(title_string)

#         # Call up region
#         region = lookup_region(maker, url, title_string)

#         # Process the image source
#         image, image_type = process_image_src(image_src)

#         # Custom code for Vinovore Eagle Rock
#         sold_out = product.find('div', class_="grid-product__tag--sold-out")
#         if not sold_out:
#             # Check if it's a wine item, if so add to wine list
#             wine = process_item(title_string, image, image_type, url, maker, price, region, store, title, product_type)
#             if wine is not None:
#                 wines.append(wine)
#                 print(title)
      




# Vinovore Silverlake

for url in vinovore_silverlake_urls:

    # Define store
    store = 'Vinovore Silverlake'

    # Define how to target a product
    products = get_products(url, "div", "product")

    for product in products:

        # Define how to target the title
        title_soup = get_title_soup(product, "h3", "product__title")

        # Define how to target the image
        image_src = get_image_src(product, "src", "product__img")

        # --- Don't need to edit anything below this point --- #

        # Call up title string function to use for parsing
        title_string = get_title_string(title_soup)

        # Call up product type
        product_type =  get_type(title_string, url)

        # Call up title
        title = get_title(title_soup)
        
        # Call up maker
        maker = lookup_maker(title_string)

        # Call up region
        region = lookup_region(maker, url, title_string)

        # Process the image source
        image, image_type = process_image_src(image_src)
        
        # ----- Custom price code for Vinovore Silverlake -----
              
        # Check if sold out
        stock = product.find("p", class_="product__price").text.strip()
   
        # Define how to target the price
        if stock !='Sold Out':
            price = get_price(product, "span", "money")
            # Check if it's a wine item, if so add to wine list
            wine = process_item(title_string, image, image_type, url, maker, price, region, store, title, product_type)
            if wine is not None:
                wines.append(wine)
                print(title)








# Shuffle wine list
random.shuffle(wines)

# Write JSON file
with open("data.json", "w") as writeJSON:
	json.dump({'wine': wines}, writeJSON, ensure_ascii=False)

# Print in terminal (only needed for troubleshooting)    
# print(json.dumps(wines, indent=4))
print('success!')