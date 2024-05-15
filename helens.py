base_url = "https://helenswines.com/collections"
collections = ["sparkling", "white", "rose", "red", "orange"]
countries = ["australia", "austria", "chile", "corsica", "domestic", "france", "germany", "italy", "portugal", "spain"]

helens_urls = []

for collection in collections:
    for country in countries:
        helens_urls.append(f"{base_url}/{collection}/{country}")