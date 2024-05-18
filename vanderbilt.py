# vanderbilt_base_urls = [
#     "https://vwm.wine/collections/red",
#     "https://vwm.wine/collections/white",
#     "https://vwm.wine/collections/orange-skin-contact",
#     "https://vwm.wine/collections/rose",
#     "https://vwm.wine/collections/sparkling-wine"
# ]

# # Define the number of pages for each base URL
# vanderbilt_pages = [15, 12, 4, 4, 4]


# https://vwm.wine/collections/france?filter.v.option.style=Red
# https://vwm.wine/collections/france?filter.v.option.style=Red&page=2
# https://vwm.wine/collections/france?filter.v.option.style=Pet+Nat+•+Methode+Ancestrale
# https://vwm.wine/collections/france?filter.v.option.style=Rosé
# https://vwm.wine/collections/france?filter.v.option.style=Rose
# https://vwm.wine/collections/france?filter.v.option.style=Sparkling
# https://vwm.wine/collections/france?filter.v.option.style=White

# https://vwm.wine/collections/italy?filter.v.option.style=Orange
# https://vwm.wine/collections/italy?filter.v.option.style=Orange+•+Skin+Contact
# https://vwm.wine/collections/italy?filter.v.option.style=Pet+Nat+•+Methode+Ancestrale
# https://vwm.wine/collections/italy?filter.v.option.style=Red
# https://vwm.wine/collections/italy?filter.v.option.style=Rosé
# https://vwm.wine/collections/italy?filter.v.option.style=Sparkling
# https://vwm.wine/collections/italy?filter.v.option.style=White

# https://vwm.wine/collections/usa?filter.v.option.style=Orange
# https://vwm.wine/collections/usa?filter.v.option.style=Orange+•+Skin+Contact



base_url = "https://vwm.wine/collections/"
countries_wine_types_pages = {
    "france": {
        "Orange": 1,
        "Orange+•+Skin+Contact": 1,
        "Pet+Nat+•+Methode+Ancestrale": 1,
        "Red": 8,
        "Rosé": 1,
        "Rose": 1,
        "Sparkling": 4,
        "White": 1,
    },
    "italy": {
        "Orange": 1,
        "Orange+•+Skin+Contact": 1,
        "Pet+Nat+•+Methode+Ancestrale": 1,
        "Red": 5,
        "Rosé": 1,
        "Rose": 1,
        "Sparkling": 1,
        "White": 2,
    },
    "usa": {
        "Orange": 1,
        "Orange+•+Skin+Contact": 1,
        "Pet+Nat+•+Methode+Ancestrale": 1,
        "Red": 8,
        "Rosé": 1,
        "Rose": 1,
        "Sparkling": 1,
        "White": 2,
    },
    "central-south-america": {
        "Orange": 1,
        "Orange+•+Skin+Contact": 1,
        "Pet+Nat+•+Methode+Ancestrale": 1,
        "Red": 2,
        "Rosé": 1,
        "Rose": 1,
        "Sparkling": 1,
        "White": 1,
    },
    "spain": {
        "Orange": 1,
        "Orange+•+Skin+Contact": 1,
        "Pet+Nat+•+Methode+Ancestrale": 1,
        "Red": 2,
        "Rosé": 1,
        "Rose": 1,
        "Sparkling": 1,
        "White": 1,
    },
    "portugal": {
        "Orange": 1,
        "Orange+•+Skin+Contact": 1,
        "Pet+Nat+•+Methode+Ancestrale": 1,
        "Red": 1,
        "Rosé": 1,
        "Rose": 1,
        "Sparkling": 1,
        "White": 1,
    },
    "austria": {
        "Orange": 1,
        "Orange+•+Skin+Contact": 1,
        "Pet+Nat+•+Methode+Ancestrale": 1,
        "Red": 1,
        "Rosé": 1,
        "Rose": 1,
        "Sparkling": 1,
        "White": 1,
    },
    "germany-1": {
        "Orange": 1,
        "Orange+•+Skin+Contact": 1,
        "Pet+Nat+•+Methode+Ancestrale": 1,
        "Red": 1,
        "Rosé": 1,
        "Rose": 1,
        "Sparkling": 1,
        "White": 2,
    },
    "other-europe": {
        "Orange": 1,
        "Orange+•+Skin+Contact": 1,
        "Pet+Nat+•+Methode+Ancestrale": 1,
        "Red": 3,
        "Rosé": 1,
        "Rose": 1,
        "Sparkling": 1,
        "White": 1,
    },
}

vanderbilt_urls = []
for country, wine_types_pages in countries_wine_types_pages.items():
    for wine_type, pages in wine_types_pages.items():
        for page in range(1, pages + 1):
            url = base_url + country + "?filter.v.option.style=" + wine_type + "&filter.v.availability=1"
            if page != 1:
                url += "&page=" + str(page)
            vanderbilt_urls.append(url)