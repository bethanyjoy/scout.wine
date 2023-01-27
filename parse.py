import re
import json
import requests
from bs4 import BeautifulSoup

# sets up empty list to store wine data
wines = []

# list of silverlake wine urls to parse
sl_orange_urls = [
"https://silverlakewine.com/collections/orange",
"https://silverlakewine.com/collections/orange?page=2",
"https://silverlakewine.com/collections/orange?page=3",
"https://silverlakewine.com/collections/orange?page=4",
"https://silverlakewine.com/collections/orange?page=5",
"https://silverlakewine.com/collections/orange?page=6"
]
# sl_red_urls = [
# ]
# sl_rose_urls = [
# ]
# sl_sparkling_urls = [
# ]
# sl_white_urls = [
# ]

# list of highland park wine urls to parse
# hlp_orange_urls = [
# "https://www.highlandparkwine.com/collections/orange-wine",
# "https://www.highlandparkwine.com/collections/orange-wine?page=2",
# "https://www.highlandparkwine.com/collections/orange-wine?page=3",
# "https://www.highlandparkwine.com/collections/orange-wine?page=4",
# ]
# hlp_red_urls = [
# "https://www.highlandparkwine.com/collections/usa-red-wines",
# "https://www.highlandparkwine.com/collections/usa-red-wines?page=2",
# "https://www.highlandparkwine.com/collections/usa-red-wines?page=3",
# "https://www.highlandparkwine.com/collections/usa-red-wines?page=4",
# "https://www.highlandparkwine.com/collections/usa-red-wines?page=5",
# "https://www.highlandparkwine.com/collections/usa-red-wines?page=6",
# "https://www.highlandparkwine.com/collections/usa-red-wines?page=7",
# "https://www.highlandparkwine.com/collections/french-reds",
# "https://www.highlandparkwine.com/collections/french-reds?page=2",
# "https://www.highlandparkwine.com/collections/french-reds?page=3",
# "https://www.highlandparkwine.com/collections/french-reds?page=4",
# "https://www.highlandparkwine.com/collections/french-reds?page=5",
# "https://www.highlandparkwine.com/collections/french-reds?page=6",
# "https://www.highlandparkwine.com/collections/french-reds?page=7",
# "https://www.highlandparkwine.com/collections/french-reds?page=8",
# "https://www.highlandparkwine.com/collections/italian-reds",
# "https://www.highlandparkwine.com/collections/italian-reds?page=2",
# "https://www.highlandparkwine.com/collections/italian-reds?page=3",
# "https://www.highlandparkwine.com/collections/italian-reds?page=4",
# "https://www.highlandparkwine.com/collections/spanish-portuguese-reds",
# "https://www.highlandparkwine.com/collections/spanish-portuguese-reds?page=2",
# "https://www.highlandparkwine.com/collections/spanish-portuguese-reds?page=3",
# ]
# hlp_rose_urls = [
# ]
# hlp_sparkling_urls = [
# ]
# hlp_white_urls = [
# ]

# list of everson royce urls to parse
# er_orange_urls = [
# "https://www.eversonroyce.com/collections/orange-wine"
# ]
# er_red_urls = [
# ]
# er_rose_urls = [
# ]
# er_sparkling_urls = [
# ]
# er_white_urls = [
# ]

