import re
import json
import requests
from bs4 import BeautifulSoup

# sets up empty list to store wine data
wines = []

# list of goodluck wine urls to parse
gl_orange_urls = [
"https://www.goodluckwineshop.com/shop/orangewine/6?page=1&limit=180&sort_by=category_order&sort_order=asc"
]
gl_rose_urls = [
"https://www.goodluckwineshop.com/shop/ros-/3?page=1&limit=180&sort_by=category_order&sort_order=asc"
]
gl_red_urls = [
"https://www.goodluckwineshop.com/shop/redwine/4?page=1&limit=180&sort_by=category_order&sort_order=asc"
]
gl_sparkling_urls = [
"https://www.goodluckwineshop.com/shop/sparkling/5?page=1&limit=180&sort_by=category_order&sort_order=asc"
]
gl_white_urls = [
"https://www.goodluckwineshop.com/shop/whitewine/2?page=1&limit=180&sort_by=category_order&sort_order=asc"
]

# list of silverlake wine urls to parse
sl_orange_urls = [
"https://silverlakewine.ecwid.com/Orange-&-Skin-Contact-c50339661"
]
sl_red_urls = [
"https://silverlakewine.ecwid.com/French-Red-c50377213",
"https://silverlakewine.ecwid.com/American-Red-c50356323",
"https://silverlakewine.ecwid.com/Italian-Red-c50357299",
"https://silverlakewine.ecwid.com/Spain-Portugal-Red-c50357296",
"https://silverlakewine.ecwid.com/Eastern-European-Red-c50356322",
"https://silverlakewine.ecwid.com/Southern-Hemisphere-Red-c50356321"
]
sl_rose_urls = [
"https://silverlakewine.ecwid.com/Ros%C3%A9-c50357170"
]
sl_sparkling_urls = [
"https://silverlakewine.ecwid.com/Sparkling-c50339659"
]
sl_white_urls = [
"https://silverlakewine.ecwid.com/French-White-c50339663",
"https://silverlakewine.ecwid.com/American-White-c50357300",
"https://silverlakewine.ecwid.com/Italian-White-c50357298",
"https://silverlakewine.ecwid.com/Spain-Portugal-White-c50338673",
"https://silverlakewine.ecwid.com/Eastern-European-White-c50357297",
"https://silverlakewine.ecwid.com/Southern-Hemisphere-White-c50339660"
]

