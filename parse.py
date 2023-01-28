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
sl_red_urls = [
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
"https://silverlakewine.com/collections/red?page=26"
]
sl_rose_urls = [
"https://silverlakewine.com/collections/rose",
"https://silverlakewine.com/collections/rose?page=2",
"https://silverlakewine.com/collections/rose?page=3",
"https://silverlakewine.com/collections/rose?page=4",
"https://silverlakewine.com/collections/rose?page=5",
"https://silverlakewine.com/collections/rose?page=6"
]
sl_sparkling_urls = [
"https://silverlakewine.com/collections/sparkling",
"https://silverlakewine.com/collections/sparkling?page=2",
"https://silverlakewine.com/collections/sparkling?page=3",
"https://silverlakewine.com/collections/sparkling?page=4",
"https://silverlakewine.com/collections/sparkling?page=5",
"https://silverlakewine.com/collections/sparkling?page=6",
"https://silverlakewine.com/collections/sparkling?page=7",
"https://silverlakewine.com/collections/sparkling?page=8"
]
sl_white_urls = [
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
"https://silverlakewine.com/collections/white?page=14"
]

# list of highland park wine urls to parse
hlp_orange_urls = [
"https://www.highlandparkwine.com/collections/orange-wine",
"https://www.highlandparkwine.com/collections/orange-wine?page=2",
"https://www.highlandparkwine.com/collections/orange-wine?page=3",
"https://www.highlandparkwine.com/collections/orange-wine?page=4"
]
hlp_red_urls = [
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
"https://www.highlandparkwine.com/collections/reds-from-the-southern-hemisphere?page=4"
]
hlp_rose_urls = [
"https://www.highlandparkwine.com/collections/rose",
"https://www.highlandparkwine.com/collections/rose?page=2",
"https://www.highlandparkwine.com/collections/rose?page=3",
"https://www.highlandparkwine.com/collections/rose?page=4",
"https://www.highlandparkwine.com/collections/rose?page=5"
]
hlp_sparkling_urls = [
"https://www.highlandparkwine.com/collections/sparkling-wine",
"https://www.highlandparkwine.com/collections/sparkling-wine?page=2",
"https://www.highlandparkwine.com/collections/sparkling-wine?page=3",
"https://www.highlandparkwine.com/collections/sparkling-wine?page=4",
"https://www.highlandparkwine.com/collections/sparkling-wine?page=5",
"https://www.highlandparkwine.com/collections/sparkling-wine?page=6"
]
hlp_white_urls = [
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
"https://www.highlandparkwine.com/collections/white-wines-from-the-southern-hemisphere?page=2"
]

# list of everson royce urls to parse
er_orange_urls = [
"https://www.eversonroyce.com/collections/orange-wine",
"https://www.eversonroyce.com/collections/orange-wine?page=2",
"https://www.eversonroyce.com/collections/orange-wine?page=3",
"https://www.eversonroyce.com/collections/orange-wine?page=4",
"https://www.eversonroyce.com/collections/orange-wine?page=5",
]
er_red_urls = [
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
"https://www.eversonroyce.com/collections/reds-from-the-southern-hemisphere?page=2"
]
er_rose_urls = [
"https://www.eversonroyce.com/collections/rose",
"https://www.eversonroyce.com/collections/rose?page=2",
"https://www.eversonroyce.com/collections/rose?page=3",
"https://www.eversonroyce.com/collections/rose?page=4"
]
er_sparkling_urls = [
"https://www.eversonroyce.com/collections/sparklin-wine",
"https://www.eversonroyce.com/collections/sparklin-wine?page=2",
"https://www.eversonroyce.com/collections/sparklin-wine?page=3",
"https://www.eversonroyce.com/collections/sparklin-wine?page=4",
"https://www.eversonroyce.com/collections/sparklin-wine?page=5",
"https://www.eversonroyce.com/collections/sparklin-wine?page=6"
]
er_white_urls = [
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
"https://www.eversonroyce.com/collections/white-wines-from-the-southern-hemisphere?page=2"
]

