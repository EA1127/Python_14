# import requests
# from bs4 import BeautifulSoup as BS
# import csv

# def get_url(url):
#     response = requests.get(url)
#     # print(response.status_code)
#     # print(response.text)
#     return response.text

# def get_html(html):
#     soup = BS(html, 'lxml')
#     category = soup.find('div', class_ = 'main-nav__container').find('ul', class_ = 'main-nav__first-level-list')
#     # print(category)
#     koko = []
#     for i in category:
#         koko.append(i.text)
#     print(koko)

# def main():
#     url = "https://lalafo.kg/"
#     get_html(get_url(url))

# def main():
#     html = requests.get('https://lalafo.kg/').text
#     soup = BS(html, 'lxml')
#     category = soup.find('div', class_ = 'main-nav__container').find('ul', class_ = 'main-nav__first-level-list')
#     try:
#         category = soup.find('div', class_ = 'main-nav__container').find('ul', class_ = 'main-nav__first-level-list')
#     except:
#         print(category)
#     koko = []
#     for i in category:
#         koko.append(i.text)
#     print(koko)
#     with open('text.csv', 'w') as file:
#         file.writelines([i + '\n' for i in koko])

# main()
