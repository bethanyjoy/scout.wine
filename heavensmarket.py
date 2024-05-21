# hm_base_urls = [
#     "https://www.heavensmarketla.com/collections/sparkling",
#     "https://www.heavensmarketla.com/collections/white",
#     "https://www.heavensmarketla.com/collections/skin-contact",
#     "https://www.heavensmarketla.com/collections/rose",
# 	"https://www.heavensmarketla.com/collections/red",
# ]

# # Define the number of pages for each base URL
# hm_pages = [2, 3, 2, 2, 5]





base_url = "https://www.heavensmarketla.com/collections/"
wine_types = {
    "red": 5,
    "white": 3,
    "rose": 2,
    "skin-contact": 2,
    "sparkling": 2,
}

heavensmarket_urls = [f"{base_url}{wine_type}" + (f"?page={i}" if i > 1 else "") for wine_type, pages in wine_types.items() for i in range(1, pages + 1)]