# list of vinovore eagle rock urls to parse
vver_orange_urls = [
"https://vinovoreeaglerock.com/collections/orange",
"https://vinovoreeaglerock.com/collections/orange?page=2",
"https://vinovoreeaglerock.com/collections/orange?page=3",
"https://vinovoreeaglerock.com/collections/orange?page=4"
]
vver_rose_urls = [
"https://vinovoreeaglerock.com/collections/rose",
"https://vinovoreeaglerock.com/collections/rose?page=2",
"https://vinovoreeaglerock.com/collections/rose?page=3",
"https://vinovoreeaglerock.com/collections/rose?page=4"
]
vver_red_urls = [
"https://vinovoreeaglerock.com/collections/red",
"https://vinovoreeaglerock.com/collections/red?page=2",
"https://vinovoreeaglerock.com/collections/red?page=3",
"https://vinovoreeaglerock.com/collections/red?page=4",
"https://vinovoreeaglerock.com/collections/red?page=5",
"https://vinovoreeaglerock.com/collections/red?page=6",
"https://vinovoreeaglerock.com/collections/red?page=7",
"https://vinovoreeaglerock.com/collections/red?page=8",
]
vver_white_urls = [
"https://vinovoreeaglerock.com/collections/white",
"https://vinovoreeaglerock.com/collections/white?page=2",
"https://vinovoreeaglerock.com/collections/white?page=3",
"https://vinovoreeaglerock.com/collections/white?page=4",
"https://vinovoreeaglerock.com/collections/white?page=5",
"https://vinovoreeaglerock.com/collections/white?page=6",
]
vver_sparkling_urls = [
"https://vinovoreeaglerock.com/collections/sparkling",
"https://vinovoreeaglerock.com/collections/sparkling?page=2",
"https://vinovoreeaglerock.com/collections/sparkling?page=3",
"https://vinovoreeaglerock.com/collections/sparkling?page=4",
"https://vinovoreeaglerock.com/collections/sparkling?page=5",
"https://vinovoreeaglerock.com/collections/sparkling?page=6",
]

# code for parsing highland park wine urls
for x in hlp_orange_urls:
    soup = BeautifulSoup(requests.get(x).content, 'html.parser')
    products = soup.find_all("div", class_="prod-block")
    for product in products:
        title = product.find("div", class_="title").text.replace(" ", "")
        title_text = product.find("div", class_="title").text.strip()
        price = product.find("div", class_="product-price").text.strip()
        link = 'http://highlandparkwine.com' + product.find("a")['href']
        imagesoup = product.find('noscript')
        imageurl = imagesoup.find("img", class_="rimage__image")['src']
        image = 'https:' + imageurl
        store = 'highlandpark'
        store_text = 'Highland Park Wine'
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
for x in hlp_rose_urls:
    soup = BeautifulSoup(requests.get(x).content, 'html.parser')
    products = soup.find_all("div", class_="prod-block")
    for product in products:
        title = product.find("div", class_="title").text.replace(" ", "")
        title_text = product.find("div", class_="title").text.strip()
        price = product.find("div", class_="product-price").text.strip()
        link = 'http://highlandparkwine.com' + product.find("a")['href']
        imagesoup = product.find('noscript')
        imageurl = imagesoup.find("img", class_="rimage__image")['src']
        image = 'https:' + imageurl
        store = 'highlandpark'
        store_text = 'Highland Park Wine'
        type = 'rose'
        type_text = 'Ros&#233;'
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
for x in hlp_red_urls:
    soup = BeautifulSoup(requests.get(x).content, 'html.parser')
    products = soup.find_all("div", class_="prod-block")
    for product in products:
        title = product.find("div", class_="title").text.replace(" ", "")
        title_text = product.find("div", class_="title").text.strip()
        price = product.find("div", class_="product-price").text.strip()
        link = 'http://highlandparkwine.com' + product.find("a")['href']
        imagesoup = product.find('noscript')
        imageurl = imagesoup.find("img", class_="rimage__image")['src']
        image = 'https:' + imageurl
        store = 'highlandpark'
        store_text = 'Highland Park Wine'
        type = 'red'
        type_text = 'Red'
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
for x in hlp_white_urls:
    soup = BeautifulSoup(requests.get(x).content, 'html.parser')
    products = soup.find_all("div", class_="prod-block")
    for product in products:
        title = product.find("div", class_="title").text.replace(" ", "")
        title_text = product.find("div", class_="title").text.strip()
        price = product.find("div", class_="product-price").text.strip()
        link = 'http://highlandparkwine.com' + product.find("a")['href']
        imagesoup = product.find('noscript')
        imageurl = imagesoup.find("img", class_="rimage__image")['src']
        image = 'https:' + imageurl
        store = 'highlandpark'
        store_text = 'Highland Park Wine'
        type = 'white'
        type_text = 'White'
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
for x in hlp_sparkling_urls:
    soup = BeautifulSoup(requests.get(x).content, 'html.parser')
    products = soup.find_all("div", class_="prod-block")
    for product in products:
        title = product.find("div", class_="title").text.replace(" ", "")
        title_text = product.find("div", class_="title").text.strip()
        price = product.find("div", class_="product-price").text.strip()
        link = 'http://highlandparkwine.com' + product.find("a")['href']
        imagesoup = product.find('noscript')
        imageurl = imagesoup.find("img", class_="rimage__image")['src']
        image = 'https:' + imageurl
        store = 'highlandpark'
        store_text = 'Highland Park Wine'
        type = 'sparkling'
        type_text = 'Sparkling'
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


