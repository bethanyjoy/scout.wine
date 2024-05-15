base_url = "https://flaskandfield.com/collections/wine?filter.p.product_type={}&filter.p.m.custom.region={}"
product_types = ["Red+Wine", "Rosé+Wine", "Skin+Contact+Wine", "Sparkling+Wine", "White+Wine"]
regions = ["Argentina", "Austria", "Australia", "California", "Chile", "France", "Georgia+%28country%29", "Germany", "Italy", "Lebanon", "Morocco", "Oregon", "Portugal", "South+Africa", "Spain", "USA"]

faf_urls = [base_url.format(product_type, region) for product_type in product_types for region in regions]