# list of highland park wine urls to parse
hlp_orange_urls = [
"https://highlandparkwine.company.site/Orange-&-Skin-Contact-c55336450",
"https://highlandparkwine.company.site/Orange-&-Skin-Contact-c55336450?offset=60",
"https://highlandparkwine.company.site/Orange-&-Skin-Contact-c55336450?offset=120"
]
hlp_red_urls = [
"https://highlandparkwine.company.site/French-Red-c55334847",
"https://highlandparkwine.company.site/French-Red-c55334847?offset=60",
"https://highlandparkwine.company.site/French-Red-c55334847?offset=120",
"https://highlandparkwine.company.site/Italian-Red-c55334846",
"https://highlandparkwine.company.site/Italian-Red-c55334846?offset=60",
"https://highlandparkwine.company.site/Italian-Red-c55334846?offset=120",
"https://highlandparkwine.company.site/American-Red-c55333952",
"https://highlandparkwine.company.site/American-Red-c55333952?offset=60",
"https://highlandparkwine.company.site/American-Red-c55333952?offset=120",
"https://highlandparkwine.company.site/Spain-Portugal-Red-c55333956",
"https://highlandparkwine.company.site/Spain-Portugal-Red-c55333956?offset=60",
"https://highlandparkwine.company.site/Spain-Portugal-Red-c55333956?offset=120",
"https://highlandparkwine.company.site/Eastern-European-Red-c55336453",
"https://highlandparkwine.company.site/Eastern-European-Red-c55336453?offset=60",
"https://highlandparkwine.company.site/Eastern-European-Red-c55336453?offset=120",
"https://highlandparkwine.company.site/Southern-Hemisphere-Red-c55336454",
"https://highlandparkwine.company.site/Southern-Hemisphere-Red-c55336454?offset=60",
"https://highlandparkwine.company.site/Southern-Hemisphere-Red-c55336454?offset=120"
]
hlp_rose_urls = [
"https://highlandparkwine.company.site/Ros%C3%A9-All-Day-c55334842",
"https://highlandparkwine.company.site/Ros%C3%A9-All-Day-c55334842?offset=60",
"https://highlandparkwine.company.site/Ros%C3%A9-All-Day-c55334842?offset=120"
]
hlp_sparkling_urls = [
"https://highlandparkwine.company.site/Sparkling-c55334841",
"https://highlandparkwine.company.site/Sparkling-c55334841?offset=60",
"https://highlandparkwine.company.site/Sparkling-c55334841?offset=120"
]
hlp_white_urls = [
"https://highlandparkwine.company.site/French-White-c55334849",
"https://highlandparkwine.company.site/French-White-c55334849?offset=60",
"https://highlandparkwine.company.site/French-White-c55334849?offset=120",
"https://highlandparkwine.company.site/Italian-White-c55334844",
"https://highlandparkwine.company.site/Italian-White-c55334844?offset=60",
"https://highlandparkwine.company.site/Italian-White-c55334844?offset=120",
"https://highlandparkwine.company.site/American-White-c55334843",
"https://highlandparkwine.company.site/American-White-c55334843?offset=60",
"https://highlandparkwine.company.site/American-White-c55334843?offset=120",
"https://highlandparkwine.company.site/Spain-Portugal-White-c55336456",
"https://highlandparkwine.company.site/Spain-Portugal-White-c55336456?offset=60",
"https://highlandparkwine.company.site/Spain-Portugal-White-c55336456?offset=120",
"https://highlandparkwine.company.site/Eastern-European-White-c55334848",
"https://highlandparkwine.company.site/Eastern-European-White-c55334848?offset=60",
"https://highlandparkwine.company.site/Eastern-European-White-c55334848?offset=120",
"https://highlandparkwine.company.site/Southern-Hemisphere-White-c55334850",
"https://highlandparkwine.company.site/Southern-Hemisphere-White-c55334850?offset=60",
"https://highlandparkwine.company.site/Southern-Hemisphere-White-c55334850?offset=120",
]

