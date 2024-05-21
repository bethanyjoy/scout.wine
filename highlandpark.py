base_url = "https://highlandparkwine.com/collections/"
wine_types = {
    "usa-red-wines": 7,
    "french-reds": 8,
    "italian-reds": 4,
    "spanish-portuguese-reds": 3,
    "eastern-european-reds": 3,
    "reds-from-the-southern-hemisphere": 4,
    "white-wines-from-the-usa": 4,
    "french-white-wine": 5,
    "italian-white-wine": 4,
    "spanish-portuguese-whites": 3,
    "eastern-european-whites": 3,
    "white-wines-from-the-southern-hemisphere": 3,
    "rose": 5,
    "orange-wine": 6,
    "sparkling-wine": 6,
    "chillable-reds": 6,
}

highlandpark_urls = [f"{base_url}{wine_type}" + (f"?page={i}" if i > 1 else "") for wine_type, pages in wine_types.items() for i in range(1, pages + 1)]