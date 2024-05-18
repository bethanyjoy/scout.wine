# tw_base_urls = [
# 	"https://tomorrowswine.com/collections/reds",
#     "https://tomorrowswine.com/collections/whites",
#     "https://tomorrowswine.com/collections/rose",
#     "https://tomorrowswine.com/collections/orange",
#     "https://tomorrowswine.com/collections/sparkling"
# ]

# # Define the number of pages for each base URL
# tw_pages = [12, 8, 3, 5, 5]



base_url = "https://tomorrowswine.com/collections/all/"
colors = ["red", "white", "rose", "orange", "sparkling", "pet-nat"]
countries = ["united-states", "france", "spain", "italy", "austria", "eastern-europe", ""]

tw_urls = [base_url + color + "+" + country for color in colors for country in countries]