# code for parsing vinovore eagle rock urls
for x in vver_orange_urls:
    soup = BeautifulSoup(requests.get(x).content, 'html.parser')
    products = soup.find_all("div", class_="grid-product")
    for product in products:
        title = product.find("div", class_="grid-product__title").text.replace(" ", "")
        if title == 'BuildAGiftBox' or title == 'AddAGiftBoxorBag':
          print()
        else:
          title_text = product.find("div", class_="grid-product__title").text.strip()
          pricesoup = product.find("div", class_="grid-product__price")
          if pricesoup.span:
            price = 'On Sale'
          else:
            price = pricesoup.text.strip()
          link = 'http://vinovoreeaglerock.com' + product.find("a")['href']
          imagesoup = product.find('noscript')
          imageurl = imagesoup.find("img", class_="grid-product__image")['src']
          image = 'https:' + imageurl
          store = 'vinovoreeaglerock'
          store_text = 'Vinovore Eagle Rock'
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
for x in vver_rose_urls:
    soup = BeautifulSoup(requests.get(x).content, 'html.parser')
    products = soup.find_all("div", class_="grid-product")
    for product in products:
        title = product.find("div", class_="grid-product__title").text.replace(" ", "")
        if title == 'BuildAGiftBox' or title == 'AddAGiftBoxorBag':
          print()
        else:
          title_text = product.find("div", class_="grid-product__title").text.strip()
          pricesoup = product.find("div", class_="grid-product__price")
          if pricesoup.span:
            price = 'On Sale'
          else:
            price = pricesoup.text.strip()
          link = 'http://vinovoreeaglerock.com' + product.find("a")['href']
          imagesoup = product.find('noscript')
          imageurl = imagesoup.find("img", class_="grid-product__image")['src']
          image = 'https:' + imageurl
          store = 'vinovoreeaglerock'
          store_text = 'Vinovore Eagle Rock'
          type = 'rose'
          type_text = 'Ros&#233;'
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
for x in vver_red_urls:
    soup = BeautifulSoup(requests.get(x).content, 'html.parser')
    products = soup.find_all("div", class_="grid-product")
    for product in products:
        title = product.find("div", class_="grid-product__title").text.replace(" ", "")
        if title == 'BuildAGiftBox' or title == 'AddAGiftBoxorBag':
          print()
        else:
          title_text = product.find("div", class_="grid-product__title").text.strip()
          pricesoup = product.find("div", class_="grid-product__price")
          if pricesoup.span:
            price = 'On Sale'
          else:
            price = pricesoup.text.strip()
          link = 'http://vinovoreeaglerock.com' + product.find("a")['href']
          imagesoup = product.find('noscript')
          imageurl = imagesoup.find("img", class_="grid-product__image")['src']
          image = 'https:' + imageurl
          store = 'vinovoreeaglerock'
          store_text = 'Vinovore Eagle Rock'
          type = 'red'
          type_text = 'Red'
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
for x in vver_white_urls:
    soup = BeautifulSoup(requests.get(x).content, 'html.parser')
    products = soup.find_all("div", class_="grid-product")
    for product in products:
        title = product.find("div", class_="grid-product__title").text.replace(" ", "")
        if title == 'BuildAGiftBox' or title == 'AddAGiftBoxorBag':
          print()
        else:
          title_text = product.find("div", class_="grid-product__title").text.strip()
          pricesoup = product.find("div", class_="grid-product__price")
          if pricesoup.span:
            price = 'On Sale'
          else:
            price = pricesoup.text.strip()
          link = 'http://vinovoreeaglerock.com' + product.find("a")['href']
          imagesoup = product.find('noscript')
          imageurl = imagesoup.find("img", class_="grid-product__image")['src']
          image = 'https:' + imageurl
          store = 'vinovoreeaglerock'
          store_text = 'Vinovore Eagle Rock'
          type = 'white'
          type_text = 'White'
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
for x in vver_sparkling_urls:
    soup = BeautifulSoup(requests.get(x).content, 'html.parser')
    products = soup.find_all("div", class_="grid-product")
    for product in products:
        title = product.find("div", class_="grid-product__title").text.replace(" ", "")
        if title == 'BuildAGiftBox' or title == 'AddAGiftBoxorBag':
          print()
        else:
          title_text = product.find("div", class_="grid-product__title").text.strip()
          pricesoup = product.find("div", class_="grid-product__price")
          if pricesoup.span:
            price = 'On Sale'
          else:
            price = pricesoup.text.strip()
          link = 'http://vinovoreeaglerock.com' + product.find("a")['href']
          imagesoup = product.find('noscript')
          imageurl = imagesoup.find("img", class_="grid-product__image")['src']
          image = 'https:' + imageurl
          store = 'vinovoreeaglerock'
          store_text = 'Vinovore Eagle Rock'
          type = 'sparkling'
          type_text = 'Sparkling'
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



