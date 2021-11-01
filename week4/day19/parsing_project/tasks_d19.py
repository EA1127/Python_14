"""
Задание 1

Нужно получить статус запроса доступа к странице:
https://stackoverflow.com/questions
присвойте результат запроса к переменной source и выведите эту переменную в консоль.
Примерный вывод в консоли:
200 
"""
# import requests
# source = requests.get('https://stackoverflow.com/questions').status_code
# print(source)


"""
Задание 2

Спарсите тэги h1, p и ссылку с тэга a из веб-страницы:
http://www.example.com/
и выведите результат в консоль в таком виде:
h1:  Example Domain
p:  This domain is for use in illustrative examples in documents. You may use this domain in literature without prior coordination or asking for permission.
a:  https://www.iana.org/domains/example  
"""
# html_text = requests.get('http://www.example.com/').text
# soup = BeautifulSoup(html_text, 'lxml')
# a = soup.find("a").get('href')
# p = soup.find('p').text
# h1 = soup.find('h1').text

"""
Задание 3

Выведите с главной страницы википедии:
https://www.wikipedia.org/

сколько всего статей есть немецком языке.
Вывод в консоль должен быть таким:

Deutsch
2 590 000+ Artikel 
"""



"""
Задание 4

Напишите программу которая проверяет имеет ли страница заголовок(тэг h1) или нет.
Для этого напишите функцию getTitle() которая будет принимать url страницы и возвращать заголовок если он есть, если же его нет то будет возвращать "Title could not be found"

 print(getTitle('http://www.example.com/'))
Output:

 <h1>Example Domain</h1>
"""

"""
Задание 5

На странице:
https://www.makers.kg
есть названия курсов которые предлагает Makers.
Спарсите названия курсов и выведите в консоль:
Founders  
Coding Bootcamp  
Junior Club  
Studio 
"""
# import requests
# from bs4 import BeautifulSoup
# html_text = requests.get('https://www.makers.kg').text
# soup = BeautifulSoup(html_text, 'lxml')
# all_ = soup.find_all('h3', class_ = "feature-cards-card-info-title")
# for i in all_:
#     print(i.text)



"""
Задание 6

Выведите ссылки на все картинки к каждому из курсов:

Founders
Coding Bootcamp
Junior Club
Studio

В HTML страницы путь к картинке указан неполный:

"./assets/5fa63c0bbfbadb648dc12062/5fa63c0c40384a6339fabfdc_95c1a1c.png" 
вам нужно сделать так, чтобы ссылка была выведена в виде:

https://www.makers.kg/assets/5fa63c0bbfbadb648dc12062/5fa63c0c40384a6339fabfdc_95c1a1c.png  
при переходе по ссылке, она должна быть рабочей и выводить картинку
"""

"""



Задание 7

Теперь спарсите и выведите в консоль описание к каждому курсу.
Например:
Обучаем SMM и digital маркетингу на реальном проекте.  Курс охватывает глубокие знания маркетинга и продаж.
"""
# import requests
# from bs4 import BeautifulSoup
# html_text = requests.get('https://www.makers.kg').text
# soup = BeautifulSoup(html_text, 'lxml')
# all_ = soup.find_all('div', class_="feature-cards-card-info-subtitle")
# for i in all_:
#     print(i.text)
"""

Задание 8

Создайте функцию get_info() которая принимает url:

https://www.makers.kg

Функция должна записывать заголовок, описание к курсу и ссылку на картинку в список list_ в виде словаря для каждого курса.
Ключами в словарях должны быть строки 'name','description', 'image_link', а значениями сами заголовки, описания и ссылки на 
картинки(ссылка также должна быть полной и рабочей).
Выведите данный список в консоль:

print(get_info('https://www.makers.kg')) 
Примерный вывод:

[{'name': 'Founders', 'description': 'Обучаем SMM и digital маркетингу на реальном проекте. Курс охватывает глубокие знания 
маркетинга и продаж.', 'image_link': 'https://www.makers.kg/assets/5fa63c0bbfbadb648dc12062/5fa63c0c40384a6339fabfdc_95c1a1c.png'}, 

{'name': 'Coding Bootcamp', 'description': 'Первый bootcamp по программированию в Кыргызстане. Обучение идет на реальных проектах 5 
дней в неделю по 8 часов на протяжении 3 месяцев.', 'image_link': 
'https://www.makers.kg/assets/5fa63c0bbfbadb648dc12062/5fa63c0c40384a0abffabfd5_5a615b4.png'},

{'name': 'Junior Club', 'description': 'Обучение программированию для продвинутых разработчиков. По окончанию лучшие выпускники могут
 получить работу в компаниях-партнерах', 'image_link': 'https://www.makers.kg/assets/5fa63c0bbfbadb648dc12062/5fa63c0c40384a54c1fabfd3_1db079d.png'}

{'name': 'Studio', 'description': 'Разработка сайтов, приложений и ПО для бизнеса и организаций. Консультация по внедрению 
IT решений.', 'image_link': 'https://www.makers.kg/assets/5fa63c0bbfbadb648dc12062/5fa63c0c40384a2686fabfd7_79c8646.png'}] 
MAIN.PY

"""

