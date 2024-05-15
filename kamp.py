base_url = "https://shopkamp.com/collections/"
wine_types = ["red", "chillable-reds", "white", "rose", "orange", "sparkling"]
countries = ["austria", "california", "france", "germany", "greece", "italy", "oregon", "portugal", "spain"]

kamp_urls = [f"{base_url}{wine_type}/{country}" for wine_type in wine_types for country in countries]