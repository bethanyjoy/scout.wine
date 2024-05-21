# vver_base_urls = [
# 	"https://vinovoreeaglerock.com/collections/red",
# 	"https://vinovoreeaglerock.com/collections/white",
# 	"https://vinovoreeaglerock.com/collections/orange",
# 	"https://vinovoreeaglerock.com/collections/rose",
# 	"https://vinovoreeaglerock.com/collections/sparkling",
# ]

# # Define the number of pages for each base URL
# vver_pages = [8, 6, 4, 4, 6]

base_url = "https://vinovoreeaglerock.com/collections/"
wine_types = {
    "red": 8,
    "white": 6,
    "rose": 4,
    "orange": 4,
    "sparkling": 6,
}

vinovore_eaglerock_urls = [f"{base_url}{wine_type}" + (f"?page={i}" if i > 1 else "") for wine_type, pages in wine_types.items() for i in range(1, pages + 1)]