# code for parsing highland park wine urls
# for x in hlp_orange_urls:
#     soup = BeautifulSoup(requests.get(x).content, 'html.parser')
#     products = soup.find_all("div", class_="grid-product")
#     for product in products:
#         title = product.find("div", class_="grid-product__title-inner").text.replace(" ", "")
#         title_text = product.find("div", class_="grid-product__title-inner").text.strip()
#         price = product.find("div", class_="grid-product__price").text.strip()
#         link = product.find("a", class_="grid-product__title")['href']
#         if product.img:
#             image = product.find("img", class_="grid-product__picture")['src']
#         else:
#             image = 'https://cdn11.bigcommerce.com/s-t1pm6282q8/images/stencil/500x659/products/918/1976/image_coming_soon__47973.1624218886.1280.1280__52076.1628386968.jpg?c=1'
#         store = 'highlandpark'
#         store_text = 'Highland Park Wine'
#         type = 'orange'
#         type_text = 'Orange'
#         wines.append({
#             'Title': title,
#             'Title_text': title_text,
#             'Price': price,
#             'Link': link,
#             'Image': image,
#             'Type': type,
#             'Type_text': type_text,
#             'Store': store,
#             'Store_text': store_text,
#         })
# for x in hlp_rose_urls:
#     soup = BeautifulSoup(requests.get(x).content, 'html.parser')
#     products = soup.find_all("div", class_="grid-product")
#     for product in products:
#         title = product.find("div", class_="grid-product__title-inner").text.replace(" ", "")
#         title_text = product.find("div", class_="grid-product__title-inner").text.strip()
#         price = product.find("div", class_="grid-product__price").text.strip()
#         link = product.find("a", class_="grid-product__title")['href']
#         if product.img:
#             image = product.find("img", class_="grid-product__picture")['src']
#         else:
#             image = 'https://cdn11.bigcommerce.com/s-t1pm6282q8/images/stencil/500x659/products/918/1976/image_coming_soon__47973.1624218886.1280.1280__52076.1628386968.jpg?c=1'
#         store = 'highlandpark'
#         store_text = 'Highland Park Wine'
#         type = 'rose'
#         type_text = 'Ros&#233;'
#         wines.append({
#             'Title': title,
#             'Title_text': title_text,
#             'Price': price,
#             'Link': link,
#             'Image': image,
#             'Type': type,
#             'Type_text': type_text,
#             'Store': store,
#             'Store_text': store_text,
#         })
# for x in hlp_red_urls:
#     soup = BeautifulSoup(requests.get(x).content, 'html.parser')
#     products = soup.find_all("div", class_="grid-product")
#     for product in products:
#         title = product.find("div", class_="grid-product__title-inner").text.replace(" ", "")
#         title_text = product.find("div", class_="grid-product__title-inner").text.strip()
#         price = product.find("div", class_="grid-product__price").text.strip()
#         link = product.find("a", class_="grid-product__title")['href']
#         if product.img:
#             image = product.find("img", class_="grid-product__picture")['src']
#         else:
#             image = 'https://cdn11.bigcommerce.com/s-t1pm6282q8/images/stencil/500x659/products/918/1976/image_coming_soon__47973.1624218886.1280.1280__52076.1628386968.jpg?c=1'
#         store = 'highlandpark'
#         store_text = 'Highland Park Wine'
#         type = 'red'
#         type_text = 'Red'
#         wines.append({
#             'Title': title,
#             'Title_text': title_text,
#             'Price': price,
#             'Link': link,
#             'Image': image,
#             'Type': type,
#             'Type_text': type_text,
#             'Store': store,
#             'Store_text': store_text,
#         })
# for x in hlp_white_urls:
#     soup = BeautifulSoup(requests.get(x).content, 'html.parser')
#     products = soup.find_all("div", class_="grid-product")
#     for product in products:
#         title = product.find("div", class_="grid-product__title-inner").text.replace(" ", "")
#         title_text = product.find("div", class_="grid-product__title-inner").text.strip()
#         price = product.find("div", class_="grid-product__price").text.strip()
#         link = product.find("a", class_="grid-product__title")['href']
#         if product.img:
#             image = product.find("img", class_="grid-product__picture")['src']
#         else:
#             image = 'https://cdn11.bigcommerce.com/s-t1pm6282q8/images/stencil/500x659/products/918/1976/image_coming_soon__47973.1624218886.1280.1280__52076.1628386968.jpg?c=1'
#         store = 'highlandpark'
#         store_text = 'Highland Park Wine'
#         type = 'white'
#         type_text = 'White'
#         wines.append({
#             'Title': title,
#             'Title_text': title_text,
#             'Price': price,
#             'Link': link,
#             'Image': image,
#             'Type': type,
#             'Type_text': type_text,
#             'Store': store,
#             'Store_text': store_text,
#         })
# for x in hlp_sparkling_urls:
#     soup = BeautifulSoup(requests.get(x).content, 'html.parser')
#     products = soup.find_all("div", class_="grid-product")
#     for product in products:
#         title = product.find("div", class_="grid-product__title-inner").text.replace(" ", "")
#         title_text = product.find("div", class_="grid-product__title-inner").text.strip()
#         price = product.find("div", class_="grid-product__price").text.strip()
#         link = product.find("a", class_="grid-product__title")['href']
#         if product.img:
#             image = product.find("img", class_="grid-product__picture")['src']
#         else:
#             image = 'https://cdn11.bigcommerce.com/s-t1pm6282q8/images/stencil/500x659/products/918/1976/image_coming_soon__47973.1624218886.1280.1280__52076.1628386968.jpg?c=1'
#         store = 'highlandpark'
#         store_text = 'Highland Park Wine'
#         type = 'sparkling'
#         type_text = 'Sparkling'
#         wines.append({
#             'Title': title,
#             'Title_text': title_text,
#             'Price': price,
#             'Link': link,
#             'Image': image,
#             'Type': type,
#             'Type_text': type_text,
#             'Store': store,
#             'Store_text': store_text,
#         })

