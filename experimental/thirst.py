base_url = "https://thirstmerchants.com/collections/wines?filter.p.m.custom.country="
countries_pages = {
    "Argentina": 1, 
    "Austria": 1, 
    "Chile": 1, 
    "France": 12,
    "Georgia": 1, 
    "Germany": 1, 
    "Italy": 4, 
    "Portugal": 1, 
    "Spain": 4, 
    "South+Africa": 1,
    "USA": 4
}

thirst_urls = []
for country, pages in countries_pages.items():
    for page in range(1, pages + 1):
        thirst_urls.append(base_url + country + "&page=" + str(page))