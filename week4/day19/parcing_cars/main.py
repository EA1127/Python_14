import requests
from bs4 import BeautifulSoup as BS

import csv

def get_html(url):
    response = requests.get(url)
    # print(response.status_code)
    # print(response.text)
    return response.text

def get_data(html):
    soup = BS(html, 'lxml')
    catalog = soup.find('div', class_='catalog-list')
    cars = catalog.find_all('a', class_='catalog-list-item')
    # print(cars)
    for car in cars:
        try:
            title = car.find('span', class_='catalog-item-caption').text.strip()
        except:
            title = 'A car'

        try:
            img = car.find('img', class_='catalog-item-cover-img').get('src')
        except:
            img = 'data:image/png;base64,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'

        try:
            price = car.find('span', class_="catalog-item-price").text.strip()
        except:
            price = 'Dogovornaya'
        # print(title, img, price)

        data = {
            'title': title,
            'price': price,
            'img': img
        }
        write_to_csv(data)


def write_headers():
    with open('cars.csv', 'a') as file:
        fieldnames = ['Name', 'Price', 'Photo']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

def write_to_csv(data):
    with open('cars.csv', 'a') as file:
        fieldnames = ['Name', 'Price', 'Photo']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow({'Name': data['title'], 'Price': data['price'], 'Photo': data['img']})

def main():
    with open('cars.csv', 'w') as file: pass
    write_headers()
    
    i = 1
    while True:
        cars_url = f'https://cars.kg/offers/{i}?vendor=57fa24ee2860c45a2a2c0905'
        html = get_html(cars_url)
        catalog = BS(html, 'lxml').find('div', class_='catalog-list')
        if not catalog:
            break
        get_data(html)
        i += 1

main()