# code for parsing silverlake wine urls
for x in sl_orange_urls:
    soup = BeautifulSoup(requests.get(x).content, 'html.parser')
    products = soup.find_all("div", class_="prod-block")
    for product in products:
        title = product.find("div", class_="title").text.replace(" ", "")
        title_text = product.find("div", class_="title").text.strip()
        price = product.find("div", class_="product-price").text.strip()
        link = 'https://silverlakewine.com' + product.find("a")['href']
        imagesoup = product.find('noscript')
        imageurl = imagesoup.find("img", class_="rimage__image")['src']
        image = 'https:' + imageurl
        store = 'silverlake'
        store_text = 'Silver Lake Wine'
        type = 'orange'
        type_text = 'Orange'
        wines.append({
            'Title': title,
            'Title_text': title_text,
            'Price': price,
            'Link': link,
            'Image': image,
            'Type': type,
            'Type_text': type_text,
            'Store': store,
            'Store_text': store_text,
        })
# for x in sl_rose_urls:
#     soup = BeautifulSoup(requests.get(x).content, 'html.parser')
#     products = soup.find_all("div", class_="grid-product")
#     for product in products:
#         title = product.find("div", class_="title").text.replace(" ", "")
#         title_text = product.find("div", class_="title").text.strip()
#         price = product.find("div", class_="product-price").text.strip()
#         link = product.find("a")['href']
#         imagesoup = product.find('noscript')
#         imageurl = imagesoup.find("img", class_="rimage__image")['src']
#         image = 'https:' + imageurl
#         store = 'silverlake'
#         store_text = 'Silver Lake Wine'
#         type = 'rose'
#         type_text = 'Ros&#233;'
#         wines.append({
#             'Title': title,
#             'Title_text': title_text,
#             'Price': price,
#             'Link': link,
#             'Image': image,
#             'Type': type,
#             'Type_text': type_text,
#             'Store': store,
#             'Store_text': store_text,
#         })
# for x in sl_red_urls:
#     soup = BeautifulSoup(requests.get(x).content, 'html.parser')
#     products = soup.find_all("div", class_="grid-product")
#     for product in products:
#         title = product.find("div", class_="title").text.replace(" ", "")
#         title_text = product.find("div", class_="title").text.strip()
#         price = product.find("div", class_="product-price").text.strip()
#         link = product.find("a")['href']
#         imagesoup = product.find('noscript')
#         imageurl = imagesoup.find("img", class_="rimage__image")['src']
#         image = 'https:' + imageurl
#         store = 'silverlake'
#         store_text = 'Silver Lake Wine'
#         type = 'red'
#         type_text = 'Red'
#         wines.append({
#             'Title': title,
#             'Title_text': title_text,
#             'Price': price,
#             'Link': link,
#             'Image': image,
#             'Type': type,
#             'Type_text': type_text,
#             'Store': store,
#             'Store_text': store_text,
#         })
# for x in sl_white_urls:
#     soup = BeautifulSoup(requests.get(x).content, 'html.parser')
#     products = soup.find_all("div", class_="grid-product")
#     for product in products:
#         title = product.find("div", class_="title").text.replace(" ", "")
#         title_text = product.find("div", class_="title").text.strip()
#         price = product.find("div", class_="product-price").text.strip()
#         link = product.find("a")['href']
#         imagesoup = product.find('noscript')
#         imageurl = imagesoup.find("img", class_="rimage__image")['src']
#         image = 'https:' + imageurl
#         store = 'silverlake'
#         store_text = 'Silver Lake Wine'
#         type = 'white'
#         type_text = 'White'
#         wines.append({
#             'Title': title,
#             'Title_text': title_text,
#             'Price': price,
#             'Link': link,
#             'Image': image,
#             'Type': type,
#             'Type_text': type_text,
#             'Store': store,
#             'Store_text': store_text,
#         })
# for x in sl_sparkling_urls:
#     soup = BeautifulSoup(requests.get(x).content, 'html.parser')
#     products = soup.find_all("div", class_="grid-product")
#     for product in products:
#         title = product.find("div", class_="title").text.replace(" ", "")
#         title_text = product.find("div", class_="title").text.strip()
#         price = product.find("div", class_="product-price").text.strip()
#         link = product.find("a")['href']
#         imagesoup = product.find('noscript')
#         imageurl = imagesoup.find("img", class_="rimage__image")['src']
#         image = 'https:' + imageurl
#         store = 'silverlake'
#         store_text = 'Silver Lake Wine'
#         type = 'sparkling'
#         type_text = 'Sparkling'
#         wines.append({
#             'Title': title,
#             'Title_text': title_text,
#             'Price': price,
#             'Link': link,
#             'Image': image,
#             'Type': type,
#             'Type_text': type_text,
#             'Store': store,
#             'Store_text': store_text,
#         })

