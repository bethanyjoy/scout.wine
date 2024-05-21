# # SF
# from gemini import gemini_base_urls, gemini_pages
# from tomorrow import tw_urls
# from baygrape import bg_base_urls, bg_pages

# # NY
# from lesir import lesir_urls
# from thirst import thirst_urls
# from fiasco import fiasco_base_urls, fiasco_pages
# from leon import leon_urls
# from stranger import sw_urls
# from vanderbilt import vanderbilt_urls




###### ----- Web Scraping with Selenium ----- ######

##### Attempt #1

# url = "https://order.toasttab.com/online/tilda"

# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')

# # Find all 'li' elements with class 'item'
# products = soup.find_all('li', class_='item')

# wines = []
# for product in products:
#     # Find 'h4' element within each 'li' element
#     wine_name = product.find('h4')
#     if wine_name is not None:
#         wines.append(wine_name.text.strip())

# print(wines)

# from selenium import webdriver
# from selenium.webdriver.firefox.service import Service
# from bs4 import BeautifulSoup

# # You need to download the correct driver for your browser and provide the path
# s = Service('./geckodriver')
# driver = webdriver.Firefox(service=s)

# url = "https://order.toasttab.com/online/tilda"
# driver.get(url)

# # Let the JavaScript load
# driver.implicitly_wait(30)

# soup = BeautifulSoup(driver.page_source, 'html.parser')

# # Find all 'li' elements with class 'item'
# products = soup.find_all('li', class_='item')

# wines = []
# for product in products:
#     # Find 'h4' element within each 'li' element
#     wine_name = product.find('h4')
#     print(wine_name)
#     if wine_name is not None:
#         wines.append(wine_name.text.strip())

# print(wines)
# driver.quit()
# # print('success!')


##### Attempt #2

# from selenium import webdriver
# from selenium.webdriver.firefox.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from bs4 import BeautifulSoup

# # You need to download the correct driver for your browser and provide the path
# s = Service('./geckodriver')
# driver = webdriver.Firefox(service=s)

# url = "https://order.toasttab.com/online/tilda"
# driver.get(url)

# # Wait for the 'li' elements with class 'item' to be loaded
# wait = WebDriverWait(driver, 30)
# products = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'li.item')))

# soup = BeautifulSoup(driver.page_source, 'html.parser')

# # Find all 'li' elements with class 'item'
# products = soup.find_all('li', class_='item')

# wines = []
# for product in products:
#     # Find 'h4' element within each 'li' element
#     wine_name = product.find('h4')
#     print(wine_name)
#     if wine_name is not None:
#         wines.append(wine_name.text.strip())

# print(wines)

# driver.quit()

# print('success!')


#########################





###### ----- Other cities/stores ----- ######





# ////////////// KEEP COMMENTED OUT /////////////////


# # Psychic Wines

# # NOT WORKING

# # Generate urls (delete if not needed)
# psychic_urls = generate_urls(psychic_base_urls, psychic_pages)

# for url in psychic_urls:

#     # Define store
#     store = 'Psychic Wines'

#     # Define how to target a product
#     products = get_products(url, "div", "product-group")

#     for product in products:

#         # Define how to target the title 
#         # Note: if name + maker are separate - use other template
#         title_soup = get_title_soup(product, "p", "w-product-title")

#         # Define how to target the image
#         image_src = get_image_src(product, "src")

#         # Define how to target the price
#         price = get_price(product, "div", "product-price__text")

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




# # Vanderbilt Ave Fine Wines

# # Only need to edit orange text and xx instances

# # Test out initial url
# # xx_urls = ["https://vwm.wine/collections/orange-skin-contact"]

# # Generate urls (delete if not needed)
# # xx_urls = generate_urls(xx_base_urls, xx_pages)

# for url in vanderbilt_urls:

#     # Define store
#     store = 'Vanderbilt Ave'

#     # Define how to target a product
#     products = get_products(url, "div", "grid-product")

#     for product in products:

#         # Define how to target the title 
#         # Note: if name + maker are separate - use other template
#         title_soup = get_title_soup(product, "div", "grid-product__title")

#         # Define how to target the image
#         image_src = get_image_src(product, "src")
#         # image_src = get_image_src_parentdiv(product, "image-wrap")

#         # Define how to target the price
#         price = get_price(product, "div", "grid-product__price")
#         # price = None

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

#         print(title)







# # Stranger Wines

# for url in sw_urls:

#     # Define store
#     store = 'Stranger Wines'