"""
Задание 9

Напишите код который сохраняет все названия категорий со страницы:

https://enter.kg/
в список category_list.
После, напишите функцию которая имеет два параметра - список категорий - categories и ключевое слово - keyword.
Функция должна производить поиск по ключевому слову в списке заголовков category_list и возвращать список заголовков 
которые содержат данное слово (независимо от регистра).

К примеру:
print(find_category(category_list, 'Ноутбуки')) 
Вывод будет:
['Ноутбуки, Ультрабуки, Гот. решения (1281)', 'Ноутбуки (1235)', 'Ноутбуки, Ультрабуки, Гот. решения(1281)', 'Ноутбуки и ультрабуки'] 
"""




"""
-- Задание 10 --

Напишите программу которая будет парсить топ 250 фильмов с сайта IMBD:
http://www.imdb.com/chart/top
Затем напишите функцию get_link, которая будет принимать в аргументы список фильмов - title_list и строку - name. Функция должна 
производить поиск в списке по строке и возвращать ссылку на фильм. Вы должны вернуть только первое совпадение в списке.

Например:
get_link(title_list, 'shawshank') 
Вернет вам:

https://www.imdb.com/title/tt0111161/ 
"""
# import requests
# from bs4 import BeautifulSoup
# html_text = requests.get('https://www.imdb.com/chart/top').text
# soup = BeautifulSoup(html_text, 'lxml')
# title_list = soup.find_all('td', class_ = "titleColumn")

# def get_link(title_list, name):
#     for title_ in title_list:
#         if name.lower() in title_.find('a').text.lower():
#             return'https://www.imdb.com' + title_.find("a").get("href")

# print(get_link(title_list, 'shawshank'))






# task 
# import requests
# from bs4 import BeautifulSoup
# html_text = requests.get('https://www.makers.kg').text
# soup = BeautifulSoup(html_text, 'lxml')
# Founders = soup.find('h3', class_ ="feature-cards-card-info-title").text
# print(Founders)



# task 
import requests
from bs4 import BeautifulSoup
html_text = requests.get('https://www.makers.kg').text
soup = BeautifulSoup(html_text, 'lxml')
all_ = soup.find_all('img', class_ = "feature-cards-card-image")
for i in all_:
    print(i.get('src'))






# task 
# import requests
# from bs4 import BeautifulSoup
# def get_info(url):
#     list_ = []
#     html_text = requests.get('https://www.makers.kg').text
#     soup = BeautifulSoup(html_text, 'lxml')
#     all_ = soup.find_all('h3', class_ = "feature-cards-card-info-title")
#     for i in all_:
#         dict_ = {'name':i.text}
#         list_.append(dict_)

#     html_text = requests.get('https://www.makers.kg').text
#     soup = BeautifulSoup(html_text, 'lxml')
#     all_ = soup.find_all('div', class_="feature-cards-card-info-subtitle")
#     f = 0
#     for i in all_:
#         list_[f]['description'] = i.text
#         f += 1
        
#     html_text = requests.get('https://www.makers.kg').text
#     soup = BeautifulSoup(html_text, 'lxml')
#     all_ = soup.find_all('img', class_ = "feature-cards-card-image")
#     k = 0
#     for i in all_:
#         i = "https://www.makers.kg" +i.get('src').replace('.','',1)
#         list_[k]['image_link'] = i
#         k += 1
        
#     return list_

# print(get_info('https://www.makers.kg')) 


# task 
# import requests
# from bs4 import BeautifulSoup
# category_list = []
# html_text = requests.get('https://enter.kg/').text
# soup = BeautifulSoup(html_text, 'lxml')
# li = soup.find_all('li', class_ = "VmClose")
# for i in li:
#     if i.find('a'):
#         k = i.find('a')
#         category_list.append(k.text)
# print(category_list)


# task 
# import requests
# from bs4 import BeautifulSoup
# category_list = []
# html_text = requests.get('https://enter.kg/').text
# soup = BeautifulSoup(html_text, 'lxml')
# li = soup.find_all('li', class_ = "VmClose")
# for i in li:
#     if i.find('a'):
#         k = i.find('a')
#         category_list.append(k.text)
# def find_category(categories, keyword):
#     for_print=[]
#     for i in categories:
#         if str(keyword).lower() in i.lower():
#             for_print.append(i)
#     return for_print
# print(category_list)
# print((find_category(category_list, 'Ноутбуки')))


# task 
# import requests
# from bs4 import BeautifulSoup
# html_text = requests.get('https://enter.kg/').text
# soup = BeautifulSoup(html_text, 'lxml')
# li = soup.find_all('li', class_ = "VmClose")
# category_list = [i.find('a').text for i in li if i.find('a')]
# category_list = [i.text.strip() for i in li]
# def find_category(categories, keyword):
#     return [item for item in categories if keyword.lower() in item.lower()]
# print((find_category(category_list, 'Ноутбуки')))
# print(category_list)


# task 
# import requests
# from bs4 import BeautifulSoup
# html_text = requests.get('http://www.imdb.com/chart/top').text
# soup = BeautifulSoup(html_text, 'lxml')
# li = soup.find_all('td', class_ = "titleColumn")
# title_list = [i.find('a').text for i in li]
# link_list = [i.find('a').get('href') for i in li]
# def get_link(title_list, name):
#     for name_ in title_list:
#         if name.lower() in name_.lower():
#             index_ = title_list.index(name_)
#             print('https://www.imdb.com' + link_list[index_])
# get_link(title_list, 'roOM') 


