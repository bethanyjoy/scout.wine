# vvsl_base_urls = [
# 	"https://vinovoresilverlake.com/collections/red",
# 	"https://vinovoresilverlake.com/collections/white",
# 	"https://vinovoresilverlake.com/collections/rose",
# 	"https://vinovoresilverlake.com/collections/orange",
# 	"https://vinovoresilverlake.com/collections/sparkling",
# ]

# # Define the number of pages for each base URL
# vvsl_pages = [5, 5, 3, 5, 5]


base_url = "https://vinovoresilverlake.com/collections/"
wine_types = {
    "red": 5,
    "white": 5,
    "rose": 3,
    "orange": 5,
    "sparkling": 5,
}

vinovore_silverlake_urls = [f"{base_url}{wine_type}" + (f"?page={i}" if i > 1 else "") for wine_type, pages in wine_types.items() for i in range(1, pages + 1)]