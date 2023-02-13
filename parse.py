import re
import json
import requests
from bs4 import BeautifulSoup

# sets up empty list to store wine data
wines = []



# list of vinovore eagle rock urls to parse
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
vver_rose_urls = [
"https://vinovoreeaglerock.com/collections/rose",
"https://vinovoreeaglerock.com/collections/rose?page=2",
"https://vinovoreeaglerock.com/collections/rose?page=3",
"https://vinovoreeaglerock.com/collections/rose?page=4"
]
vver_orange_urls = [
"https://vinovoreeaglerock.com/collections/orange",
"https://vinovoreeaglerock.com/collections/orange?page=2",
"https://vinovoreeaglerock.com/collections/orange?page=3",
"https://vinovoreeaglerock.com/collections/orange?page=4"
]
vver_sparkling_urls = [
"https://vinovoreeaglerock.com/collections/sparkling",
"https://vinovoreeaglerock.com/collections/sparkling?page=2",
"https://vinovoreeaglerock.com/collections/sparkling?page=3",
"https://vinovoreeaglerock.com/collections/sparkling?page=4",
"https://vinovoreeaglerock.com/collections/sparkling?page=5",
"https://vinovoreeaglerock.com/collections/sparkling?page=6",
]


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
      imagecheck = imagesoup.find("img", class_="grid-product__image")
      if imagecheck is not None:
        imageurl = imagesoup.find("img", class_="grid-product__image")['src']
        image = 'https:' + imageurl
      else:
        image = 'assets/placeholder.png'
      if 'lewandowski' in title.lower():
        maker = 'Ruth Lewandowski'
      elif 'amevive' in title.lower():
        maker = 'Amevive'
      elif 'amplify' in title.lower():
        maker = 'Amplify'
      elif 'broc' in title.lower():
        maker = 'Broc Cellars'
      elif 'cirelli' in title.lower():
        maker = 'Cirelli'
      elif 'dueterre' in title.lower():
        maker = 'Due Terre'
      elif 'folkmachine' in title.lower():
        maker = 'Folk Machine'
      elif 'furlani' in title.lower():
        maker = 'Furlani'
      elif 'gentle folk' in title.lower():
        maker = 'Gentle Folk'
      elif 'goodboywine' in title.lower():
        maker = 'Good Boy Wine'
      elif 'gutoggau' in title.lower():
        maker = 'Gut Oggau'
      elif 'kopptisch' in title.lower():
        maker = 'Kopptisch'
      elif 'koehnen' in title.lower():
        maker = 'Koehnen'
      elif 'lasjaras' in title.lower():
        maker = 'Las Jaras'
      elif 'marigny' in title.lower():
        maker = 'Marigny'
      elif 'marthastoumen' in title.lower():
        maker = 'Martha Stoumen'
      elif 'meinklang' in title.lower():
        maker = 'Meinklang'
      elif 'nestarec' in title.lower():
        maker = 'Nestarec'
      elif 'oldwestminster' in title.lower():
        maker = 'Old Westminster'
      elif 'purity' in title.lower():
        maker = 'Purity'
      elif 'stagiaire' in title.lower():
        maker = 'Stagiaire'
      elif 'scottyboy' in title.lower():
        maker = 'Scotty Boy'
      elif 'scotty-boy' in title.lower():
        maker = 'Scotty Boy'
      elif 'stagiaire' in title.lower():
        maker = 'Stagiaire'
      elif 'subjecttochange' in title.lower():
        maker = 'Subject to Change'
      elif 'swick' in title.lower():
        maker = 'Swick'
      elif 'wavywines' in title.lower():
        maker = 'Wavy Wines'
      elif 'wildarcfarm' in title.lower():
        maker = 'Wild Arc Farm'
      elif 'wonderwerk' in title.lower():
        maker = 'Wonderwerk'
      else:
        maker ='undefined'
      wines.append({
        'Title': title,
        'Title_text': title_text,
        'Maker': maker,
        'Price': price,
        'Link': link,
        'Image': image,
        'Type': 'orange',
        'Type_text': 'Orange',
        'Store': 'vinovoreeaglerock',
        'Store_text': 'Vinovore Eagle Rock',
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
      imagecheck = imagesoup.find("img", class_="grid-product__image")
      if imagecheck is not None:
        imageurl = imagesoup.find("img", class_="grid-product__image")['src']
        image = 'https:' + imageurl
      else:
        image = 'assets/placeholder.png'
      if 'lewandowski' in title.lower():
        maker = 'Ruth Lewandowski'
      elif 'amevive' in title.lower():
        maker = 'Amevive'
      elif 'amplify' in title.lower():
        maker = 'Amplify'
      elif 'broc' in title.lower():
        maker = 'Broc Cellars'
      elif 'cirelli' in title.lower():
        maker = 'Cirelli'
      elif 'dueterre' in title.lower():
        maker = 'Due Terre'
      elif 'folkmachine' in title.lower():
        maker = 'Folk Machine'
      elif 'furlani' in title.lower():
        maker = 'Furlani'
      elif 'gentle folk' in title.lower():
        maker = 'Gentle Folk'
      elif 'goodboywine' in title.lower():
        maker = 'Good Boy Wine'
      elif 'gutoggau' in title.lower():
        maker = 'Gut Oggau'
      elif 'kopptisch' in title.lower():
        maker = 'Kopptisch'
      elif 'koehnen' in title.lower():
        maker = 'Koehnen'
      elif 'lasjaras' in title.lower():
        maker = 'Las Jaras'
      elif 'marigny' in title.lower():
        maker = 'Marigny'
      elif 'marthastoumen' in title.lower():
        maker = 'Martha Stoumen'
      elif 'meinklang' in title.lower():
        maker = 'Meinklang'
      elif 'nestarec' in title.lower():
        maker = 'Nestarec'
      elif 'oldwestminster' in title.lower():
        maker = 'Old Westminster'
      elif 'purity' in title.lower():
        maker = 'Purity'
      elif 'stagiaire' in title.lower():
        maker = 'Stagiaire'
      elif 'scottyboy' in title.lower():
        maker = 'Scotty Boy'
      elif 'scotty-boy' in title.lower():
        maker = 'Scotty Boy'
      elif 'stagiaire' in title.lower():
        maker = 'Stagiaire'
      elif 'subjecttochange' in title.lower():
        maker = 'Subject to Change'
      elif 'swick' in title.lower():
        maker = 'Swick'
      elif 'wavywines' in title.lower():
        maker = 'Wavy Wines'
      elif 'wildarcfarm' in title.lower():
        maker = 'Wild Arc Farm'
      elif 'wonderwerk' in title.lower():
        maker = 'Wonderwerk'
      else:
        maker ='undefined'
      wines.append({
        'Title': title,
        'Title_text': title_text,
        'Maker': maker,
        'Price': price,
        'Link': link,
        'Image': image,
        'Type': 'rose',
        'Type_text': 'Ros&#233;',
        'Store': 'vinovoreeaglerock',
        'Store_text': 'Vinovore Eagle Rock',
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
      imagecheck = imagesoup.find("img", class_="grid-product__image")
      if imagecheck is not None:
        imageurl = imagesoup.find("img", class_="grid-product__image")['src']
        image = 'https:' + imageurl
      else:
        image = 'assets/placeholder.png'
      if 'lewandowski' in title.lower():
        maker = 'Ruth Lewandowski'
      elif 'amevive' in title.lower():
        maker = 'Amevive'
      elif 'amplify' in title.lower():
        maker = 'Amplify'
      elif 'broc' in title.lower():
        maker = 'Broc Cellars'
      elif 'cirelli' in title.lower():
        maker = 'Cirelli'
      elif 'dueterre' in title.lower():
        maker = 'Due Terre'
      elif 'folkmachine' in title.lower():
        maker = 'Folk Machine'
      elif 'furlani' in title.lower():
        maker = 'Furlani'
      elif 'gentle folk' in title.lower():
        maker = 'Gentle Folk'
      elif 'goodboywine' in title.lower():
        maker = 'Good Boy Wine'
      elif 'gutoggau' in title.lower():
        maker = 'Gut Oggau'
      elif 'kopptisch' in title.lower():
        maker = 'Kopptisch'
      elif 'koehnen' in title.lower():
        maker = 'Koehnen'
      elif 'lasjaras' in title.lower():
        maker = 'Las Jaras'
      elif 'marigny' in title.lower():
        maker = 'Marigny'
      elif 'marthastoumen' in title.lower():
        maker = 'Martha Stoumen'
      elif 'meinklang' in title.lower():
        maker = 'Meinklang'
      elif 'nestarec' in title.lower():
        maker = 'Nestarec'
      elif 'oldwestminster' in title.lower():
        maker = 'Old Westminster'
      elif 'purity' in title.lower():
        maker = 'Purity'
      elif 'stagiaire' in title.lower():
        maker = 'Stagiaire'
      elif 'scottyboy' in title.lower():
        maker = 'Scotty Boy'
      elif 'scotty-boy' in title.lower():
        maker = 'Scotty Boy'
      elif 'stagiaire' in title.lower():
        maker = 'Stagiaire'
      elif 'subjecttochange' in title.lower():
        maker = 'Subject to Change'
      elif 'swick' in title.lower():
        maker = 'Swick'
      elif 'wavywines' in title.lower():
        maker = 'Wavy Wines'
      elif 'wildarcfarm' in title.lower():
        maker = 'Wild Arc Farm'
      elif 'wonderwerk' in title.lower():
        maker = 'Wonderwerk'
      else:
        maker ='undefined'
      wines.append({
        'Title': title,
        'Title_text': title_text,
        'Maker': maker,
        'Price': price,
        'Link': link,
        'Image': image,
        'Type': 'red',
        'Type_text': 'Red',
        'Store': 'vinovoreeaglerock',
        'Store_text': 'Vinovore Eagle Rock',
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
      imagecheck = imagesoup.find("img", class_="grid-product__image")
      if imagecheck is not None:
        imageurl = imagesoup.find("img", class_="grid-product__image")['src']
        image = 'https:' + imageurl
      else:
        image = 'assets/placeholder.png'
      if 'lewandowski' in title.lower():
        maker = 'Ruth Lewandowski'
      elif 'amevive' in title.lower():
        maker = 'Amevive'
      elif 'amplify' in title.lower():
        maker = 'Amplify'
      elif 'broc' in title.lower():
        maker = 'Broc Cellars'
      elif 'cirelli' in title.lower():
        maker = 'Cirelli'
      elif 'dueterre' in title.lower():
        maker = 'Due Terre'
      elif 'folkmachine' in title.lower():
        maker = 'Folk Machine'
      elif 'furlani' in title.lower():
        maker = 'Furlani'
      elif 'gentle folk' in title.lower():
        maker = 'Gentle Folk'
      elif 'goodboywine' in title.lower():
        maker = 'Good Boy Wine'
      elif 'gutoggau' in title.lower():
        maker = 'Gut Oggau'
      elif 'kopptisch' in title.lower():
        maker = 'Kopptisch'
      elif 'koehnen' in title.lower():
        maker = 'Koehnen'
      elif 'lasjaras' in title.lower():
        maker = 'Las Jaras'
      elif 'marigny' in title.lower():
        maker = 'Marigny'
      elif 'marthastoumen' in title.lower():
        maker = 'Martha Stoumen'
      elif 'meinklang' in title.lower():
        maker = 'Meinklang'
      elif 'nestarec' in title.lower():
        maker = 'Nestarec'
      elif 'oldwestminster' in title.lower():
        maker = 'Old Westminster'
      elif 'purity' in title.lower():
        maker = 'Purity'
      elif 'stagiaire' in title.lower():
        maker = 'Stagiaire'
      elif 'scottyboy' in title.lower():
        maker = 'Scotty Boy'
      elif 'scotty-boy' in title.lower():
        maker = 'Scotty Boy'
      elif 'stagiaire' in title.lower():
        maker = 'Stagiaire'
      elif 'subjecttochange' in title.lower():
        maker = 'Subject to Change'
      elif 'swick' in title.lower():
        maker = 'Swick'
      elif 'wavywines' in title.lower():
        maker = 'Wavy Wines'
      elif 'wildarcfarm' in title.lower():
        maker = 'Wild Arc Farm'
      elif 'wonderwerk' in title.lower():
        maker = 'Wonderwerk'
      else:
        maker ='undefined'
      wines.append({
        'Title': title,
        'Title_text': title_text,
        'Maker': maker,
        'Price': price,
        'Link': link,
        'Image': image,
        'Type': 'white',
        'Type_text': 'White',
        'Store': 'vinovoreeaglerock',
        'Store_text': 'Vinovore Eagle Rock',
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
      imagecheck = imagesoup.find("img", class_="grid-product__image")
      if imagecheck is not None:
        imageurl = imagesoup.find("img", class_="grid-product__image")['src']
        image = 'https:' + imageurl
      else:
        image = 'assets/placeholder.png'
      if 'lewandowski' in title.lower():
        maker = 'Ruth Lewandowski'
      elif 'amevive' in title.lower():
        maker = 'Amevive'
      elif 'amplify' in title.lower():
        maker = 'Amplify'
      elif 'broc' in title.lower():
        maker = 'Broc Cellars'
      elif 'cirelli' in title.lower():
        maker = 'Cirelli'
      elif 'dueterre' in title.lower():
        maker = 'Due Terre'
      elif 'folkmachine' in title.lower():
        maker = 'Folk Machine'
      elif 'furlani' in title.lower():
        maker = 'Furlani'
      elif 'gentle folk' in title.lower():
        maker = 'Gentle Folk'
      elif 'goodboywine' in title.lower():
        maker = 'Good Boy Wine'
      elif 'gutoggau' in title.lower():
        maker = 'Gut Oggau'
      elif 'kopptisch' in title.lower():
        maker = 'Kopptisch'
      elif 'koehnen' in title.lower():
        maker = 'Koehnen'
      elif 'lasjaras' in title.lower():
        maker = 'Las Jaras'
      elif 'marigny' in title.lower():
        maker = 'Marigny'
      elif 'marthastoumen' in title.lower():
        maker = 'Martha Stoumen'
      elif 'meinklang' in title.lower():
        maker = 'Meinklang'
      elif 'nestarec' in title.lower():
        maker = 'Nestarec'
      elif 'oldwestminster' in title.lower():
        maker = 'Old Westminster'
      elif 'purity' in title.lower():
        maker = 'Purity'
      elif 'stagiaire' in title.lower():
        maker = 'Stagiaire'
      elif 'scottyboy' in title.lower():
        maker = 'Scotty Boy'
      elif 'scotty-boy' in title.lower():
        maker = 'Scotty Boy'
      elif 'stagiaire' in title.lower():
        maker = 'Stagiaire'
      elif 'subjecttochange' in title.lower():
        maker = 'Subject to Change'
      elif 'swick' in title.lower():
        maker = 'Swick'
      elif 'wavywines' in title.lower():
        maker = 'Wavy Wines'
      elif 'wildarcfarm' in title.lower():
        maker = 'Wild Arc Farm'
      elif 'wonderwerk' in title.lower():
        maker = 'Wonderwerk'
      else:
        maker ='undefined'
      wines.append({
        'Title': title,
        'Title_text': title_text,
        'Maker': maker,
        'Price': price,
        'Link': link,
        'Image': image,
        'Type': 'sparkling',
        'Type_text': 'Sparkling',
        'Store': 'vinovoreeaglerock',
        'Store_text': 'Vinovore Eagle Rock',
      })



# list of highland park wine urls to parse
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
hlp_rose_urls = [
"https://www.highlandparkwine.com/collections/rose",
"https://www.highlandparkwine.com/collections/rose?page=2",
"https://www.highlandparkwine.com/collections/rose?page=3",
"https://www.highlandparkwine.com/collections/rose?page=4",
"https://www.highlandparkwine.com/collections/rose?page=5"
]
hlp_orange_urls = [
"https://www.highlandparkwine.com/collections/orange-wine",
"https://www.highlandparkwine.com/collections/orange-wine?page=2",
"https://www.highlandparkwine.com/collections/orange-wine?page=3",
"https://www.highlandparkwine.com/collections/orange-wine?page=4"
]
hlp_sparkling_urls = [
"https://www.highlandparkwine.com/collections/sparkling-wine",
"https://www.highlandparkwine.com/collections/sparkling-wine?page=2",
"https://www.highlandparkwine.com/collections/sparkling-wine?page=3",
"https://www.highlandparkwine.com/collections/sparkling-wine?page=4",
"https://www.highlandparkwine.com/collections/sparkling-wine?page=5",
"https://www.highlandparkwine.com/collections/sparkling-wine?page=6"
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
		imagecheck = imagesoup.find("img", class_="rimage__image")
		if imagecheck is not None:
			imageurl = imagesoup.find("img", class_="rimage__image")['src']
			image = 'https:' + imageurl
		else:
			image = 'assets/placeholder.png'
		if 'lewandowski' in title.lower():
        maker = 'Ruth Lewandowski'
		elif 'amevive' in title.lower():
			maker = 'Amevive'
		elif 'amplify' in title.lower():
			maker = 'Amplify'
		elif 'broc' in title.lower():
			maker = 'Broc Cellars'
		elif 'cirelli' in title.lower():
			maker = 'Cirelli'
		elif 'dueterre' in title.lower():
			maker = 'Due Terre'
		elif 'folkmachine' in title.lower():
			maker = 'Folk Machine'
		elif 'furlani' in title.lower():
			maker = 'Furlani'
		elif 'gentle folk' in title.lower():
			maker = 'Gentle Folk'
		elif 'goodboywine' in title.lower():
			maker = 'Good Boy Wine'
		elif 'gutoggau' in title.lower():
			maker = 'Gut Oggau'
		elif 'kopptisch' in title.lower():
			maker = 'Kopptisch'
		elif 'koehnen' in title.lower():
			maker = 'Koehnen'
		elif 'lasjaras' in title.lower():
			maker = 'Las Jaras'
		elif 'marigny' in title.lower():
			maker = 'Marigny'
		elif 'marthastoumen' in title.lower():
			maker = 'Martha Stoumen'
		elif 'meinklang' in title.lower():
			maker = 'Meinklang'
		elif 'nestarec' in title.lower():
			maker = 'Nestarec'
		elif 'oldwestminster' in title.lower():
			maker = 'Old Westminster'
		elif 'purity' in title.lower():
			maker = 'Purity'
		elif 'stagiaire' in title.lower():
			maker = 'Stagiaire'
		elif 'scottyboy' in title.lower():
			maker = 'Scotty Boy'
		elif 'scotty-boy' in title.lower():
			maker = 'Scotty Boy'
		elif 'stagiaire' in title.lower():
			maker = 'Stagiaire'
		elif 'subjecttochange' in title.lower():
			maker = 'Subject to Change'
		elif 'swick' in title.lower():
			maker = 'Swick'
		elif 'wavywines' in title.lower():
			maker = 'Wavy Wines'
		elif 'wildarcfarm' in title.lower():
			maker = 'Wild Arc Farm'
		elif 'wonderwerk' in title.lower():
			maker = 'Wonderwerk'
		else:
			maker ='undefined'
		wines.append({
			'Title': title,
			'Title_text': title_text,
			'Maker': maker,
			'Price': price,
			'Link': link,
			'Image': image,
			'Type': '',
			'Type_text': '',
			'Store': 'highlandpark',
			'Store_text': 'Highland Park Wine',
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
		imagecheck = imagesoup.find("img", class_="rimage__image")
		if imagecheck is not None:
			imageurl = imagesoup.find("img", class_="rimage__image")['src']
			image = 'https:' + imageurl
		else:
			image = 'assets/placeholder.png'
		if 'lewandowski' in title.lower():
        maker = 'Ruth Lewandowski'
		elif 'amevive' in title.lower():
			maker = 'Amevive'
		elif 'amplify' in title.lower():
			maker = 'Amplify'
		elif 'broc' in title.lower():
			maker = 'Broc Cellars'
		elif 'cirelli' in title.lower():
			maker = 'Cirelli'
		elif 'dueterre' in title.lower():
			maker = 'Due Terre'
		elif 'folkmachine' in title.lower():
			maker = 'Folk Machine'
		elif 'furlani' in title.lower():
			maker = 'Furlani'
		elif 'gentle folk' in title.lower():
			maker = 'Gentle Folk'
		elif 'goodboywine' in title.lower():
			maker = 'Good Boy Wine'
		elif 'gutoggau' in title.lower():
			maker = 'Gut Oggau'
		elif 'kopptisch' in title.lower():
			maker = 'Kopptisch'
		elif 'koehnen' in title.lower():
			maker = 'Koehnen'
		elif 'lasjaras' in title.lower():
			maker = 'Las Jaras'
		elif 'marigny' in title.lower():
			maker = 'Marigny'
		elif 'marthastoumen' in title.lower():
			maker = 'Martha Stoumen'
		elif 'meinklang' in title.lower():
			maker = 'Meinklang'
		elif 'nestarec' in title.lower():
			maker = 'Nestarec'
		elif 'oldwestminster' in title.lower():
			maker = 'Old Westminster'
		elif 'purity' in title.lower():
			maker = 'Purity'
		elif 'stagiaire' in title.lower():
			maker = 'Stagiaire'
		elif 'scottyboy' in title.lower():
			maker = 'Scotty Boy'
		elif 'scotty-boy' in title.lower():
			maker = 'Scotty Boy'
		elif 'stagiaire' in title.lower():
			maker = 'Stagiaire'
		elif 'subjecttochange' in title.lower():
			maker = 'Subject to Change'
		elif 'swick' in title.lower():
			maker = 'Swick'
		elif 'wavywines' in title.lower():
			maker = 'Wavy Wines'
		elif 'wildarcfarm' in title.lower():
			maker = 'Wild Arc Farm'
		elif 'wonderwerk' in title.lower():
			maker = 'Wonderwerk'
		else:
			maker ='undefined'
		wines.append({
			'Title': title,
			'Title_text': title_text,
			'Maker': maker,
			'Price': price,
			'Link': link,
			'Image': image,
			'Type': '',
			'Type_text': '',
			'Store': 'highlandpark',
			'Store_text': 'Highland Park Wine',
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
		imagecheck = imagesoup.find("img", class_="rimage__image")
		if imagecheck is not None:
			imageurl = imagesoup.find("img", class_="rimage__image")['src']
			image = 'https:' + imageurl
		else:
			image = 'assets/placeholder.png'
		if 'lewandowski' in title.lower():
        maker = 'Ruth Lewandowski'
		elif 'amevive' in title.lower():
			maker = 'Amevive'
		elif 'amplify' in title.lower():
			maker = 'Amplify'
		elif 'broc' in title.lower():
			maker = 'Broc Cellars'
		elif 'cirelli' in title.lower():
			maker = 'Cirelli'
		elif 'dueterre' in title.lower():
			maker = 'Due Terre'
		elif 'folkmachine' in title.lower():
			maker = 'Folk Machine'
		elif 'furlani' in title.lower():
			maker = 'Furlani'
		elif 'gentle folk' in title.lower():
			maker = 'Gentle Folk'
		elif 'goodboywine' in title.lower():
			maker = 'Good Boy Wine'
		elif 'gutoggau' in title.lower():
			maker = 'Gut Oggau'
		elif 'kopptisch' in title.lower():
			maker = 'Kopptisch'
		elif 'koehnen' in title.lower():
			maker = 'Koehnen'
		elif 'lasjaras' in title.lower():
			maker = 'Las Jaras'
		elif 'marigny' in title.lower():
			maker = 'Marigny'
		elif 'marthastoumen' in title.lower():
			maker = 'Martha Stoumen'
		elif 'meinklang' in title.lower():
			maker = 'Meinklang'
		elif 'nestarec' in title.lower():
			maker = 'Nestarec'
		elif 'oldwestminster' in title.lower():
			maker = 'Old Westminster'
		elif 'purity' in title.lower():
			maker = 'Purity'
		elif 'stagiaire' in title.lower():
			maker = 'Stagiaire'
		elif 'scottyboy' in title.lower():
			maker = 'Scotty Boy'
		elif 'scotty-boy' in title.lower():
			maker = 'Scotty Boy'
		elif 'stagiaire' in title.lower():
			maker = 'Stagiaire'
		elif 'subjecttochange' in title.lower():
			maker = 'Subject to Change'
		elif 'swick' in title.lower():
			maker = 'Swick'
		elif 'wavywines' in title.lower():
			maker = 'Wavy Wines'
		elif 'wildarcfarm' in title.lower():
			maker = 'Wild Arc Farm'
		elif 'wonderwerk' in title.lower():
			maker = 'Wonderwerk'
		else:
			maker ='undefined'
		wines.append({
			'Title': title,
			'Title_text': title_text,
			'Maker': maker,
			'Price': price,
			'Link': link,
			'Image': image,
			'Type': '',
			'Type_text': '',
			'Store': 'highlandpark',
			'Store_text': 'Highland Park Wine',
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
		imagecheck = imagesoup.find("img", class_="rimage__image")
		if imagecheck is not None:
			imageurl = imagesoup.find("img", class_="rimage__image")['src']
			image = 'https:' + imageurl
		else:
			image = 'assets/placeholder.png'
		if 'lewandowski' in title.lower():
        maker = 'Ruth Lewandowski'
		elif 'amevive' in title.lower():
			maker = 'Amevive'
		elif 'amplify' in title.lower():
			maker = 'Amplify'
		elif 'broc' in title.lower():
			maker = 'Broc Cellars'
		elif 'cirelli' in title.lower():
			maker = 'Cirelli'
		elif 'dueterre' in title.lower():
			maker = 'Due Terre'
		elif 'folkmachine' in title.lower():
			maker = 'Folk Machine'
		elif 'furlani' in title.lower():
			maker = 'Furlani'
		elif 'gentle folk' in title.lower():
			maker = 'Gentle Folk'
		elif 'goodboywine' in title.lower():
			maker = 'Good Boy Wine'
		elif 'gutoggau' in title.lower():
			maker = 'Gut Oggau'
		elif 'kopptisch' in title.lower():
			maker = 'Kopptisch'
		elif 'koehnen' in title.lower():
			maker = 'Koehnen'
		elif 'lasjaras' in title.lower():
			maker = 'Las Jaras'
		elif 'marigny' in title.lower():
			maker = 'Marigny'
		elif 'marthastoumen' in title.lower():
			maker = 'Martha Stoumen'
		elif 'meinklang' in title.lower():
			maker = 'Meinklang'
		elif 'nestarec' in title.lower():
			maker = 'Nestarec'
		elif 'oldwestminster' in title.lower():
			maker = 'Old Westminster'
		elif 'purity' in title.lower():
			maker = 'Purity'
		elif 'stagiaire' in title.lower():
			maker = 'Stagiaire'
		elif 'scottyboy' in title.lower():
			maker = 'Scotty Boy'
		elif 'scotty-boy' in title.lower():
			maker = 'Scotty Boy'
		elif 'stagiaire' in title.lower():
			maker = 'Stagiaire'
		elif 'subjecttochange' in title.lower():
			maker = 'Subject to Change'
		elif 'swick' in title.lower():
			maker = 'Swick'
		elif 'wavywines' in title.lower():
			maker = 'Wavy Wines'
		elif 'wildarcfarm' in title.lower():
			maker = 'Wild Arc Farm'
		elif 'wonderwerk' in title.lower():
			maker = 'Wonderwerk'
		else:
			maker ='undefined'
		wines.append({
			'Title': title,
			'Title_text': title_text,
			'Maker': maker,
			'Price': price,
			'Link': link,
			'Image': image,
			'Type': '',
			'Type_text': '',
			'Store': 'highlandpark',
			'Store_text': 'Highland Park Wine',
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
		imagecheck = imagesoup.find("img", class_="rimage__image")
		if imagecheck is not None:
			imageurl = imagesoup.find("img", class_="rimage__image")['src']
			image = 'https:' + imageurl
		else:
			image = 'assets/placeholder.png'
		if 'lewandowski' in title.lower():
        maker = 'Ruth Lewandowski'
		elif 'amevive' in title.lower():
			maker = 'Amevive'
		elif 'amplify' in title.lower():
			maker = 'Amplify'
		elif 'broc' in title.lower():
			maker = 'Broc Cellars'
		elif 'cirelli' in title.lower():
			maker = 'Cirelli'
		elif 'dueterre' in title.lower():
			maker = 'Due Terre'
		elif 'folkmachine' in title.lower():
			maker = 'Folk Machine'
		elif 'furlani' in title.lower():
			maker = 'Furlani'
		elif 'gentle folk' in title.lower():
			maker = 'Gentle Folk'
		elif 'goodboywine' in title.lower():
			maker = 'Good Boy Wine'
		elif 'gutoggau' in title.lower():
			maker = 'Gut Oggau'
		elif 'kopptisch' in title.lower():
			maker = 'Kopptisch'
		elif 'koehnen' in title.lower():
			maker = 'Koehnen'
		elif 'lasjaras' in title.lower():
			maker = 'Las Jaras'
		elif 'marigny' in title.lower():
			maker = 'Marigny'
		elif 'marthastoumen' in title.lower():
			maker = 'Martha Stoumen'
		elif 'meinklang' in title.lower():
			maker = 'Meinklang'
		elif 'nestarec' in title.lower():
			maker = 'Nestarec'
		elif 'oldwestminster' in title.lower():
			maker = 'Old Westminster'
		elif 'purity' in title.lower():
			maker = 'Purity'
		elif 'stagiaire' in title.lower():
			maker = 'Stagiaire'
		elif 'scottyboy' in title.lower():
			maker = 'Scotty Boy'
		elif 'scotty-boy' in title.lower():
			maker = 'Scotty Boy'
		elif 'stagiaire' in title.lower():
			maker = 'Stagiaire'
		elif 'subjecttochange' in title.lower():
			maker = 'Subject to Change'
		elif 'swick' in title.lower():
			maker = 'Swick'
		elif 'wavywines' in title.lower():
			maker = 'Wavy Wines'
		elif 'wildarcfarm' in title.lower():
			maker = 'Wild Arc Farm'
		elif 'wonderwerk' in title.lower():
			maker = 'Wonderwerk'
		else:
			maker ='undefined'
		wines.append({
			'Title': title,
			'Title_text': title_text,
			'Maker': maker,
			'Price': price,
			'Link': link,
			'Image': image,
			'Type': '',
			'Type_text': '',
			'Store': 'highlandpark',
			'Store_text': 'Highland Park Wine',
		})






# list of heavens market urls to parse
heavens_red_urls = [
"https://www.heavensmarketla.com/collections/red",
"https://www.heavensmarketla.com/collections/red?page=2",
"https://www.heavensmarketla.com/collections/red?page=3",
"https://www.heavensmarketla.com/collections/red?page=4",
"https://www.heavensmarketla.com/collections/red?page=5",
]
heavens_white_urls = [
"https://www.heavensmarketla.com/collections/white",
"https://www.heavensmarketla.com/collections/white?page=2",
"https://www.heavensmarketla.com/collections/white?page=3",
"https://www.heavensmarketla.com/collections/white?page=4",
]
heavens_rose_urls = [
"https://www.heavensmarketla.com/collections/rose",
"https://www.heavensmarketla.com/collections/rose?page=2",
]
heavens_orange_urls = [
"https://www.heavensmarketla.com/collections/skin-contact",
"https://www.heavensmarketla.com/collections/skin-contact?page=2",
"https://www.heavensmarketla.com/collections/skin-contact?page=3",
"https://www.heavensmarketla.com/collections/skin-contact?page=4",
]
heavens_sparkling_urls = [
"https://www.heavensmarketla.com/collections/sparkling",
"https://www.heavensmarketla.com/collections/sparkling?page=2",
"https://www.heavensmarketla.com/collections/sparkling?page=3",
"https://www.heavensmarketla.com/collections/sparkling?page=4",
]


# code for parsing heavens market urls
for x in heavens_orange_urls:
	soup = BeautifulSoup(requests.get(x).content, 'html.parser')
	products = soup.find_all("li", class_="grid__item")
	for product in products:
		title = product.find("span", class_="visually-hidden").text.replace(" ", "")
		title_text = product.find("span", class_="visually-hidden").text.strip()
		price = product.find("span", class_="price-item").text.strip()
		link = 'http://heavensmarketla.com' + product.find("a", class_="grid-view-item__link")['href']
		imagesoup = product.find('noscript')
		imagecheck = imagesoup.find("img", class_="grid-view-item__image")
		if imagecheck is not None:
			imageurl = imagesoup.find("img", class_="grid-view-item__image")['src']
			image = 'https:' + imageurl
		else:
			image = 'assets/placeholder.png'
		store = 'heavensmarket'
		store_text = 'Heaven&#39;s Market'
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
for x in heavens_rose_urls:
	soup = BeautifulSoup(requests.get(x).content, 'html.parser')
	products = soup.find_all("li", class_="grid__item")
	for product in products:
		title = product.find("span", class_="visually-hidden").text.replace(" ", "")
		title_text = product.find("span", class_="visually-hidden").text.strip()
		price = product.find("span", class_="price-item").text.strip()
		link = 'http://heavensmarketla.com' + product.find("a", class_="grid-view-item__link")['href']
		imagesoup = product.find('noscript')
		imagecheck = imagesoup.find("img", class_="grid-view-item__image")
		if imagecheck is not None:
			imageurl = imagesoup.find("img", class_="grid-view-item__image")['src']
			image = 'https:' + imageurl
		else:
			image = 'assets/placeholder.png'
		store = 'heavensmarket'
		store_text = 'Heaven&#39;s Market'
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
for x in heavens_red_urls:
	soup = BeautifulSoup(requests.get(x).content, 'html.parser')
	products = soup.find_all("li", class_="grid__item")
	for product in products:
		title = product.find("span", class_="visually-hidden").text.replace(" ", "")
		title_text = product.find("span", class_="visually-hidden").text.strip()
		price = product.find("span", class_="price-item").text.strip()
		link = 'http://heavensmarketla.com' + product.find("a", class_="grid-view-item__link")['href']
		imagesoup = product.find('noscript')
		imagecheck = imagesoup.find("img", class_="grid-view-item__image")
		if imagecheck is not None:
			imageurl = imagesoup.find("img", class_="grid-view-item__image")['src']
			image = 'https:' + imageurl
		else:
			image = 'assets/placeholder.png'
		store = 'heavensmarket'
		store_text = 'Heaven&#39;s Market'
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
for x in heavens_white_urls:
	soup = BeautifulSoup(requests.get(x).content, 'html.parser')
	products = soup.find_all("li", class_="grid__item")
	for product in products:
		title = product.find("span", class_="visually-hidden").text.replace(" ", "")
		title_text = product.find("span", class_="visually-hidden").text.strip()
		price = product.find("span", class_="price-item").text.strip()
		link = 'http://heavensmarketla.com' + product.find("a", class_="grid-view-item__link")['href']
		imagesoup = product.find('noscript')
		imagecheck = imagesoup.find("img", class_="grid-view-item__image")
		if imagecheck is not None:
			imageurl = imagesoup.find("img", class_="grid-view-item__image")['src']
			image = 'https:' + imageurl
		else:
			image = 'assets/placeholder.png'
		store = 'heavensmarket'
		store_text = 'Heaven&#39;s Market'
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
for x in heavens_sparkling_urls:
	soup = BeautifulSoup(requests.get(x).content, 'html.parser')
	products = soup.find_all("li", class_="grid__item")
	for product in products:
		title = product.find("span", class_="visually-hidden").text.replace(" ", "")
		title_text = product.find("span", class_="visually-hidden").text.strip()
		price = product.find("span", class_="price-item").text.strip()
		link = 'http://heavensmarketla.com' + product.find("a", class_="grid-view-item__link")['href']
		imagesoup = product.find('noscript')
		imagecheck = imagesoup.find("img", class_="grid-view-item__image")
		if imagecheck is not None:
			imageurl = imagesoup.find("img", class_="grid-view-item__image")['src']
			image = 'https:' + imageurl
		else:
			image = 'assets/placeholder.png'
		store = 'heavensmarket'
		store_text = 'Heaven&#39;s Market'
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
for x in heavens_orange_urls:
	soup = BeautifulSoup(requests.get(x).content, 'html.parser')
	products = soup.find_all("li", class_="grid__item")
	for product in products:
		title = product.find("span", class_="visually-hidden").text.replace(" ", "")
		title_text = product.find("span", class_="visually-hidden").text.strip()
		price = product.find("span", class_="price-item").text.strip()
		link = 'http://heavensmarketla.com' + product.find("a", class_="grid-view-item__link")['href']
		imagesoup = product.find('noscript')
		imagecheck = imagesoup.find("img", class_="grid-view-item__image")
		if imagecheck is not None:
			imageurl = imagesoup.find("img", class_="grid-view-item__image")['src']
			image = 'https:' + imageurl
		else:
			image = 'assets/placeholder.png'
		store = 'heavensmarket'
		store_text = 'Heaven&#39;s Market'
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


		
		
# list of wine + eggs urls to parse
eggs_red_urls = [
"https://wineandeggs.com/collections/red-wine"
]
eggs_white_urls = [
"https://wineandeggs.com/collections/white-wine"
]
eggs_rose_urls = [
"https://wineandeggs.com/collections/wine-rose"
]
eggs_orange_urls = [
"https://wineandeggs.com/collections/skin-contact-wine"
]
eggs_sparkling_urls = [
"https://wineandeggs.com/collections/sparkling-wine"
]
eggs_co_fermented_urls = [
"https://wineandeggs.com/collections/co-fermented"
]
eggs_piquette_urls = [
"https://wineandeggs.com/collections/piquette-wine"
]	
	


# code for parsing wine + eggs urls
for x in eggs_co_fermented_urls:
	soup = BeautifulSoup(requests.get(x).content, 'html.parser')
	products = soup.find_all("div", class_="product-block")
	for product in products:
		title_name = product.find("h3", class_="product-block__title").text.strip()
		title_maker = product.find("div", class_="italicized-text").text.strip()
		title_text = title_maker + " " + title_name
		title = title_text.replace(" ", "")
		price = product.find("div", class_="product-block__price").text.strip()
		link = 'http://wineandeggs.com' + product.find("a")['href']
		imagesoup = product.find('noscript')
		imagecode = imagesoup.find("div", class_="product-block__image")['style']
		if imagecode is not None:
			imageurl = imagecode.strip("background-image:url('").strip("');")
			image = 'https:' + imageurl
		else:
			image = 'assets/placeholder.png'
		image = 'https:' + imageurl
		store = 'wineandeggs'
		store_text = 'Wine + Eggs'
		type = 'cofermented'
		type_text = 'Co-Fermented'
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
#			'Maker': title_maker,
		})
for x in eggs_orange_urls:
	soup = BeautifulSoup(requests.get(x).content, 'html.parser')
	products = soup.find_all("div", class_="product-block")
	for product in products:
		title_name = product.find("h3", class_="product-block__title").text.strip()
		title_maker = product.find("div", class_="italicized-text").text.strip()
		title_text = title_maker + " " + title_name
		title = title_text.replace(" ", "")
		price = product.find("div", class_="product-block__price").text.strip()
		link = 'http://wineandeggs.com' + product.find("a")['href']
		imagesoup = product.find('noscript')
		imagecode = imagesoup.find("div", class_="product-block__image")['style']
		if imagecode is not None:
			imageurl = imagecode.strip("background-image:url('").strip("');")
			image = 'https:' + imageurl
		else:
			image = 'assets/placeholder.png'
		image = 'https:' + imageurl
		store = 'wineandeggs'
		store_text = 'Wine + Eggs'
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
#			'Maker': title_maker,
		})
for x in eggs_rose_urls:
	soup = BeautifulSoup(requests.get(x).content, 'html.parser')
	products = soup.find_all("div", class_="product-block")
	for product in products:
		title_name = product.find("h3", class_="product-block__title").text.strip()
		title_maker = product.find("div", class_="italicized-text").text.strip()
		title_text = title_maker + " " + title_name
		title = title_text.replace(" ", "")
		price = product.find("div", class_="product-block__price").text.strip()
		link = 'http://wineandeggs.com' + product.find("a")['href']
		imagesoup = product.find('noscript')
		imagecode = imagesoup.find("div", class_="product-block__image")['style']
		if imagecode is not None:
			imageurl = imagecode.strip("background-image:url('").strip("');")
			image = 'https:' + imageurl
		else:
			image = 'assets/placeholder.png'
		image = 'https:' + imageurl
		store = 'wineandeggs'
		store_text = 'Wine + Eggs'
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
#			'Maker': title_maker,
		})
for x in eggs_red_urls:
	soup = BeautifulSoup(requests.get(x).content, 'html.parser')
	products = soup.find_all("div", class_="product-block")
	for product in products:
		title_name = product.find("h3", class_="product-block__title").text.strip()
		title_maker = product.find("div", class_="italicized-text").text.strip()
		title_text = title_maker + " " + title_name
		title = title_text.replace(" ", "")
		price = product.find("div", class_="product-block__price").text.strip()
		link = 'http://wineandeggs.com' + product.find("a")['href']
		imagesoup = product.find('noscript')
		imagecode = imagesoup.find("div", class_="product-block__image")['style']
		if imagecode is not None:
			imageurl = imagecode.strip("background-image:url('").strip("');")
			image = 'https:' + imageurl
		else:
			image = 'assets/placeholder.png'
		image = 'https:' + imageurl
		store = 'wineandeggs'
		store_text = 'Wine + Eggs'
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
#			'Maker': title_maker,
		})
for x in eggs_white_urls:
	soup = BeautifulSoup(requests.get(x).content, 'html.parser')
	products = soup.find_all("div", class_="product-block")
	for product in products:
		title_name = product.find("h3", class_="product-block__title").text.strip()
		title_maker = product.find("div", class_="italicized-text").text.strip()
		title_text = title_maker + " " + title_name
		title = title_text.replace(" ", "")
		price = product.find("div", class_="product-block__price").text.strip()
		link = 'http://wineandeggs.com' + product.find("a")['href']
		imagesoup = product.find('noscript')
		imagecode = imagesoup.find("div", class_="product-block__image")['style']
		if imagecode is not None:
			imageurl = imagecode.strip("background-image:url('").strip("');")
			image = 'https:' + imageurl
		else:
			image = 'assets/placeholder.png'
		image = 'https:' + imageurl
		store = 'wineandeggs'
		store_text = 'Wine + Eggs'
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
#			'Maker': title_maker,
		})
for x in eggs_sparkling_urls:
	soup = BeautifulSoup(requests.get(x).content, 'html.parser')
	products = soup.find_all("div", class_="product-block")
	for product in products:
		title_name = product.find("h3", class_="product-block__title").text.strip()
		title_maker = product.find("div", class_="italicized-text").text.strip()
		title_text = title_maker + " " + title_name
		title = title_text.replace(" ", "")
		price = product.find("div", class_="product-block__price").text.strip()
		link = 'http://wineandeggs.com' + product.find("a")['href']
		imagesoup = product.find('noscript')
		imagecode = imagesoup.find("div", class_="product-block__image")['style']
		if imagecode is not None:
			imageurl = imagecode.strip("background-image:url('").strip("');")
			image = 'https:' + imageurl
		else:
			image = 'assets/placeholder.png'
		image = 'https:' + imageurl
		store = 'wineandeggs'
		store_text = 'Wine + Eggs'
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
#			'Maker': title_maker,
		})
for x in eggs_piquette_urls:
	soup = BeautifulSoup(requests.get(x).content, 'html.parser')
	products = soup.find_all("div", class_="product-block")
	for product in products:
		title_name = product.find("h3", class_="product-block__title").text.strip()
		title_maker = product.find("div", class_="italicized-text").text.strip()
		title_text = title_maker + " " + title_name
		title = title_text.replace(" ", "")
		price = product.find("div", class_="product-block__price").text.strip()
		link = 'http://wineandeggs.com' + product.find("a")['href']
		imagesoup = product.find('noscript')
		imagecode = imagesoup.find("div", class_="product-block__image")['style']
		if imagecode is not None:
			imageurl = imagecode.strip("background-image:url('").strip("');")
			image = 'https:' + imageurl
		else:
			image = 'assets/placeholder.png'
		image = 'https:' + imageurl
		store = 'wineandeggs'
		store_text = 'Wine + Eggs'
		type = 'piquette'
		type_text = 'Piquette'
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
#			'Maker': title_maker,
		})
		
		
		




# list of silverlake wine urls to parse
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
sl_rose_urls = [
"https://silverlakewine.com/collections/rose",
"https://silverlakewine.com/collections/rose?page=2",
"https://silverlakewine.com/collections/rose?page=3",
"https://silverlakewine.com/collections/rose?page=4",
"https://silverlakewine.com/collections/rose?page=5",
"https://silverlakewine.com/collections/rose?page=6"
]
sl_orange_urls = [
"https://silverlakewine.com/collections/orange",
"https://silverlakewine.com/collections/orange?page=2",
"https://silverlakewine.com/collections/orange?page=3",
"https://silverlakewine.com/collections/orange?page=4",
"https://silverlakewine.com/collections/orange?page=5",
"https://silverlakewine.com/collections/orange?page=6"
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
sl_co_fermented_urls = [
"https://silverlakewine.com/collections/fruit-wine"
]


# code for parsing silverlake wine urls
for x in sl_co_fermented_urls:
	soup = BeautifulSoup(requests.get(x).content, 'html.parser')
	products = soup.find_all("div", class_="prod-block")
	for product in products:
		title = product.find("div", class_="title").text.replace(" ", "")
		title_text = product.find("div", class_="title").text.strip()
		price = product.find("div", class_="product-price").text.strip()
		link = 'http://silverlakewine.com' + product.find("a")['href']
		imagesoup = product.find('noscript')
		imagecheck = imagesoup.find("img", class_="rimage__image")
		if imagecheck is not None:
			imageurl = imagesoup.find("img", class_="rimage__image")['src']
			image = 'https:' + imageurl
		else:
			image = 'assets/placeholder.png'
		store = 'silverlake'
		store_text = 'Silverlake Wine'
		type = 'cofermented'
		type_text = 'Co-Fermented'
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
for x in sl_orange_urls:
	soup = BeautifulSoup(requests.get(x).content, 'html.parser')
	products = soup.find_all("div", class_="prod-block")
	for product in products:
		title = product.find("div", class_="title").text.replace(" ", "")
		title_text = product.find("div", class_="title").text.strip()
		price = product.find("div", class_="product-price").text.strip()
		link = 'http://silverlakewine.com' + product.find("a")['href']
		imagesoup = product.find('noscript')
		imagecheck = imagesoup.find("img", class_="rimage__image")
		if imagecheck is not None:
			imageurl = imagesoup.find("img", class_="rimage__image")['src']
			image = 'https:' + imageurl
		else:
			image = 'assets/placeholder.png'
		store = 'silverlake'
		store_text = 'Silverlake Wine'
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
		imagecheck = imagesoup.find("img", class_="rimage__image")
		if imagecheck is not None:
			imageurl = imagesoup.find("img", class_="rimage__image")['src']
			image = 'https:' + imageurl
		else:
			image = 'assets/placeholder.png'
		store = 'silverlake'
		store_text = 'Silverlake Wine'
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
		imagecheck = imagesoup.find("img", class_="rimage__image")
		if imagecheck is not None:
			imageurl = imagesoup.find("img", class_="rimage__image")['src']
			image = 'https:' + imageurl
		else:
			image = 'assets/placeholder.png'
		store = 'silverlake'
		store_text = 'Silverlake Wine'
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
		imagecheck = imagesoup.find("img", class_="rimage__image")
		if imagecheck is not None:
			imageurl = imagesoup.find("img", class_="rimage__image")['src']
			image = 'https:' + imageurl
		else:
			image = 'assets/placeholder.png'
		store = 'silverlake'
		store_text = 'Silverlake Wine'
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
		imagecheck = imagesoup.find("img", class_="rimage__image")
		if imagecheck is not None:
			imageurl = imagesoup.find("img", class_="rimage__image")['src']
			image = 'https:' + imageurl
		else:
			image = 'assets/placeholder.png'
		store = 'silverlake'
		store_text = 'Silverlake Wine'
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

				






# list of everson royce urls to parse
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
er_rose_urls = [
"https://www.eversonroyce.com/collections/rose",
"https://www.eversonroyce.com/collections/rose?page=2",
"https://www.eversonroyce.com/collections/rose?page=3",
"https://www.eversonroyce.com/collections/rose?page=4"
]
er_orange_urls = [
"https://www.eversonroyce.com/collections/orange-wine",
"https://www.eversonroyce.com/collections/orange-wine?page=2",
"https://www.eversonroyce.com/collections/orange-wine?page=3",
"https://www.eversonroyce.com/collections/orange-wine?page=4",
"https://www.eversonroyce.com/collections/orange-wine?page=5",
]
er_sparkling_urls = [
"https://www.eversonroyce.com/collections/sparklin-wine",
"https://www.eversonroyce.com/collections/sparklin-wine?page=2",
"https://www.eversonroyce.com/collections/sparklin-wine?page=3",
"https://www.eversonroyce.com/collections/sparklin-wine?page=4",
"https://www.eversonroyce.com/collections/sparklin-wine?page=5",
"https://www.eversonroyce.com/collections/sparklin-wine?page=6"
]


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
		imagecheck = imagesoup.find("img", class_="rimage__image")
		if imagecheck is not None:
			imageurl = imagesoup.find("img", class_="rimage__image")['src']
			image = 'https:' + imageurl
		else:
			image = 'assets/placeholder.png'
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
		imagecheck = imagesoup.find("img", class_="rimage__image")
		if imagecheck is not None:
			imageurl = imagesoup.find("img", class_="rimage__image")['src']
			image = 'https:' + imageurl
		else:
			image = 'assets/placeholder.png'
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
		imagecheck = imagesoup.find("img", class_="rimage__image")
		if imagecheck is not None:
			imageurl = imagesoup.find("img", class_="rimage__image")['src']
			image = 'https:' + imageurl
		else:
			image = 'assets/placeholder.png'
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
		imagecheck = imagesoup.find("img", class_="rimage__image")
		if imagecheck is not None:
			imageurl = imagesoup.find("img", class_="rimage__image")['src']
			image = 'https:' + imageurl
		else:
			image = 'assets/placeholder.png'
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
		imagecheck = imagesoup.find("img", class_="rimage__image")
		if imagecheck is not None:
			imageurl = imagesoup.find("img", class_="rimage__image")['src']
			image = 'https:' + imageurl
		else:
			image = 'assets/placeholder.png'
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

				
		






# list of kamp urls to parse
kamp_red_urls = [
"https://shopkamp.com/collections/red",
"https://shopkamp.com/collections/chillable-reds"
]
kamp_white_urls = [
"https://shopkamp.com/collections/white"
]
kamp_rose_urls = [
"https://shopkamp.com/collections/rose"
]
kamp_orange_urls = [
"https://shopkamp.com/collections/orange"
]
kamp_sparkling_urls = [
"https://shopkamp.com/collections/sparkling"
]
	
	
# code for parsing kamp urls
for x in kamp_orange_urls:
	soup = BeautifulSoup(requests.get(x).content, 'html.parser')
	products = soup.find_all("div", class_="product--root")
	for product in products:
		title_name = product.find("p", class_="product--title").text.strip()
		title_maker = product.find("div", class_="product--vendor").text.strip()
		title_text = title_maker + " " + title_name
		title = title_text.replace(" ", "")
		price = product.find("span", class_="product--price money").text.strip()
		link = 'http://shopkamp.com' + product.find("a")['href']
		imagesoup = product.find('noscript')
		imagecheck = imagesoup.find("img")
		if imagecheck is not None:
			imageurl = imagesoup.find("img")['src']
			image = 'https:' + imageurl
		else:
			image = 'assets/placeholder.png'
		store = 'kamp'
		store_text = 'Kamp'
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
#			'Maker': title_maker,
		})
for x in kamp_rose_urls:
	soup = BeautifulSoup(requests.get(x).content, 'html.parser')
	products = soup.find_all("div", class_="product--root")
	for product in products:
		title_name = product.find("p", class_="product--title").text.strip()
		title_maker = product.find("div", class_="product--vendor").text.strip()
		title_text = title_maker + " " + title_name
		title = title_text.replace(" ", "")
		price = product.find("span", class_="product--price money").text.strip()
		link = 'http://shopkamp.com' + product.find("a")['href']
		imagesoup = product.find('noscript')
		imagecheck = imagesoup.find("img")
		if imagecheck is not None:
			imageurl = imagesoup.find("img")['src']
			image = 'https:' + imageurl
		else:
			image = 'assets/placeholder.png'
		store = 'kamp'
		store_text = 'Kamp'
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
#			'Maker': title_maker,
		})
