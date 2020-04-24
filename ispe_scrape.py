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
url = 'https://ispe.org/about/staff'
response = get_url(url)

if response is not None:
    clean_html = BeautifulSoup(response, 'html.parser')
    #print(clean_html.prettify())
    #email_info = clean_html.select("li a")
    email_unordered_list = clean_html.select("ul li")
    #print(email_unordered_list[66].prettify())
    for li_items in email_unordered_list:
        email_href = li_items.find('a')
        if (email_href['href']) and (email_href['href'].find("mailto:") > -1):
             email_address = email_href['href'].split('mailto:')[1].strip()
             name_only = email_href.get_text().strip()
             name_length = len(name_only)
             title = li_items.get_text()[name_length:].strip()
             if title:
                 print(name_only+"||"+title+"||"+email_address)
        #print(name_only,"<-",name_length)
        #print(email_href.get_text())
        # if (fields['href']) and (fields['href'].find("mailto:") > -1):
        #     print(fields['href'],fields.get_text())