# list of everson royce urls to parse
er_orange_urls = [
"https://eversonroycepasadena.company.site/Orange-&-Skin-Contact-c55336468",
"https://eversonroycepasadena.company.site/Orange-&-Skin-Contact-c55336468?offset=60",
"https://eversonroycepasadena.company.site/Orange-&-Skin-Contact-c55336468?offset=120"
]
er_red_urls = [
"https://eversonroycepasadena.company.site/French-Red-c55334859",
"https://eversonroycepasadena.company.site/French-Red-c55334859?offset=60",
"https://eversonroycepasadena.company.site/French-Red-c55334859?offset=120",
"https://eversonroycepasadena.company.site/American-Red-c55336471",
"https://eversonroycepasadena.company.site/American-Red-c55336471?offset=60",
"https://eversonroycepasadena.company.site/American-Red-c55336471?offset=120",
"https://eversonroycepasadena.company.site/Spain-Portugal-Red-c55336477",
"https://eversonroycepasadena.company.site/Spain-Portugal-Red-c55336477?offset=60",
"https://eversonroycepasadena.company.site/Spain-Portugal-Red-c55336477?offset=120",
"https://eversonroycepasadena.company.site/Italian-Red-c55336470",
"https://eversonroycepasadena.company.site/Italian-Red-c55336470?offset=60",
"https://eversonroycepasadena.company.site/Italian-Red-c55336470?offset=120",
"https://eversonroycepasadena.company.site/Southern-Hemisphere-Red-c55336475",
"https://eversonroycepasadena.company.site/Southern-Hemisphere-Red-c55336475?offset=60",
"https://eversonroycepasadena.company.site/Southern-Hemisphere-Red-c55336475?offset=120",
"https://eversonroycepasadena.company.site/Eastern-European-Red-c55334860",
"https://eversonroycepasadena.company.site/Eastern-European-Red-c55334860?offset=60",
"https://eversonroycepasadena.company.site/Eastern-European-Red-c55334860?offset=120"
]
er_rose_urls = [
"https://eversonroycepasadena.company.site/Ros%C3%A9-c55334856",
"https://eversonroycepasadena.company.site/Ros%C3%A9-c55334856?offset=60",
"https://eversonroycepasadena.company.site/Ros%C3%A9-c55334856?offset=120"
]
er_sparkling_urls = [
"https://eversonroycepasadena.company.site/Sparkling-c55336466",
"https://eversonroycepasadena.company.site/Sparkling-c55336466?offset=60",
"https://eversonroycepasadena.company.site/Sparkling-c55336466?offset=120"
]
er_white_urls = [
"https://eversonroycepasadena.company.site/French-White-c55334861",
"https://eversonroycepasadena.company.site/French-White-c55334861?offset=60",
"https://eversonroycepasadena.company.site/French-White-c55334861?offset=120",
"https://eversonroycepasadena.company.site/American-White-c55336467",
"https://eversonroycepasadena.company.site/American-White-c55336467?offset=60",
"https://eversonroycepasadena.company.site/American-White-c55336467?offset=120",
"https://eversonroycepasadena.company.site/Spain-Portugal-White-c55334863",
"https://eversonroycepasadena.company.site/Spain-Portugal-White-c55334863?offset=60",
"https://eversonroycepasadena.company.site/Spain-Portugal-White-c55334863?offset=120",
"https://eversonroycepasadena.company.site/Italian-White-c55334857",
"https://eversonroycepasadena.company.site/Italian-White-c55334857?offset=60",
"https://eversonroycepasadena.company.site/Italian-White-c55334857?offset=120",
"https://eversonroycepasadena.company.site/Southern-Hemisphere-White-c55336476",
"https://eversonroycepasadena.company.site/Southern-Hemisphere-White-c55336476?offset=60",
"https://eversonroycepasadena.company.site/Southern-Hemisphere-White-c55336476?offset=120",
"https://eversonroycepasadena.company.site/Eastern-European-White-c55336473",
"https://eversonroycepasadena.company.site/Eastern-European-White-c55336473?offset=60",
"https://eversonroycepasadena.company.site/Eastern-European-White-c55336473?offset=120"
]