# code for parsing silverlake wine urls
for x in sl_orange_urls:
    soup = BeautifulSoup(requests.get(x).content, 'html.parser')
    products = soup.find_all("div", class_="prod-block")
    for product in products:
        title = product.find("div", class_="title").text.replace(" ", "")
        title_text = product.find("div", class_="title").text.strip()
        price = product.find("div", class_="product-price").text.strip()
        link = 'http://silverlakewine.com' + product.find("a")['href']
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
for x in sl_rose_urls:
    soup = BeautifulSoup(requests.get(x).content, 'html.parser')
    products = soup.find_all("div", class_="prod-block")
    for product in products:
        title = product.find("div", class_="title").text.replace(" ", "")
        title_text = product.find("div", class_="title").text.strip()
        price = product.find("div", class_="product-price").text.strip()
        link = 'http://silverlakewine.com' + product.find("a")['href']
        imagesoup = product.find('noscript')
        imageurl = imagesoup.find("img", class_="rimage__image")['src']
        image = 'https:' + imageurl
        store = 'silverlake'
        store_text = 'Silver Lake Wine'
        type = 'rose'
        type_text = 'Ros&#233;'
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
for x in sl_red_urls:
    soup = BeautifulSoup(requests.get(x).content, 'html.parser')
    products = soup.find_all("div", class_="prod-block")
    for product in products:
        title = product.find("div", class_="title").text.replace(" ", "")
        title_text = product.find("div", class_="title").text.strip()
        price = product.find("div", class_="product-price").text.strip()
        link = 'http://silverlakewine.com' + product.find("a")['href']
        imagesoup = product.find('noscript')
        imageurl = imagesoup.find("img", class_="rimage__image")['src']
        image = 'https:' + imageurl
        store = 'silverlake'
        store_text = 'Silver Lake Wine'
        type = 'red'
        type_text = 'Red'
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
for x in sl_white_urls:
    soup = BeautifulSoup(requests.get(x).content, 'html.parser')
    products = soup.find_all("div", class_="prod-block")
    for product in products:
        title = product.find("div", class_="title").text.replace(" ", "")
        title_text = product.find("div", class_="title").text.strip()
        price = product.find("div", class_="product-price").text.strip()
        link = 'http://silverlakewine.com' + product.find("a")['href']
        imagesoup = product.find('noscript')
        imageurl = imagesoup.find("img", class_="rimage__image")['src']
        image = 'https:' + imageurl
        store = 'silverlake'
        store_text = 'Silver Lake Wine'
        type = 'white'
        type_text = 'White'
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
for x in sl_sparkling_urls:
    soup = BeautifulSoup(requests.get(x).content, 'html.parser')
    products = soup.find_all("div", class_="prod-block")
    for product in products:
        title = product.find("div", class_="title").text.replace(" ", "")
        title_text = product.find("div", class_="title").text.strip()
        price = product.find("div", class_="product-price").text.strip()
        link = 'http://silverlakewine.com' + product.find("a")['href']
        imagesoup = product.find('noscript')
        imageurl = imagesoup.find("img", class_="rimage__image")['src']
        image = 'https:' + imageurl
        store = 'silverlake'
        store_text = 'Silver Lake Wine'
        type = 'sparkling'
        type_text = 'Sparkling'
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

