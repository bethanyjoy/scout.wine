



# Stanley's wet gooods

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import time

# List of URLs to scrape
# urls = ["https://www.stanleys.la/shop/wine/wine-by-type/reds/?limit=72"]

driver = webdriver.Firefox()

for url in stanley_urls:
    driver.get(url)

    # Scroll page by page
    scroll_pause_time = 1  # You can set your own pause time. My laptop is a bit slow so I use 1 sec
    screen_height = driver.execute_script("return window.screen.height;")   # get the screen height of the web
    i = 1

    while True:
        # scroll one screen height each time
        driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))  
        i += 1
        time.sleep(scroll_pause_time)
        # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
        scroll_height = driver.execute_script("return document.body.scrollHeight;")  
        # Break the loop when the height we need to scroll to is larger than the total scroll height
        if (screen_height) * i > scroll_height:
            break 

    # Now you can parse the page HTML with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Define how to target a product
    products = soup.find('ul', 'list-collection').find_all('li')

    # Define store
    store = "Stanley's Wet Goods"

    # Print the 'src' attribute of each image
    for product in products:

        # Define how to target the title 
        title_soup = get_title_soup(product, "div", "right_side_sec12")

        # Define how to target the image
        image_src = product.find("img", class_="first-image")['src']
        # print(image_src)

        # Define how to target the price
        price = product.find("p", class_="price").contents[0].strip()

        # --- Don't need to edit anything below this point --- #

        # Call up title string function to use for parsing
        title_string = get_title_string(title_soup)

        # Call up product type
        product_type =  get_type(title_string, url)

        # Call up title
        title = get_title(title_soup)
        # print(title)

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

driver.quit()


