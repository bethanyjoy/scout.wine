import re
import json
import requests
from bs4 import BeautifulSoup

# sets up empty list to store wine data
wines = []

tilda_urls = [
"https://www.toasttab.com/tilda/v3/#db025dcc7-6210-4276-809d-75b737e53506d5cbaafd1-39b5-4407-9e83-eef5eb431ef2"
]

tr_urls = [
"https://tabularasabar.com/collections/orange-wine-1"
]

hm_rose_urls = [
"https://www.heavensmarketla.com/collections/rose"
]


for x in hm_rose_urls:
    soup = BeautifulSoup(requests.get(x).content, 'html.parser')
    products = soup.find_all("li", class_="grid__item")
    for product in products:
        url = 'https://www.heavensmarketla.com'
        title = product.find("div", class_="grid-view-item__title").text.strip()
        junk = product.find("dl", class_="price price--listing").text.strip()
        price = product.find("span", class_="price-item").text.strip()
        link = product.find("a", class_="grid-view-item__link")['href']
        # image = product.find("img")['srcset']
        store = 'heavensmarket'
        store_text = 'Heavens Market'
        type = 'rose'
        type_text = 'Ros&#233;'
        wines.append({
            'Title': title - junk,
            'Price': price,
            'Link': url + link,
            # 'Image': image,
            'Type': type,
            'Type_text': type_text,
            'Store': store,
            'Store_text': store_text,
        })

# for x in tr_urls:
#     soup = BeautifulSoup(requests.get(x).content, 'html.parser')
#     products = soup.find_all("div", class_="product-list-item")
#     for product in products:
#         title = product.find("h4", class_="product-list-item-title").find("a").text.strip()
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
#             'Price': price,
#             'Link': link,
#             'Image': image,
#             'Type': type,
#             'Type_text': type_text,
#             'Store': store,
#             'Store_text': store_text,
#         })


# code for parsing tilda wine urls
# for x in tilda_urls:
#     soup = BeautifulSoup(requests.get(x).content, 'html.parser')
#     products = soup.find_all("li", class_="MenuItems-module__menuItem___3XYqJ")
#     for product in products:
#         title = product.find("span", class_="MenuItems-module__name___3MPgA").text.strip()
#         price = product.find("span", class_="MenuItemPrice-module__price___2mlHx").text.strip()
#         link = product.find("a", class_="MenuItems-module__menuItemLink___1j53q")['href'].strip("/")
#         if product.img:
#             image = product.find("div", class_="MenuItemImage-module__image___1J90p")['style']
#         else:
#             image = 'https://cdn11.bigcommerce.com/s-t1pm6282q8/images/stencil/500x659/products/918/1976/image_coming_soon__47973.1624218886.1280.1280__52076.1628386968.jpg?c=1'
#         store = 'goodluck'
#         store_text = 'Good Luck Wine Shop'
#         type = 'orange'
#         type_text = 'Orange'
#         wines.append({
#             'Title': title,
#             'Price': price,
#             'Link': link,
#             'Image': image,
#             'Type': type,
#             'Type_text': type_text,
#             'Store': store,
#             'Store_text': store_text,
#         })


# writes the wine data to the json file
with open("new-store-test.json", "w") as writeJSON:
    json.dump({'wine': wines}, writeJSON, ensure_ascii=False)

# prints data to terminal (only needed for troubleshooting)
#print(json.dumps(wines, indent=4))
print('success!')