# code for parsing everson royce wine urls
for x in er_orange_urls:
    soup = BeautifulSoup(requests.get(x).content, 'html.parser')
    products = soup.find_all("div", class_="prod-block")
    for product in products:
        title = product.find("div", class_="title").text.replace(" ", "")
        title_text = product.find("div", class_="title").text.strip()
        price = product.find("div", class_="product-price").text.strip()
        link = 'http://eversonroyce.com' + product.find("a")['href']
        imagesoup = product.find('noscript')
        imageurl = imagesoup.find("img", class_="rimage__image")['src']
        image = 'https:' + imageurl
        store = 'eversonroyce'
        store_text = 'Everson Royce'
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
for x in er_rose_urls:
    soup = BeautifulSoup(requests.get(x).content, 'html.parser')
    products = soup.find_all("div", class_="prod-block")
    for product in products:
        title = product.find("div", class_="title").text.replace(" ", "")
        title_text = product.find("div", class_="title").text.strip()
        price = product.find("div", class_="product-price").text.strip()
        link = 'http://eversonroyce.com' + product.find("a")['href']
        imagesoup = product.find('noscript')
        imageurl = imagesoup.find("img", class_="rimage__image")['src']
        image = 'https:' + imageurl
        store = 'eversonroyce'
        store_text = 'Everson Royce'
        type = 'rose'
        type_text = 'Ros&#233;'
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
for x in er_red_urls:
    soup = BeautifulSoup(requests.get(x).content, 'html.parser')
    products = soup.find_all("div", class_="prod-block")
    for product in products:
        title = product.find("div", class_="title").text.replace(" ", "")
        title_text = product.find("div", class_="title").text.strip()
        price = product.find("div", class_="product-price").text.strip()
        link = 'http://eversonroyce.com' + product.find("a")['href']
        imagesoup = product.find('noscript')
        imageurl = imagesoup.find("img", class_="rimage__image")['src']
        image = 'https:' + imageurl
        store = 'eversonroyce'
        store_text = 'Everson Royce'
        type = 'red'
        type_text = 'Red'
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
for x in er_white_urls:
    soup = BeautifulSoup(requests.get(x).content, 'html.parser')
    products = soup.find_all("div", class_="prod-block")
    for product in products:
        title = product.find("div", class_="title").text.replace(" ", "")
        title_text = product.find("div", class_="title").text.strip()
        price = product.find("div", class_="product-price").text.strip()
        link = 'http://eversonroyce.com' + product.find("a")['href']
        imagesoup = product.find('noscript')
        imageurl = imagesoup.find("img", class_="rimage__image")['src']
        image = 'https:' + imageurl
        store = 'eversonroyce'
        store_text = 'Everson Royce'
        type = 'white'
        type_text = 'White'
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
for x in er_sparkling_urls:
    soup = BeautifulSoup(requests.get(x).content, 'html.parser')
    products = soup.find_all("div", class_="prod-block")
    for product in products:
        title = product.find("div", class_="title").text.replace(" ", "")
        title_text = product.find("div", class_="title").text.strip()
        price = product.find("div", class_="product-price").text.strip()
        link = 'http://eversonroyce.com' + product.find("a")['href']
        imagesoup = product.find('noscript')
        imageurl = imagesoup.find("img", class_="rimage__image")['src']
        image = 'https:' + imageurl
        store = 'eversonroyce'
        store_text = 'Everson Royce'
        type = 'sparkling'
        type_text = 'Sparkling'
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

# writes the wine data to the json file
with open("data.json", "w") as writeJSON:
    json.dump({'wine': wines}, writeJSON, ensure_ascii=False)

# prints data to terminal (only needed for troubleshooting)
# print(json.dumps(wines, indent=4))
print('success!')
