we_urls = [
	"https://wineandeggs.com/collections/red-wine",
	"https://wineandeggs.com/collections/white-wine",
	"https://wineandeggs.com/collections/wine-rose",
	"https://wineandeggs.com/collections/skin-contact-wine",
	"https://wineandeggs.com/collections/sparkling-wine",
	"https://wineandeggs.com/collections/co-fermented",
	"https://wineandeggs.com/collections/piquette-wine",
]

# Archived Code

# # Wine + Eggs

# for url in we_urls:

# 	# Define store
# 	store = 'Wine + Eggs'

# 	# Define how to target a product
# 	products = get_products(url, "div", "product-block")

# 	for product in products:

# 		# Define how to target the title (don't need to format)
# 		title_name = product.find("h3", class_="product-block__title").text.strip().lower()
# 		title_maker = product.find("div", class_="italicized-text").text.strip().lower()
# 		title = title_maker + " " + title_name

# 		# Call up product type (don't need to edit)
# 		product_type =  get_type(title_name, url)

# 		# Define how to target + format the price
# 		price = get_price(product, "div", "product-block__price")

# 		# Define images
# 		image_code = get_noscript(product).find("div", class_="product-block__image")['style']
# 		image_src = image_code.strip("background-image:url('").strip("');")
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
# 			'Maker': lookup_maker(title_maker.replace(" ", "")),
# 			'Maker_class': get_maker_class(title_maker.replace(" ", "")),
# 			'Price': price,
# 			'Region': lookup_region(url),
# 			'Store': store,
# 			'Store_class': get_store_class(store),
# 			'Title': title,
# 			'Type': product_type,
# 			'Type_class': get_type_class(product_type)
# 		})