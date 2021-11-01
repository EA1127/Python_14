import requests
from bs4 import BeautifulSoup as BS
import csv


def main():
    r = requests.get('https://vesti.kg/').text
    soup = BS(r, 'lxml')
    title_news = soup.find('div', class_ = 'itemList')
    # print(title_news)
    title_news_text = title_news.find_all('div', class_ = 'itemBody')
    news = []
    for i in title_news_text:
        news.append(i.find('a').text.strip())
    
    # print(news)

    with open('text.csv', 'w') as file:
        for i in news:
            i = i.replace(',', '')
            file.write(i + '\n')

main()
