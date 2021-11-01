import requests
from bs4 import BeautifulSoup


def get_html(url):
    response = requests.get(url)
    # print(response.status_code)
    # print(response.text)
    return response.text


def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    # print(soup.prettify())
    pages_ul = soup.find('div', class_="col-md-6 offset-md-2 pr-0").find('ul')
    last_page = pages_ul.find_all('li')[-2]
    total_pages = last_page.find('a').get('href').split('=')[-1]
    # print(total_pages)
    return int(total_pages)

def get_page_data (html):
    soup = BeautifulSoup(html, 'lxml')
    product_list = soup.find('div', {"id":"js-product-list"}).find('div', class_="products").find_all('article', class_="product-miniature")
    # print(product_list)


    products = product_list.find('h2', class_="h3 product-title")
    print(products)


def main():
    notebooks_url = 'https://systema.kg/71-noutbuki-bishkek'
    pages = '?page='
    get_page_data(get_html(notebooks_url))
    get_total_pages(get_html(notebooks_url))

main()