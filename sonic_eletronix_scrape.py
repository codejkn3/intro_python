import requests
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup


def get_url(url):
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


def log_error(e):
    print(e)

#page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
#url = "http://dataquestio.github.io/web-scraping-pages/simple.html"
url = 'https://www.sonicelectronix.com/viewcat.php?category_id=1702&items_per_page=100'
response = get_url(url)

if response is not None:
    clean_html = BeautifulSoup(response, 'html.parser')

    product_container = clean_html.find_all(class_="addProductContainer")
    for current_product in product_container:
        #current_product = product_container[0]
        #print(current_product.prettify())

        container_info = current_product.find(class_="addToCartButton")
        product_name = container_info['data-name']
        product_price = container_info['data-price']


        print(product_name)
        print(product_price,"\n")