#     # Define how to target a product
#     products = get_products(url, "div", "product")

#     for product in products:

#         # Define how to target the title 
#         # Note: if name + maker are separate - use other template
#         title_soup = get_title_soup(product, "a", "title")

#         # Define how to target the image
#         image_src = get_image_src(product, "src")

#         # Define how to target the price
#         price = get_price(product, "div", "price")

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

#         print(title)







# # Foret - not working

# # Only need to edit orange text and xx instances

# # Test out initial url
# xx_urls = ["https://www.foretwineshop.com/shop/red/10?page=1&limit=180"]

# # Generate urls (delete if not needed)
# # xx_urls = generate_urls(xx_base_urls, xx_pages)

# for url in xx_urls:

#     # Define store
#     store = 'xx'

#     # Define how to target a product
#     products = get_products(url, "div", "product-group")

#     for product in products:

#         # Define how to target the title 
#         # Note: if name + maker are separate - use other template
#         title_soup = get_title_soup(product, "p", " w-product-title")

#         # Define how to target the image
#         image_src = get_image_src(product, "src")

#         # Define how to target the price
#         price = get_price(product, "div", "product-price__text")

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




# # /////////// New York /////////



# # Fiasco Wine

# # Generate urls (delete if not needed)
# fiasco_urls = generate_urls(fiasco_base_urls, fiasco_pages)

# for url in fiasco_urls:

#     # Define store
#     store = 'Fiasco! Wine'

#     # Define how to target a product
#     products = get_products(url, "li", "collection__list-item")

#     for product in products:

#         # Define how to target the title 
#         # Note: if name + maker are separate - use other template
#         title_soup = get_title_soup(product, "h3", "product-card__title")

#         # Define how to target the image
#         image_src = get_image_src_parentdiv(product, "product-card__image")

#         # Define how to target the price
#         price = get_price(product, "span", "price__regular-value")

#         # ! Custom code
#         # Define how to locate non-wine products
#         status_check = product.find("div", class_="product-badges__badge--sold-out")

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
        
#         # ! Custom code
#         # Ignore sold-out items
#         if status_check:
#             continue

#         # Continue parsing wine products
#         else:

#             # Check if it's a wine item, if so add to wine list
#             wine = process_item(title_string, image, image_type, url, maker, price, region, store, title, product_type)
#             if wine is not None:
#                 wines.append(wine)






# # Leon & Son

# for url in leon_urls:

#     # Define store
#     store = 'Leon + Son'

#     # Define how to target a product
#     products = get_products(url, "div", "product_thumb")

#     for product in products:

#         # Define how to target the title 
#         # Note: if name + maker are separate - use other template
#         title_soup = get_title_soup(product, "h3")

#         # Define how to target the image
#         image_src = get_image_src(product, "src")

#         # Define how to target the price
#         price = get_price(product, "p", "price")

#         # ! Custom code
#         # Define how to locate non-wine products
#         status_check = product.find("li", class_="sold_out")

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
        
#         # ! Custom code
#         # Ignore sold-out items
#         if status_check:
#             continue

#         # Continue parsing wine products
#         else:

#             # Check if it's a wine item, if so add to wine list
#             wine = process_item(title_string, image, image_type, url, maker, price, region, store, title, product_type)
#             if wine is not None:
#                 wines.append(wine)

#             print(title)







# # Thirst Merchants

# for url in thirst_urls:

#     # Define store
#     store = 'Thirst'

#     # Define how to target a product
#     products = get_products(url, "li", "grid__item")

#     for product in products:

#         # Define how to target the title 
#         # Note: if name + maker are separate - use other template
#         title_soup = get_title_soup(product, "h3", "h5")

#         # Define how to target the image
#         image_src = get_image_src(product, "src")

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
        
#         # Check if it's a wine item, if so add to wine list
#         wine = process_item(title_string, image, image_type, url, maker, price, region, store, title, product_type)
#         if wine is not None:
#             wines.append(wine)




# # Lesir (NY)

# for url in lesir_urls:

#     # Define store
#     store = 'Lesir'

#     # Define how to target a product
#     products = get_products(url, "div", "grid-item")

#     for product in products:

#         # Define how to target the title 
#         # Note: if name + maker are separate - use other template
#         title_soup = get_title_soup(product, "div", "grid-title")

#         # Define how to target the image
#         image_src = get_image_src(product, "src")

#         # Define how to target the price
#         price = get_price(product, "div", "product-price")

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