# code for parsing everson royce wine urls
# for x in er_orange_urls:
#     soup = BeautifulSoup(requests.get(x).content, 'html.parser')
#     products = soup.find_all("div", class_="grid-product")
#     for product in products:
#         title = product.find("div", class_="grid-product__title-inner").text.replace(" ", "")
#         title_text = product.find("div", class_="grid-product__title-inner").text.strip()
#         price = product.find("div", class_="grid-product__price").text.strip()
#         link = product.find("a", class_="grid-product__title")['href']
#         if product.img:
#             image = product.find("img", class_="grid-product__picture")['src']
#         else:
#             image = 'https://cdn11.bigcommerce.com/s-t1pm6282q8/images/stencil/500x659/products/918/1976/image_coming_soon__47973.1624218886.1280.1280__52076.1628386968.jpg?c=1'
#         store = 'eversonroyce'
#         store_text = 'Everson Royce'
#         type = 'orange'
#         type_text = 'Orange'
#         wines.append({
#             'Title': title,
#             'Title_text': title_text,
#             'Price': price,
#             'Link': link,
#             'Image': image,
#             'Type': type,
#             'Type_text': type_text,
#             'Store': store,
#             'Store_text': store_text,
#         })
# for x in er_rose_urls:
#     soup = BeautifulSoup(requests.get(x).content, 'html.parser')
#     products = soup.find_all("div", class_="grid-product")
#     for product in products:
#         title = product.find("div", class_="grid-product__title-inner").text.replace(" ", "")
#         title_text = product.find("div", class_="grid-product__title-inner").text.strip()
#         price = product.find("div", class_="grid-product__price").text.strip()
#         link = product.find("a", class_="grid-product__title")['href']
#         if product.img:
#             image = product.find("img", class_="grid-product__picture")['src']
#         else:
#             image = 'https://cdn11.bigcommerce.com/s-t1pm6282q8/images/stencil/500x659/products/918/1976/image_coming_soon__47973.1624218886.1280.1280__52076.1628386968.jpg?c=1'
#         store = 'eversonroyce'
#         store_text = 'Everson Royce'
#         type = 'rose'
#         type_text = 'Ros&#233;'
#         wines.append({
#             'Title': title,
#             'Title_text': title_text,
#             'Price': price,
#             'Link': link,
#             'Image': image,
#             'Type': type,
#             'Type_text': type_text,
#             'Store': store,
#             'Store_text': store_text,
#         })
# for x in er_red_urls:
#     soup = BeautifulSoup(requests.get(x).content, 'html.parser')
#     products = soup.find_all("div", class_="grid-product")
#     for product in products:
#         title = product.find("div", class_="grid-product__title-inner").text.replace(" ", "")
#         title_text = product.find("div", class_="grid-product__title-inner").text.strip()
#         price = product.find("div", class_="grid-product__price").text.strip()
#         link = product.find("a", class_="grid-product__title")['href']
#         if product.img:
#             image = product.find("img", class_="grid-product__picture")['src']
#         else:
#             image = 'https://cdn11.bigcommerce.com/s-t1pm6282q8/images/stencil/500x659/products/918/1976/image_coming_soon__47973.1624218886.1280.1280__52076.1628386968.jpg?c=1'
#         store = 'eversonroyce'
#         store_text = 'Everson Royce'
#         type = 'red'
#         type_text = 'Red'
#         wines.append({
#             'Title': title,
#             'Title_text': title_text,
#             'Price': price,
#             'Link': link,
#             'Image': image,
#             'Type': type,
#             'Type_text': type_text,
#             'Store': store,
#             'Store_text': store_text,
#         })
# for x in er_white_urls:
#     soup = BeautifulSoup(requests.get(x).content, 'html.parser')
#     products = soup.find_all("div", class_="grid-product")
#     for product in products:
#         title = product.find("div", class_="grid-product__title-inner").text.replace(" ", "")
#         title_text = product.find("div", class_="grid-product__title-inner").text.strip()
#         price = product.find("div", class_="grid-product__price").text.strip()
#         link = product.find("a", class_="grid-product__title")['href']
#         if product.img:
#             image = product.find("img", class_="grid-product__picture")['src']
#         else:
#             image = 'https://cdn11.bigcommerce.com/s-t1pm6282q8/images/stencil/500x659/products/918/1976/image_coming_soon__47973.1624218886.1280.1280__52076.1628386968.jpg?c=1'
#         store = 'eversonroyce'
#         store_text = 'Everson Royce'
#         type = 'white'
#         type_text = 'White'
#         wines.append({
#             'Title': title,
#             'Title_text': title_text,
#             'Price': price,
#             'Link': link,
#             'Image': image,
#             'Type': type,
#             'Type_text': type_text,
#             'Store': store,
#             'Store_text': store_text,
#         })
# for x in er_sparkling_urls:
#     soup = BeautifulSoup(requests.get(x).content, 'html.parser')
#     products = soup.find_all("div", class_="grid-product")
#     for product in products:
#         title = product.find("div", class_="grid-product__title-inner").text.replace(" ", "")
#         title_text = product.find("div", class_="grid-product__title-inner").text.strip()
#         price = product.find("div", class_="grid-product__price").text.strip()
#         link = product.find("a", class_="grid-product__title")['href']
#         if product.img:
#             image = product.find("img", class_="grid-product__picture")['src']
#         else:
#             image = 'https://cdn11.bigcommerce.com/s-t1pm6282q8/images/stencil/500x659/products/918/1976/image_coming_soon__47973.1624218886.1280.1280__52076.1628386968.jpg?c=1'
#         store = 'eversonroyce'
#         store_text = 'Everson Royce'
#         type = 'sparkling'
#         type_text = 'Sparkling'
#         wines.append({
#             'Title': title,
#             'Title_text': title_text,
#             'Price': price,
#             'Link': link,
#             'Image': image,
#             'Type': type,
#             'Type_text': type_text,
#             'Store': store,
#             'Store_text': store_text,
#         })


# writes the wine data to the json file
with open("data.json", "w") as writeJSON:
    json.dump({'wine': wines}, writeJSON, ensure_ascii=False)

# prints data to terminal (only needed for troubleshooting)
# print(json.dumps(wines, indent=4))
print('success!')
