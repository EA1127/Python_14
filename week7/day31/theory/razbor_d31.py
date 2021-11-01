"""
1) Используйте файл HarryPotterBooks.json. 

Напишите скрипт, который соберет все даты выпуска книг, 
посчитает их среднее арифметическое и запишит получившееся
число в файл result.txt

{
   "books": [
       {
           "title": "Philosopher's Stone",
           "year": 1997
       },
       {
           "title": "Chamber of Secrets",
           "year": 1998
       },
       {
           "title": "Prisoner of Azkaban",
           "year": 1999
       },
       {
           "title": "Goblet of Fire",
           "year": 2000
       },
       {
           "title": "Order of the Phoenix",
           "year": 2003
       },
       {
           "title": "Half-Blood Prince",
           "year": 2005
       },
       {
           "title": "Deathly Hallows",
           "year": 2007
       }
   ]
}
"""

import json
import functools

with open('HarryPotterBooks.json') as my_file:
    data = json.load(my_file)
    my_list = data['books']
    # print(my_list)

    years = [my_dict.get('year') for my_dict in my_list]
    print(years)

    average_year1 = round(sum(years) / len(years), 1)
    print(average_year1)

    summa = functools.reduce(lambda x, y: x+y, years)
    average_year2 = round(summa / len(years), 2)
    print(average_year2)

with open('result.txt', 'w') as my_file:
    my_file.write(f'{average_year1} or {average_year2}')