for x in kamp_red_urls:
	soup = BeautifulSoup(requests.get(x).content, 'html.parser')
	products = soup.find_all("div", class_="product--root")
	for product in products:
		title_name = product.find("p", class_="product--title").text.strip()
		title_maker = product.find("div", class_="product--vendor").text.strip()
		title_text = title_maker + " " + title_name
		title = title_text.replace(" ", "")
		price = product.find("span", class_="product--price money").text.strip()
		link = 'http://shopkamp.com' + product.find("a")['href']
		imagesoup = product.find('noscript')
		imagecheck = imagesoup.find("img")
		if imagecheck is not None:
			imageurl = imagesoup.find("img")['src']
			image = 'https:' + imageurl
		else:
			image = 'assets/placeholder.png'
		store = 'kamp'
		store_text = 'Kamp'
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
#			'Maker': title_maker,
		})
for x in kamp_white_urls:
	soup = BeautifulSoup(requests.get(x).content, 'html.parser')
	products = soup.find_all("div", class_="product--root")
	for product in products:
		title_name = product.find("p", class_="product--title").text.strip()
		title_maker = product.find("div", class_="product--vendor").text.strip()
		title_text = title_maker + " " + title_name
		title = title_text.replace(" ", "")
		price = product.find("span", class_="product--price money").text.strip()
		link = 'http://shopkamp.com' + product.find("a")['href']
		imagesoup = product.find('noscript')
		imagecheck = imagesoup.find("img")
		if imagecheck is not None:
			imageurl = imagesoup.find("img")['src']
			image = 'https:' + imageurl
		else:
			image = 'assets/placeholder.png'
		store = 'kamp'
		store_text = 'Kamp'
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
#			'Maker': title_maker,
		})
