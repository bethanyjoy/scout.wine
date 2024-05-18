# urls = [
#     "https://www.strangerwinesnyc.com/red/country/france/",
#     "https://www.strangerwinesnyc.com/red/country/chile/",
#     "https://www.strangerwinesnyc.com/red/country/italy/",
#     "https://www.strangerwinesnyc.com/red/country/spain/",
#     "https://www.strangerwinesnyc.com/red/country/usa/",
#     "https://www.strangerwinesnyc.com/white/country/austria/",
#     "https://www.strangerwinesnyc.com/white/country/france/",
#     "https://www.strangerwinesnyc.com/white/country/germany/",
#     "https://www.strangerwinesnyc.com/white/country/italy/",    
#     "https://www.strangerwinesnyc.com/white/country/spain/",
#     "https://www.strangerwinesnyc.com/white/country/usa/",
# ]

base_url = "https://www.strangerwinesnyc.com/"
wine_types = ["red", "white", "rose", "sparkling", "orange"]
countries = ["argentina", "austria", "australia", "chile", "croatia", "czech-republic", "france", "georgia", "germany", "greece", "italy", "japan", "lebanon", "new-zealand", "portugal", "slovenia", "south-africa", "spain", "usa", "mexico", "luxembourg", "hungary", "austrailia", "slovakia"]

sw_urls = []
for wine_type in wine_types:
    for country in countries:
        url = base_url + wine_type + "/country/" + country + "/"
        sw_urls.append(url)