# code for parsing highland park wine urls
for x in hlp_orange_urls:
    soup = BeautifulSoup(requests.get(x).content, 'html.parser')
    products = soup.find_all("div", class_="grid-product")
    for product in products:
        title = product.find("div", class_="grid-product__title-inner").text.replace(" ", "")
        title_text = product.find("div", class_="grid-product__title-inner").text.strip()
        price = product.find("div", class_="grid-product__price").text.strip()
        link = product.find("a", class_="grid-product__title")['href']
        if product.img:
            image = product.find("img", class_="grid-product__picture")['src']
        else:
            image = 'https://cdn11.bigcommerce.com/s-t1pm6282q8/images/stencil/500x659/products/918/1976/image_coming_soon__47973.1624218886.1280.1280__52076.1628386968.jpg?c=1'
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
    products = soup.find_all("div", class_="grid-product")
    for product in products:
        title = product.find("div", class_="grid-product__title-inner").text.replace(" ", "")
        title_text = product.find("div", class_="grid-product__title-inner").text.strip()
        price = product.find("div", class_="grid-product__price").text.strip()
        link = product.find("a", class_="grid-product__title")['href']
        if product.img:
            image = product.find("img", class_="grid-product__picture")['src']
        else:
            image = 'https://cdn11.bigcommerce.com/s-t1pm6282q8/images/stencil/500x659/products/918/1976/image_coming_soon__47973.1624218886.1280.1280__52076.1628386968.jpg?c=1'
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
    products = soup.find_all("div", class_="grid-product")
    for product in products:
        title = product.find("div", class_="grid-product__title-inner").text.replace(" ", "")
        title_text = product.find("div", class_="grid-product__title-inner").text.strip()
        price = product.find("div", class_="grid-product__price").text.strip()
        link = product.find("a", class_="grid-product__title")['href']
        if product.img:
            image = product.find("img", class_="grid-product__picture")['src']
        else:
            image = 'https://cdn11.bigcommerce.com/s-t1pm6282q8/images/stencil/500x659/products/918/1976/image_coming_soon__47973.1624218886.1280.1280__52076.1628386968.jpg?c=1'
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
    products = soup.find_all("div", class_="grid-product")
    for product in products:
        title = product.find("div", class_="grid-product__title-inner").text.replace(" ", "")
        title_text = product.find("div", class_="grid-product__title-inner").text.strip()
        price = product.find("div", class_="grid-product__price").text.strip()
        link = product.find("a", class_="grid-product__title")['href']
        if product.img:
            image = product.find("img", class_="grid-product__picture")['src']
        else:
            image = 'https://cdn11.bigcommerce.com/s-t1pm6282q8/images/stencil/500x659/products/918/1976/image_coming_soon__47973.1624218886.1280.1280__52076.1628386968.jpg?c=1'
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
    products = soup.find_all("div", class_="grid-product")
    for product in products:
        title = product.find("div", class_="grid-product__title-inner").text.replace(" ", "")
        title_text = product.find("div", class_="grid-product__title-inner").text.strip()
        price = product.find("div", class_="grid-product__price").text.strip()
        link = product.find("a", class_="grid-product__title")['href']
        if product.img:
            image = product.find("img", class_="grid-product__picture")['src']
        else:
            image = 'https://cdn11.bigcommerce.com/s-t1pm6282q8/images/stencil/500x659/products/918/1976/image_coming_soon__47973.1624218886.1280.1280__52076.1628386968.jpg?c=1'
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

