# ss_base_urls = [
#     "https://www.sipsnackshop.com/collections/red-wine-white-wine-bubbles/champagne",
# 	"https://www.sipsnackshop.com/collections/red-wine-white-wine-bubbles/chillable-red",
#     "https://www.sipsnackshop.com/collections/red-wine-white-wine-bubbles/orange-wine",
# 	"https://www.sipsnackshop.com/collections/red-wine-white-wine-bubbles/pet-nat",
#     "https://www.sipsnackshop.com/collections/red-wine-white-wine-bubbles/red",
# 	"https://www.sipsnackshop.com/collections/red-wine-white-wine-bubbles/red-wine",
# 	"https://www.sipsnackshop.com/collections/red-wine-white-wine-bubbles/rose",
# 	"https://www.sipsnackshop.com/collections/red-wine-white-wine-bubbles/rose-wine",
# 	"https://www.sipsnackshop.com/collections/red-wine-white-wine-bubbles/sparkling-wine",
# 	"https://www.sipsnackshop.com/collections/red-wine-white-wine-bubbles/white",
# 	"https://www.sipsnackshop.com/collections/red-wine-white-wine-bubbles/white-wine",
# ]

# # Define the number of pages for each base URL
# ss_pages = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]



base_url = "https://sipsnackshop.com/collections/red-wine-white-wine-bubbles/"
wine_types = {
    "champagne": 2,
    "chillable-red": 2,
    "orange-wine": 2,
    "pet-nat": 2,
    "red": 2,
    "red-wine": 2,
	"rose": 2,
	"rose-wine": 2,
    "sparkling-wine": 2,
    "white": 2,
    "white-wine": 2
}
sipsnack_urls = [f"{base_url}{wine_type}" + (f"?page={i}" if i > 1 else "") for wine_type, pages in wine_types.items() for i in range(1, pages + 1)]