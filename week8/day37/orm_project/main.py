import requests
from bs4 import BeautifulSoup

TOTAL_PAGES = 6

def get_html(url):
    response = requests.get(url)
    return response.text

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    grid = soup.find('div', class_='grid-deputs')
    dep_list = grid.find_all('div', class_='dep-item')
    # return dep_list

    deputy_info = []
    for dep in dep_list:
        name = dep.find('a', class_='name').text
        fraction = dep.find('div', class_='info').text
        try:
            tel = dep.find('a', class_='phone-call').find('span').text
        except:
            tel = ''
        deputy_info.append((name, fraction, tel))
    return deputy_info

def main():
    deputy_total = []
    for page in range(1, TOTAL_PAGES+1):
        kenesh_url = f"http://kenesh.kg/ru/deputy/list/35?page={page}"
        html = get_html(kenesh_url)
        data = get_data(html)
        deputy_total.extend(data)
    return deputy_total

# print(main())
# print(len(main()))

if __name__ == '__main__':
    main()
