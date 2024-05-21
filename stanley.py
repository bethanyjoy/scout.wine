# stanley_urls = [
#     "https://www.stanleys.la/shop/wine/wine-by-type/sparkling/?limit=72",
#     "https://www.stanleys.la/shop/wine/wine-by-type/sparkling/page2.html?limit=72",
#     "https://www.stanleys.la/shop/wine/wine-by-type/whites/?limit=72",
#     "https://www.stanleys.la/shop/wine/wine-by-type/whites/page2.html?limit=72",
#     "https://www.stanleys.la/shop/wine/wine-by-type/whites/page3.html?limit=72",
#     "https://www.stanleys.la/shop/wine/wine-by-type/orange/?limit=72",
#     "https://www.stanleys.la/shop/wine/wine-by-type/orange/page2.html?limit=72",
#     "https://www.stanleys.la/shop/wine/wine-by-type/rose/?limit=72",
#     "https://www.stanleys.la/shop/wine/wine-by-type/rose/page2.html?limit=72",
#     "https://www.stanleys.la/shop/wine/wine-by-type/chillable-red/?limit=72",
#     "https://www.stanleys.la/shop/wine/wine-by-type/chillable-red/page2.html?limit=72",
#     "https://www.stanleys.la/shop/wine/wine-by-type/reds/?limit=72",
#     "https://www.stanleys.la/shop/wine/wine-by-type/reds/page2.html?limit=72",
#     "https://www.stanleys.la/shop/wine/wine-by-type/reds/page3.html?limit=72",
#     "https://www.stanleys.la/shop/wine/wine-by-type/reds/page4.html?limit=72",
#     "https://www.stanleys.la/shop/wine/wine-by-type/reds/page5.html?limit=72",
#     "https://www.stanleys.la/shop/wine/wine-by-type/reds/page6.html?limit=72",
#     "https://www.stanleys.la/shop/wine/wine-by-type/reds/page7.html?limit=72",
# ]

base_url = "https://www.stanleys.la/shop/wine/wine-by-type/"
wine_types = ["sparkling", "whites", "orange", "rose", "chillable-red", "reds"]
pages = {
    "sparkling": 1,
    "whites": 2,
    "orange": 1,
    "rose": 1,
    "chillable-red": 1,
    "reds": 4
}

stanley_urls = [f"{base_url}{wine_type}/page{i}.html?limit=72" for wine_type in wine_types for i in range(1, pages[wine_type] + 1)]