# code for parsing silverlake wine urls
for x in sl_orange_urls:
    soup = BeautifulSoup(requests.get(x).content, 'html.parser')
    products = soup.find_all("div", class_="grid-product")
    for product in products:
        title = product.find("div", class_="grid-product__title-inner").text.replace(" ", "")
        title_text = product.find("div", class_="grid-product__title-inner").text.strip()
        price = product.find("div", class_="grid-product__price").text.strip()
        link = product.find("a", class_="grid-product__title")['href']
        if product.img:
            image = product.find("img", class_="grid-product__picture")['src']
        else:
            image = 'https://cdn11.bigcommerce.com/s-t1pm6282q8/images/stencil/500x659/products/918/1976/image_coming_soon__47973.1624218886.1280.1280__52076.1628386968.jpg?c=1'
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
    products = soup.find_all("div", class_="grid-product")
    for product in products:
        title = product.find("div", class_="grid-product__title-inner").text.replace(" ", "")
        title_text = product.find("div", class_="grid-product__title-inner").text.strip()
        price = product.find("div", class_="grid-product__price").text.strip()
        link = product.find("a", class_="grid-product__title")['href']
        if product.img:
            image = product.find("img", class_="grid-product__picture")['src']
        else:
            image = 'https://cdn11.bigcommerce.com/s-t1pm6282q8/images/stencil/500x659/products/918/1976/image_coming_soon__47973.1624218886.1280.1280__52076.1628386968.jpg?c=1'
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
    products = soup.find_all("div", class_="grid-product")
    for product in products:
        title = product.find("div", class_="grid-product__title-inner").text.replace(" ", "")
        title_text = product.find("div", class_="grid-product__title-inner").text.strip()
        price = product.find("div", class_="grid-product__price").text.strip()
        link = product.find("a", class_="grid-product__title")['href']
        if product.img:
            image = product.find("img", class_="grid-product__picture")['src']
        else:
            image = 'https://cdn11.bigcommerce.com/s-t1pm6282q8/images/stencil/500x659/products/918/1976/image_coming_soon__47973.1624218886.1280.1280__52076.1628386968.jpg?c=1'
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
    products = soup.find_all("div", class_="grid-product")
    for product in products:
        title = product.find("div", class_="grid-product__title-inner").text.replace(" ", "")
        title_text = product.find("div", class_="grid-product__title-inner").text.strip()
        price = product.find("div", class_="grid-product__price").text.strip()
        link = product.find("a", class_="grid-product__title")['href']
        if product.img:
            image = product.find("img", class_="grid-product__picture")['src']
        else:
            image = 'https://cdn11.bigcommerce.com/s-t1pm6282q8/images/stencil/500x659/products/918/1976/image_coming_soon__47973.1624218886.1280.1280__52076.1628386968.jpg?c=1'
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
    products = soup.find_all("div", class_="grid-product")
    for product in products:
        title = product.find("div", class_="grid-product__title-inner").text.replace(" ", "")
        title_text = product.find("div", class_="grid-product__title-inner").text.strip()
        price = product.find("div", class_="grid-product__price").text.strip()
        link = product.find("a", class_="grid-product__title")['href']
        if product.img:
            image = product.find("img", class_="grid-product__picture")['src']
        else:
            image = 'https://cdn11.bigcommerce.com/s-t1pm6282q8/images/stencil/500x659/products/918/1976/image_coming_soon__47973.1624218886.1280.1280__52076.1628386968.jpg?c=1'
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
    products = soup.find_all("div", class_="grid-product")
    for product in products:
        title = product.find("div", class_="grid-product__title-inner").text.replace(" ", "")
        title_text = product.find("div", class_="grid-product__title-inner").text.strip()
        price = product.find("div", class_="grid-product__price").text.strip()
        link = product.find("a", class_="grid-product__title")['href']
        if product.img:
            image = product.find("img", class_="grid-product__picture")['src']
        else:
            image = 'https://cdn11.bigcommerce.com/s-t1pm6282q8/images/stencil/500x659/products/918/1976/image_coming_soon__47973.1624218886.1280.1280__52076.1628386968.jpg?c=1'
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
    products = soup.find_all("div", class_="grid-product")
    for product in products:
        title = product.find("div", class_="grid-product__title-inner").text.replace(" ", "")
        title_text = product.find("div", class_="grid-product__title-inner").text.strip()
        price = product.find("div", class_="grid-product__price").text.strip()
        link = product.find("a", class_="grid-product__title")['href']
        if product.img:
            image = product.find("img", class_="grid-product__picture")['src']
        else:
            image = 'https://cdn11.bigcommerce.com/s-t1pm6282q8/images/stencil/500x659/products/918/1976/image_coming_soon__47973.1624218886.1280.1280__52076.1628386968.jpg?c=1'
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
    products = soup.find_all("div", class_="grid-product")
    for product in products:
        title = product.find("div", class_="grid-product__title-inner").text.replace(" ", "")
        title_text = product.find("div", class_="grid-product__title-inner").text.strip()
        price = product.find("div", class_="grid-product__price").text.strip()
        link = product.find("a", class_="grid-product__title")['href']
        if product.img:
            image = product.find("img", class_="grid-product__picture")['src']
        else:
            image = 'https://cdn11.bigcommerce.com/s-t1pm6282q8/images/stencil/500x659/products/918/1976/image_coming_soon__47973.1624218886.1280.1280__52076.1628386968.jpg?c=1'
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
    products = soup.find_all("div", class_="grid-product")
    for product in products:
        title = product.find("div", class_="grid-product__title-inner").text.replace(" ", "")
        title_text = product.find("div", class_="grid-product__title-inner").text.strip()
        price = product.find("div", class_="grid-product__price").text.strip()
        link = product.find("a", class_="grid-product__title")['href']
        if product.img:
            image = product.find("img", class_="grid-product__picture")['src']
        else:
            image = 'https://cdn11.bigcommerce.com/s-t1pm6282q8/images/stencil/500x659/products/918/1976/image_coming_soon__47973.1624218886.1280.1280__52076.1628386968.jpg?c=1'
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
    products = soup.find_all("div", class_="grid-product")
    for product in products:
        title = product.find("div", class_="grid-product__title-inner").text.replace(" ", "")
        title_text = product.find("div", class_="grid-product__title-inner").text.strip()
        price = product.find("div", class_="grid-product__price").text.strip()
        link = product.find("a", class_="grid-product__title")['href']
        if product.img:
            image = product.find("img", class_="grid-product__picture")['src']
        else:
            image = 'https://cdn11.bigcommerce.com/s-t1pm6282q8/images/stencil/500x659/products/918/1976/image_coming_soon__47973.1624218886.1280.1280__52076.1628386968.jpg?c=1'
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