# # Henry's - Won't work without selenium (load more page issue)

# # Test out initial url
# xx_urls = ["https://henrys.nyc/collections/red-wine"]

# # Generate urls (delete if not needed)
# # xx_urls = generate_urls(xx_base_urls, xx_pages)

# for url in xx_urls:

#     # Define store
#     store = 'xx'

#     # Define how to target a product
#     products = get_products(url, "li", "grid__item")

#     for product in products:

#         # Define how to target the title 
#         # Note: if name + maker are separate - use other template
#         title_soup = get_title_soup(product, "span", "indiv-product-title-text")

#         # Define how to target the image
#         image_src = get_image_src(product, "src")

#         # Define how to target the price
#         price = get_price(product, "span", "money")

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









# /////////// San Francisco /////////


# # Bay Grape Wine (SF)

# # Generate urls (delete if not needed)
# bg_urls = generate_urls(bg_base_urls, bg_pages)

# for url in bg_urls:

#     # Define store
#     store = 'Bay Grape Wine'

#     # Define how to target a product
#     products = get_products(url, "div", "v65-product3Up")
#     # products = get_products(url, "div", "v65-group")

#     for product in products:

#         # Define how to target the title 
#         # Note: if name + maker are separate - use other template
#         title_soup = get_title_soup(product, "div", "v65-product-title")
#         # title_soup = get_title_soup(product, "div", "v65-title")

#         # Define how to target the image
#         image_src = "oakland.baygrapewine.com" + get_image_src(product, "src")

#         # Define how to target the price
#         price = get_price(product, "div", "v65-product-addToCart-price")

#         # /// Don't need to edit anything below this point /// #

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
#         # image, image_type = process_image_src_loadcheck(image_src)
#         image, image_type = process_image_src(image_src)

#         # Check if it's a wine item, if so add to wine list
#         wine = process_item(title_string, image, image_type, url, maker, price, region, store, title, product_type)
#         if wine is not None:
#             wines.append(wine)







# # Tomorrow's Wine (SF)

# for url in tw_urls:

#     # Define store
#     store = 'Tomorrows Wine'

#     # Define how to target a product
#     products = get_products(url, "li", "product")

#     for product in products:

#         # Define how to target the title 
#         # Note: if name + maker are separate - use other template
#         title_soup = get_title_soup(product, "h2", "title")

#         # Define how to target the image
#         image_src = get_image_src(product, "src")

#         # Define how to target the price
#         price = get_price(product, "p", "price")

#         # ! Custom code
#         # Define how to locate non-wine products
#         status_check = product.find("span", class_="badge-soldout")

#         # /// Don't need to edit anything below this point /// #

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

#         # ! Custom code
#         # Ignore sold-out items
#         if status_check:
#             continue

#         # Continue parsing wine products
#         else:
        
#             # Check if it's a wine item, if so add to wine list
#             wine = process_item(title_string, image, image_type, url, maker, price, region, store, title, product_type)
#             if wine is not None:
#                 wines.append(wine)

                




# # Gemini Bottle Co. (SF)

# # Generate urls (delete if not needed)
# gemini_urls = generate_urls(gemini_base_urls, gemini_pages)

# for url in gemini_urls:

#     # Define store
#     store = 'Gemini Bottle Co.'

#     # Define how to target a product
#     products = get_products(url, "div", "product-grid-item")

#     for product in products:

#         # Define how to target the title 
#         # Note: if name + maker are separate - use other template
#         title_soup = get_title_soup(product, "p", "grid__title")

#         # Define how to target the image
#         image_src = get_image_src(product, "src")

#         # Define how to target the price
#         price = get_price(product, "span", "price")

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





# # Bottle Bacchanal (SF)

# # Only need to edit orange text and XX instances

# # Test out initial url
# bb_urls = ["https://www.bottlebacchanal.com/shop/orange/28"]

# # Generate urls (delete if not needed)
# # XX_urls = generate_urls(XX_base_urls, XX_pages)

# for url in bb_urls:

#     # Define store
#     store = 'Bottle Bacchanal'

#     # Define how to target a product
#     products = get_products(url, "div", "product-group")

#     print(products)

#     for product in products:

#         # Define how to target the title 
#         # Note: if name + maker are separate - use other template
#         title_soup = get_title_soup(product, "div", "product-title__text")

#         # Define how to target the image
#         image_src = get_image_src(product, "src")

#         # Define how to target the price
#         price = get_price(product, "div", "product-price__text")

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