for x in kamp_sparkling_urls:
	soup = BeautifulSoup(requests.get(x).content, 'html.parser')
	products = soup.find_all("div", class_="product--root")
	for product in products:
		title_name = product.find("p", class_="product--title").text.strip()
		title_maker = product.find("div", class_="product--vendor").text.strip()
		title_text = title_maker + " " + title_name
		title = title_text.replace(" ", "")
		price = product.find("span", class_="product--price money").text.strip()
		link = 'http://shopkamp.com' + product.find("a")['href']
		imagesoup = product.find('noscript')
		imagecheck = imagesoup.find("img")
		if imagecheck is not None:
			imageurl = imagesoup.find("img")['src']
			image = 'https:' + imageurl
		else:
			image = 'assets/placeholder.png'
		store = 'kamp'
		store_text = 'Kamp'
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
#			'Maker': title_maker,
		})
	
	
	
	
	
	
# list of field and flask urls to parse
field_red_urls = [
"https://flaskandfield.com/collections/wine?filter.p.product_type=Red+Wine",
"https://flaskandfield.com/collections/wine?filter.p.product_type=Red+Wine&page=2",
"https://flaskandfield.com/collections/wine?filter.p.product_type=Red+Wine&page=3",
"https://flaskandfield.com/collections/wine?filter.p.product_type=Red+Wine&page=4",
]
field_white_urls = [
"https://flaskandfield.com/collections/wine?filter.p.product_type=White+Wine",
"https://flaskandfield.com/collections/wine?filter.p.product_type=White+Wine&page=2",
"https://flaskandfield.com/collections/wine?filter.p.product_type=White+Wine&page=3",
]
field_rose_urls = [
"https://flaskandfield.com/collections/wine?filter.p.product_type=Ros%C3%A9+Wine",
"https://flaskandfield.com/collections/wine?filter.p.product_type=Ros%C3%A9+Wine&page=2",
]
field_orange_urls = [
"https://flaskandfield.com/collections/wine?filter.p.product_type=Skin+Contact+Wine",
"https://flaskandfield.com/collections/wine?filter.p.product_type=Skin+Contact+Wine&page=2",
]
field_sparkling_urls = [
"https://flaskandfield.com/collections/wine?filter.p.product_type=Sparkling+Wine",
"https://flaskandfield.com/collections/wine?filter.p.product_type=Sparkling+Wine&page=2",
]
	
	

