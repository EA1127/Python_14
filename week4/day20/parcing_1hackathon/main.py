import requests
from bs4 import BeautifulSoup as BSoup
import csv
from time import sleep

def get_html(url):
    r = requests.get(url)
    # print(r.status_code)
    # print(r.text)
    return r.text

def get_total_pages(html):
    soup = BSoup(html, 'lxml')
    pages_ul = soup.find('div', class_="pager-wrap").find('ul')
    last_page = pages_ul.find_all('li')[-1]
    total_pages = last_page.find('a').get('href').split('=')[-1]
    # print(total_pages)
    return int(total_pages)

def get_page_data (html):
    soup = BSoup(html, 'lxml')
    catalogue = soup.find('div', class_='list-view')
    phones = catalogue.find_all('div', class_='item product_listbox oh')
    # print(phones)
    for phone in phones:
        try:
            name = phone.find('div', class_='listbox_title').text.strip()
        except:
            name = 'just_phone'
        
        try:
            price = phone.find('div', class_='listbox_price').text.strip()
        except:
            price = 'Not indicated'

        try:
            img_link = phone.find('div', class_='listbox_img pull-left').find('img').get('src')
            if 'images/product' in img_link:
                img = 'https://www.kivano.kg' + img_link
            else:
                img = 'https:' + img_link
        except:
            img = 'https://media.istockphoto.com/photos/dog-on-the-phone-picture-id473502112?k=20&m=473502112&s=612x612&w=0&h=-XfSN-riSPMZ_ZA-5NtCPTLXtgJLdTFtQ5bBoGxguyQ='
        # print(name)
        # print(price)
        # print(img)

        data = {
            'name': name,
            'price': price,
            'img': img}
        # print(data)
        write_to_csv(data)

def write_headers():
    with open('phones_kivano.csv', 'a') as file:
        fieldnames = ['Name', 'Price', 'Photo']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

def write_to_csv(data):
    with open('phones_kivano.csv', 'a') as file:
        fieldnames = ['Name', 'Price', 'Photo']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow({'Name': data['name'], 'Price': data['price'], 'Photo': data['img']})

def main():
    with open('phones_kivano.csv', 'w') as file: pass
    write_headers()
    url_ = 'https://www.kivano.kg/mobilnye-telefony'
    # get_total_pages(get_html(url_))

    i = 1
    while i <= get_total_pages(get_html(url_)):
        url = f'https://www.kivano.kg/mobilnye-telefony?page={i}'
        print(url)
        html = get_html(url)
        catalogue = BSoup(html, 'lxml').find('div', class_='list-view')
        if not catalogue:
            break
        get_page_data(html)
        i += 1

while True:
    main()
    sleep(3600)