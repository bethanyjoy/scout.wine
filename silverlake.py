base_url = "https://silverlakewine.com/collections/"
wine_types = {
    "red": 1,
    "white": 2,
    "rose": 1,
    "orange": 3,
    "sparkling": 1,
    "fruit-wine": 1,
    # "piquette": 1,
    "chillable": 1
}

silverlake_urls = [f"{base_url}{wine_type}" + (f"?page={i}" if i > 1 else "") for wine_type, pages in wine_types.items() for i in range(1, pages + 1)]