# code for parsing field and flask urls
for x in field_orange_urls:
	soup = BeautifulSoup(requests.get(x).content, 'html.parser')
	products = soup.find_all("li", class_="grid__item")
	for product in products:
		title = product.find("h3", class_="card__heading").text.replace(" ", "")
		title_text = product.find("h3", class_="card__heading").text.strip()
		price = product.find("span", class_="price-item").text.strip()
		link = 'http://flaskandfield.com' + product.find("a")['href']
		imagecheck = product.find("img")
		if imagecheck is not None:
			imageurl = product.find("img")['src']
			image = 'https:' + imageurl
		else:
			image = 'assets/placeholder.png'
		store = 'flaskandfield'
		store_text = 'Flask &#38; Field'
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
for x in field_rose_urls:
	soup = BeautifulSoup(requests.get(x).content, 'html.parser')
	products = soup.find_all("li", class_="grid__item")
	for product in products:
		title = product.find("h3", class_="card__heading").text.replace(" ", "")
		title_text = product.find("h3", class_="card__heading").text.strip()
		price = product.find("span", class_="price-item").text.strip()
		link = 'http://flaskandfield.com' + product.find("a")['href']
		imagecheck = product.find("img")
		if imagecheck is not None:
			imageurl = product.find("img")['src']
			image = 'https:' + imageurl
		else:
			image = 'assets/placeholder.png'
		store = 'flaskandfield'
		store_text = 'Flask &#38; Field'
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
for x in field_red_urls:
	soup = BeautifulSoup(requests.get(x).content, 'html.parser')
	products = soup.find_all("li", class_="grid__item")
	for product in products:
		title = product.find("h3", class_="card__heading").text.replace(" ", "")
		title_text = product.find("h3", class_="card__heading").text.strip()
		price = product.find("span", class_="price-item").text.strip()
		link = 'http://flaskandfield.com' + product.find("a")['href']
		imagecheck = product.find("img")
		if imagecheck is not None:
			imageurl = product.find("img")['src']
			image = 'https:' + imageurl
		else:
			image = 'assets/placeholder.png'
		store = 'flaskandfield'
		store_text = 'Flask &#38; Field'
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
for x in field_white_urls:
	soup = BeautifulSoup(requests.get(x).content, 'html.parser')
	products = soup.find_all("li", class_="grid__item")
	for product in products:
		title = product.find("h3", class_="card__heading").text.replace(" ", "")
		title_text = product.find("h3", class_="card__heading").text.strip()
		price = product.find("span", class_="price-item").text.strip()
		link = 'http://flaskandfield.com' + product.find("a")['href']
		imagecheck = product.find("img")
		if imagecheck is not None:
			imageurl = product.find("img")['src']
			image = 'https:' + imageurl
		else:
			image = 'assets/placeholder.png'
		store = 'flaskandfield'
		store_text = 'Flask &#38; Field'
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
for x in field_sparkling_urls:
	soup = BeautifulSoup(requests.get(x).content, 'html.parser')
	products = soup.find_all("li", class_="grid__item")
	for product in products:
		title = product.find("h3", class_="card__heading").text.replace(" ", "")
		title_text = product.find("h3", class_="card__heading").text.strip()
		price = product.find("span", class_="price-item").text.strip()
		link = 'http://flaskandfield.com' + product.find("a")['href']
		imagecheck = product.find("img")
		if imagecheck is not None:
			imageurl = product.find("img")['src']
			image = 'https:' + imageurl
		else:
			image = 'assets/placeholder.png'
		store = 'flaskandfield'
		store_text = 'Flask &#38; Field'
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
