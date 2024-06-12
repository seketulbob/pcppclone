import requests
from bs4 import BeautifulSoup
from .models import Product

def scrape():
    url = 'https://shopee.com.my/search?keyword=pc%20parts'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    for item in soup.select('.shopee-search-item-result__item'):
        name = item.select_one('.yQmmFK._1POlWt._36CEnF').text.strip()
        price = item.select_one('.zp9xm9.kNGSLn.l-u0xK').text.strip()
        item_url = 'https://shopee.com.my' + item.select_one('a')['href']
        source = 'Shopee'

        Product.objects.create(name=name, price=price, url=item_url, source=source)