# code for parsing goodluck wine urls
for x in gl_orange_urls:
    soup = BeautifulSoup(requests.get(x).content, 'html.parser')
    products = soup.find_all("div", class_="w-container")
    for product in products:
        title = product.find("h3", class_="w-product-title").text.replace(" ", "")
        title_text = product.find("h3", class_="w-product-title").text.strip()
        price = product.find("span", class_="price price--withoutTax").text.strip()
        link = product.find("a", class_="card-figure__link")['href'].strip("/")
        image = product.find("img", class_="card-image")['src']
        store = 'goodluck'
        store_text = 'Good Luck Wine Shop'
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
for x in gl_rose_urls:
    soup = BeautifulSoup(requests.get(x).content, 'html.parser')
    products = soup.find_all("li", class_="product")
    for product in products:
        title = product.find("h3", class_="card-title").text.replace(" ", "")
        title_text = product.find("h3", class_="card-title").text.strip()
        price = product.find("span", class_="price price--withoutTax").text.strip()
        link = product.find("a", class_="card-figure__link")['href'].strip("/")
        image = product.find("img", class_="card-image")['src']
        store = 'goodluck'
        store_text = 'Good Luck Wine Shop'
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
for x in gl_red_urls:
    soup = BeautifulSoup(requests.get(x).content, 'html.parser')
    products = soup.find_all("li", class_="product")
    for product in products:
        title = product.find("h3", class_="card-title").text.replace(" ", "")
        title_text = product.find("h3", class_="card-title").text.strip()
        price = product.find("span", class_="price price--withoutTax").text.strip()
        link = product.find("a", class_="card-figure__link")['href'].strip("/")
        image = product.find("img", class_="card-image")['src']
        store = 'goodluck'
        store_text = 'Good Luck Wine Shop'
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
for x in gl_white_urls:
    soup = BeautifulSoup(requests.get(x).content, 'html.parser')
    products = soup.find_all("li", class_="product")
    for product in products:
        title = product.find("h3", class_="card-title").text.replace(" ", "")
        title_text = product.find("h3", class_="card-title").text.strip()
        price = product.find("span", class_="price price--withoutTax").text.strip()
        link = product.find("a", class_="card-figure__link")['href'].strip("/")
        image = product.find("img", class_="card-image")['src']
        store = 'goodluck'
        store_text = 'Good Luck Wine Shop'
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
for x in gl_sparkling_urls:
    soup = BeautifulSoup(requests.get(x).content, 'html.parser')
    products = soup.find_all("li", class_="product")
    for product in products:
        title = product.find("h3", class_="card-title").text.replace(" ", "")
        title_text = product.find("h3", class_="card-title").text.strip()
        price = product.find("span", class_="price price--withoutTax").text.strip()
        link = product.find("a", class_="card-figure__link")['href'].strip("/")
        image = product.find("img", class_="card-image")['src']
        store = 'goodluck'
        store_text = 'Good Luck Wine Shop'
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
#print(json.dumps(wines, indent=4))
print('success!')
