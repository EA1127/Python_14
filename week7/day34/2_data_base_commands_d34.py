
""" ----------------------- Варианты операций: SELECT, INSERT, UDPATE, DELETE, ALTER TABLE ----------------------- """

#   * примечание: большие буквы - это ЗАПРОСЫ psql (точка с запятой это обязательная часть запроса), 
#   а маленькие это по сути введенные нами слова или переменные или команды, 

"""



1. SELECT column-1, column-2, column-3 FROM table_name;
    (покзать таблицу со столбцами column-1, column-2, column-3)

2. SELECT * FROM table_name;
    (показать всю таблицу)

3. INSERT INTO table_name (name_column-1, name_column-2, name_column-3...name_column-n) VALUES (value-1, value-2, value-3...value-n);
    (вставить в таблицу столбцы name_column-1, name_column-2, name_column-3...name_column-n со значениями value-1, value-2, value-3...value-n)

4. SELECT name_column-1 || ' ' || name_column-2 FROM table_name;
    (покзать таблицу с объединенными столбцами name_column-1, name_column-2 через пробел - то есть оlин стобец [name_column-1 name_column-2])

5. SELECT name_column-1 || ' ' || name_column-2 AS "new name_column" FROM table_name;
    (покзать таблицу с объединенными столбцами name_column-1, name_column-2 через пробел и с новым названием столбца полученных из объединенных)

6. SELECT name_column-1 || ' ' || name_column-2 AS "new name_column", name_column-3 FROM table_name;
    (покзать таблицу с объединенными столбцами name_column-1, name_column-2 через пробел (с новым названием столбца полученных из объединенных) 
    и столбца name_column-3

7. SELECT name_column-1, name_column-2 AS new_name_column-2 FROM table_name;
    (показать таблицу со столбцами name_column-1 и name_column-2 но с измененным названием столбца name_column-2)

8. SELECT name_column-1 AS new_name_column-1, name_column-2 AS new_name_column-3 FROM table_name;
    (показать таблицу со столбцами name_column-1 и name_column-2 но с измененными названиями обоих столбцов)

9. SELECT * FROM table_name ORDER BY name_column-2;
    (показать всю таблицу отсортированную по столбцу name_column-2 (по алфавиту или по возрастанию - по дефолту стоит ASC));

10. SELECT * FROM table_name ORDER BY name_column-1 DESC;
    (показать всю таблицу отсортированную по столбцу name_column-1 (по убыванию));

11. SELECT * FROM table_name ORDER BY name_column-2 ASC, name_column-1 DESC;
    (показать всю таблицу отсортированную по столбцу name_column-2 по возрастанию и по столбцу name_column-1 по убыванию);

12. SELECT * FROM table_name ORDER BY name_column-2 ASC NULLS FIRST;
    (показать всю таблицу отсортированную по столбцу name_column-2 по возрастанию, но при этом чтобы строки с нулевыми значениями были вверху)

13. SELECT * FROM table_name ORDER BY name_column-2 ASC NULLS LAST;
    (показать всю таблицу отсортированную по столбцу name_column-2 по возрастанию, но при этом чтобы строки с нулевыми значениями были снизу)

14. Пример создания типа данных ENUM:
    postgres=# CREATE TYPE condition AS ENUM ('new', 'used', 'fixed');
    CREATE TYPE
(* примечание: condition - это название типа ENUM)

15. Пример создания таблицы!!!:

    postgres=# CREATE TABLE Car(
    postgres(# id SERIAL PRIMARY KEY,
    postgres(# brand VARCHAR(50) NOT NULL,
    postgres(# model VARCHAR(50) NOT NULL,
    postgres(# state condition DEFAULT 'new',
    postgres(# price MONEY,
    postgres(# is_registered BOOL DEFAULT True,
    postgres(# date_of_release DATE);
    CREATE TABLE
(* примечание: SERIAL - это тип данных,
               PRIMARY KEY - это ограниечение (constraint) NUT NULL и UNIQUE
               VARCHAR(50) - это тип данных - текст с 50-тью символами, если меньше 50-ти то остальные свободны (при CHAR свободные не бывают))
               DEFAULT 'new' - дефолтное значение 'new'
               MONEY - это тип данных
               BOOL DEFAULT True - это тип данных, дефолтное значение TRUE
               DATE - это тип данных

16. ПРИМЕР - Показать всю таблицу с использованием условного выражения WHERE:
    postgres=# SELECT * FROM car WHERE is_registered = True;
(* примечание: здесь показали всю таблицу, но с уловием что все машины (car) отвечают условию is_registered = True)

17. ПРИМЕР - Показать таблицу с использованием условного выражения WHERE, AND, OR, NOT:
    postgres=# SELECT * FROM car WHERE state = 'new';
    mydb=# SELECT * FROM info WHERE country = 'Kyrgyzstan';
    mydb=# SELECT * FROM info WHERE age > 20;
    mydb=# SELECT * FROM info WHERE experiance <=3;
    mydb=# SELECT name || ' ' || last_name AS "ful name", experiance FROM info WHERE experiance >= 4;
    mydb=# SELECT name, last_name, email FROM info WHERE last_name <> 'Snow';
    mydb=# SELECT name, last_name, email FROM info WHERE last_name <> 'Snow' AND name <> 'Zain';
    mydb=# SELECT name, last_name, email FROM info WHERE last_name = 'Snow' OR name = 'Malik';
    mydb=# SELECT name, last_name, email FROM info WHERE NOT last_name = 'Snow';

18. ПРИМЕР - Показать таблицу с использованием выражения IN:
    mydb=# SELECT name, last_name, country FROM info WHERE NOT country IN ('USA', 'Great Britain', 'Kyrgyzstan');
    mydb=# SELECT name, last_name, country FROM info WHERE country IN ('India', 'Russia', 'Germany');

19. ПРИМЕР - Показать всю таблицу с использованием выражения BETWEEN:
    mydb=# SELECT * FROM info WHERE age BETWEEN 20 AND 30;        если тип данных чисел INTEGER
    mydb=# SELECT * FROM info WHERE age BETWEEN '20' AND '30';    если тип данных чисел  MONEY
    mydb=# SELECT * FROM info WHERE (experiance BETWEEN 3 AND 6) and (age BETWEEN 25 and 30);

20. ПРИМЕР - Показать таблицу с использованием выражения DISTINCT:
    mydb=# SELECT DISTINCT country FROM info;       покажет все country без повтора
    mydb=# SELECT DISTINCT programming_language FROM info;
        programming_language 
        ----------------------
        Python
        Javascript
        (2 rows)

    mydb=# SELECT DISTINCT ON (country) country, last_name FROM info ORDER BY country, last_name;
            country    |   last_name    
        ---------------+----------------
        Australia     | Kiddo
        Canada        | Deadpool
        China         | Chi
        Germany       | Smartungschaft
        Great Britain | Chart
        India         | Malik
        Island        | Snow
        Japan         | Reeves
        Kyrgyzstan    | Ataibekov
        Norway        | Asgardson
        Russia        | Sharapova
        USA           | Gray
        (12 rows)

    mydb=# SELECT DISTINCT ON (country) country, last_name FROM info ORDER BY country;
            country    |   last_name    
        ---------------+----------------
        Australia     | Kiddo
        Canada        | Deadpool
        China         | Chi
        Germany       | Smartungschaft
        Great Britain | Chart
        India         | Malik
        Island        | Snow
        Japan         | Reeves
        Kyrgyzstan    | Jannetova
        Norway        | Asgardson
        Russia        | Sharapova
        USA           | 
        (12 rows)

----------------------------------------------------------------------------------------------------------------------------------------------
21. ПРИМЕР - Показать таблицу с использованием выражения LIKE;
mydb=# SELECT * FROM info WHERE name LIKE 'A%';      (покажет все поля таблицы где в столбце name слово начинается на A)

 id | name  |   last_name    |  country   |        email        | age | programming_language | experiance 
----+-------+----------------+------------+---------------------+-----+----------------------+------------
  2 | Alice | Snow           | Island     | asnow@hotmail.com   |  23 | Javascript           |          2
  5 | Andy  | Sacks          | USA        | sandrea@yahoo.com   |  22 | Python               |          3
  9 | Alima | Dzhanybayeva   | Kyrgyzstan | dalima@hotmail.com  |  23 | Python               |          1
 11 | Atai  | Ataibekov      | Kyrgyzstan | atai_atai@gmail.com |  25 | Javascript           |          3
 15 | Alex  | Smartungschaft | Germany    | alexsmart@gmail.com |  29 | Javascript           |          9
(5 rows)


22. ПРИМЕР - использованием выражения LIKE;
mydb=# SELECT * FROM info WHERE email LIKE '%@gmail.com';(покажет все поля таблицы где в столбце email слово заканчивается на gmail.com)

id |  name  |   last_name    |    country    |          email          | age | programming_language | experiance 
----+--------+----------------+---------------+-------------------------+-----+----------------------+------------
  1 | John   | Snow           | Island        | jsnow@gmail.com         |  43 | Python               |          3
  6 | Emely  | Chart          | Great Britain | cemely@gmail.com        |  23 | Python               |          5
  8 | Talant | Talantbekov    | Kyrgyzstan    | talasuper@gmail.com     |  34 | Javascript           |          1
 11 | Atai   | Ataibekov      | Kyrgyzstan    | atai_atai@gmail.com     |  25 | Javascript           |          3
 14 | Kianu  | Reeves         | Japan         | kianu@gmail.com         |  50 | Javascript           |          7
 15 | Alex   | Smartungschaft | Germany       | alexsmart@gmail.com     |  29 | Javascript           |          9
 16 | Maria  | Sharapova      | Russia        | sugarpova@gmail.com     |  34 | Python               |          2
 17 | Loky   | Asgardson      | Norway        | lokyloky@gmail.com      | 300 | Python               |          5
 18 | Jean   | Gray           | USA           | white_pheonix@gmail.com |  17 | Javascript           |          3
 19 | Ryan   | Deadpool       | Canada        | dead_pool@gmail.com     |  38 | Python               |          2
(10 rows)


23. ПРИМЕР - использованием выражения LIKE;
mydb=# SELECT * FROM info WHERE name LIKE '%ala%';

 id |  name  |  last_name  |  country   |        email        | age | programming_language | experiance 
----+--------+-------------+------------+---------------------+-----+----------------------+------------
  8 | Talant | Talantbekov | Kyrgyzstan | talasuper@gmail.com |  34 | Javascript           |          1
(1 row)


24. ПРИМЕР - использованием выражения LIKE;
mydb=# SELECT * FROM info WHERE country LIKE 'US_';

 id | name  | last_name | country |          email          | age | programming_language | experiance 
----+-------+-----------+---------+-------------------------+-----+----------------------+------------
  3 | Sandy | Smith     | USA     | ssandy@yahoo.com        |  18 | Javascript           |          4
  5 | Andy  | Sacks     | USA     | sandrea@yahoo.com       |  22 | Python               |          3
 18 | Jean  | Gray      | USA     | white_pheonix@gmail.com |  17 | Javascript           |          3
 24 | Kate  |           | USA     | katty@hotmail.com       |     | Javascript           |          2
(4 rows)


25. ПРИМЕР - использованием выражения LIKE:
mydb=# SELECT * FROM info WHERE last_name LIKE '___y' OR name LIKE '%y';

 id | name  | last_name |    country    |          email          | age | programming_language | experiance 
----+-------+-----------+---------------+-------------------------+-----+----------------------+------------
  3 | Sandy | Smith     | USA           | ssandy@yahoo.com        |  18 | Javascript           |          4
  5 | Andy  | Sacks     | USA           | sandrea@yahoo.com       |  22 | Python               |          3
  6 | Emely | Chart     | Great Britain | cemely@gmail.com        |  23 | Python               |          5
 17 | Loky  | Asgardson | Norway        | lokyloky@gmail.com      | 300 | Python               |          5
 18 | Jean  | Gray      | USA           | white_pheonix@gmail.com |  17 | Javascript           |          3
(5 rows)


26. ПРИМЕР - использованием выражения LIKE:
mydb=# SELECT * FROM info WHERE last_name ILIKE 's%' AND age BETWEEN 20 and 35;

 id | name  |   last_name    | country |        email        | age | programming_language | experiance 
----+-------+----------------+---------+---------------------+-----+----------------------+------------
  2 | Alice | Snow           | Island  | asnow@hotmail.com   |  23 | Javascript           |          2
  5 | Andy  | Sacks          | USA     | sandrea@yahoo.com   |  22 | Python               |          3
 15 | Alex  | Smartungschaft | Germany | alexsmart@gmail.com |  29 | Javascript           |          9
 16 | Maria | Sharapova      | Russia  | sugarpova@gmail.com |  34 | Python               |          2
(4 rows)

-----------------------------------------------------------------------------------------------------------------------------------------------------------

27. ПРИМЕР - использованием выражения IS:
mydb=# SELECT * FROM info WHERE age IS NULL;

 id | name | last_name | country |       email       | age | programming_language | experiance 
----+------+-----------+---------+-------------------+-----+----------------------+------------
 24 | Kate |           | USA     | katty@hotmail.com |     | Javascript           |          2
(1 row)

mydb=# SELECT * FROM info WHERE NOT last_name IS NULL;
............


-----------------------------------------------------------------------------------------------------------------------------------------------------------
28. ПРИМЕР - использованием выражения LIMIT:
mydb=# SELECT * FROM info LIMIT 10;     (показать 10 первых строк)

 id |  name  |  last_name   |    country    |        email        | age | programming_language | experiance 
----+--------+--------------+---------------+---------------------+-----+----------------------+------------
  1 | John   | Snow         | Island        | jsnow@gmail.com     |  43 | Python               |          3
  2 | Alice  | Snow         | Island        | asnow@hotmail.com   |  23 | Javascript           |          2
  3 | Sandy  | Smith        | USA           | ssandy@yahoo.com    |  18 | Javascript           |          4
  5 | Andy   | Sacks        | USA           | sandrea@yahoo.com   |  22 | Python               |          3
  6 | Emely  | Chart        | Great Britain | cemely@gmail.com    |  23 | Python               |          5
  7 | Emil   | Avazov       | Kyrgyzstan    | eayvazov@yahoo.com  |  28 | Python               |          1
  8 | Talant | Talantbekov  | Kyrgyzstan    | talasuper@gmail.com |  34 | Javascript           |          1
  9 | Alima  | Dzhanybayeva | Kyrgyzstan    | dalima@hotmail.com  |  23 | Python               |          1
 10 | Jannet | Jannetova    | Kyrgyzstan    | jjannet@yahoo.com   |  34 | Python               |          1
 11 | Atai   | Ataibekov    | Kyrgyzstan    | atai_atai@gmail.com |  25 | Javascript           |          3
(10 rows)

28. ПРИМЕР - использованием выражения LIMIT:
mydb=# SELECT * FROM info ORDER BY id LIMIT 10;

 id |  name  |  last_name   |    country    |        email        | age | programming_language | experiance 
----+--------+--------------+---------------+---------------------+-----+----------------------+------------
  1 | John   | Snow         | Island        | jsnow@gmail.com     |  43 | Python               |          3
  2 | Alice  | Snow         | Island        | asnow@hotmail.com   |  23 | Javascript           |          2
  3 | Sandy  | Smith        | USA           | ssandy@yahoo.com    |  18 | Javascript           |          4
  5 | Andy   | Sacks        | USA           | sandrea@yahoo.com   |  22 | Python               |          3
  6 | Emely  | Chart        | Great Britain | cemely@gmail.com    |  23 | Python               |          5
  7 | Emil   | Avazov       | Kyrgyzstan    | eayvazov@yahoo.com  |  28 | Python               |          1
  8 | Talant | Talantbekov  | Kyrgyzstan    | talasuper@gmail.com |  34 | Javascript           |          1
  9 | Alima  | Dzhanybayeva | Kyrgyzstan    | dalima@hotmail.com  |  23 | Python               |          1
 10 | Jannet | Jannetova    | Kyrgyzstan    | jjannet@yahoo.com   |  34 | Python               |          1
 11 | Atai   | Ataibekov    | Kyrgyzstan    | atai_atai@gmail.com |  25 | Javascript           |          3
(10 rows)

29. ПРИМЕР - использованием выражения LIMIT:
mydb=# SELECT * FROM info ORDER BY experiance DESC LIMIT 10;

 id |  name   |   last_name    |    country    |        email        | age | programming_language | experiance 
----+---------+----------------+---------------+---------------------+-----+----------------------+------------
 15 | Alex    | Smartungschaft | Germany       | alexsmart@gmail.com |  29 | Javascript           |          9
 14 | Kianu   | Reeves         | Japan         | kianu@gmail.com     |  50 | Javascript           |          7
 13 | Biatrix | Kiddo          | Australia     | bikiddo@hotmail.com |  30 | Python               |          6
 20 | Zain    | Malik          | India         | zain@hotmail.com    |  26 | Javascript           |          6
  6 | Emely   | Chart          | Great Britain | cemely@gmail.com    |  23 | Python               |          5
 17 | Loky    | Asgardson      | Norway        | lokyloky@gmail.com  | 300 | Python               |          5
 21 | Shan    | Chi            | China         | 10rings@yahoo.com   |  25 | Python               |          5
  3 | Sandy   | Smith          | USA           | ssandy@yahoo.com    |  18 | Javascript           |          4
 12 | Kani    | Mentor         | Kyrgyzstan    | kani@yahoo.com      |  26 | Javascript           |          4
 11 | Atai    | Ataibekov      | Kyrgyzstan    | atai_atai@gmail.com |  25 | Javascript           |          3
(10 rows)


30. ПРИМЕР - использованием выражения LIMIT:
mydb=# SELECT * FROM info ORDER BY experiance DESC LIMIT 10 OFFSET 4;       (с помощью OFFSET пропустили первые четыре строки и начали с пятого)

 id |  name  | last_name |    country    |          email          | age | programming_language | experiance 
----+--------+-----------+---------------+-------------------------+-----+----------------------+------------
  6 | Emely  | Chart     | Great Britain | cemely@gmail.com        |  23 | Python               |          5
 21 | Shan   | Chi       | China         | 10rings@yahoo.com       |  25 | Python               |          5
 17 | Loky   | Asgardson | Norway        | lokyloky@gmail.com      | 300 | Python               |          5
  3 | Sandy  | Smith     | USA           | ssandy@yahoo.com        |  18 | Javascript           |          4
 12 | Kani   | Mentor    | Kyrgyzstan    | kani@yahoo.com          |  26 | Javascript           |          4
  1 | John   | Snow      | Island        | jsnow@gmail.com         |  43 | Python               |          3
  5 | Andy   | Sacks     | USA           | sandrea@yahoo.com       |  22 | Python               |          3
 11 | Atai   | Ataibekov | Kyrgyzstan    | atai_atai@gmail.com     |  25 | Javascript           |          3
 18 | Jean   | Gray      | USA           | white_pheonix@gmail.com |  17 | Javascript           |          3
 23 | Nimuea | Murriel   | Great Britain | nimuea@yahoo.com        | 200 | Javascript           |          3
(10 rows)


31. ПРИМЕР - использованием выражения FETCH:
mydb=# SELECT * FROM info ORDER BY experiance DESC FETCH FIRST (10) ROW ONLY;     (показать 10 первых строк отсортированных по убыванию по столбцу experiance)  

 id |  name   |   last_name    |    country    |        email        | age | programming_language | experiance 
----+---------+----------------+---------------+---------------------+-----+----------------------+------------
 15 | Alex    | Smartungschaft | Germany       | alexsmart@gmail.com |  29 | Javascript           |          9
 14 | Kianu   | Reeves         | Japan         | kianu@gmail.com     |  50 | Javascript           |          7
 13 | Biatrix | Kiddo          | Australia     | bikiddo@hotmail.com |  30 | Python               |          6
 20 | Zain    | Malik          | India         | zain@hotmail.com    |  26 | Javascript           |          6
  6 | Emely   | Chart          | Great Britain | cemely@gmail.com    |  23 | Python               |          5
 17 | Loky    | Asgardson      | Norway        | lokyloky@gmail.com  | 300 | Python               |          5
 21 | Shan    | Chi            | China         | 10rings@yahoo.com   |  25 | Python               |          5
  3 | Sandy   | Smith          | USA           | ssandy@yahoo.com    |  18 | Javascript           |          4
 12 | Kani    | Mentor         | Kyrgyzstan    | kani@yahoo.com      |  26 | Javascript           |          4
 11 | Atai    | Ataibekov      | Kyrgyzstan    | atai_atai@gmail.com |  25 | Javascript           |          3
(10 rows)


32. ПРИМЕР - использованием выражения FETCH:
mydb=# SELECT * FROM info ORDER BY experiance DESC OFFSET 5 FETCH FIRST (10) ROW ONLY;
(отсортируй по убыванию по столбцу experiance, пропустив первые 5, и покажи только 10 строк)

 id |  name  | last_name |    country    |          email          | age | programming_language | experiance 
----+--------+-----------+---------------+-------------------------+-----+----------------------+------------
 21 | Shan   | Chi       | China         | 10rings@yahoo.com       |  25 | Python               |          5
 17 | Loky   | Asgardson | Norway        | lokyloky@gmail.com      | 300 | Python               |          5
  3 | Sandy  | Smith     | USA           | ssandy@yahoo.com        |  18 | Javascript           |          4
 12 | Kani   | Mentor    | Kyrgyzstan    | kani@yahoo.com          |  26 | Javascript           |          4
  1 | John   | Snow      | Island        | jsnow@gmail.com         |  43 | Python               |          3
  5 | Andy   | Sacks     | USA           | sandrea@yahoo.com       |  22 | Python               |          3
 11 | Atai   | Ataibekov | Kyrgyzstan    | atai_atai@gmail.com     |  25 | Javascript           |          3
 18 | Jean   | Gray      | USA           | white_pheonix@gmail.com |  17 | Javascript           |          3
 23 | Nimuea | Murriel   | Great Britain | nimuea@yahoo.com        | 200 | Javascript           |          3
  2 | Alice  | Snow      | Island        | asnow@hotmail.com       |  23 | Javascript           |          2
(10 rows)
==============================================================================================================================================================


33. Функция SUM() примеры:
mydb=# SELECT SUM(age) AS age_sum FROM info WHERE country = 'USA';
(просуммируй значения столбца age и покажи как age_sum из таблицы info, только по строкам где country равна USA)

 age_sum 
---------
      57
(1 row)
--------------------------------------------------------------------

mydb=# SELECT SUM(experiance) AS EXP_SUM FROM info WHERE country = 'Kyrgyzstan';
 exp_sum 
---------
      11
(1 row)
--------------------------------------------------------------------

mydb=# SELECT COUNT(id) FROM info WHERE email LIKE '%hotmail.com';
 count 
-------
     5
(1 row)
--------------------------------------------------------------------

mydb=# SELECT country, SUM(experiance) FROM info GROUP BY country;
    country    | sum 
---------------+-----
 USA           |  12
 Germany       |   9
 Canada        |   2
 India         |   6
 Kyrgyzstan    |  11
 Japan         |   7
 China         |   6
 Russia        |   2
 Norway        |   5
 Australia     |   6
 Island        |   5
 Great Britain |   8
(12 rows)
---------------------------------------------------------------------------------------------------------------------------------------------------------------


34. Функция COUNT() примеры:

mydb=# SELECT COUNT(id) FROM info;
 count 
-------
    23
(1 row)
--------------------------------------------------------------------

mydb=# SELECT country, COUNT(id) FROM info GROUP BY country;
    country    | count 
---------------+-------
 USA           |     4
 Germany       |     1
 Canada        |     1
 India         |     1
 Kyrgyzstan    |     6
 Japan         |     1
 China         |     2
 Russia        |     1
 Norway        |     1
 Australia     |     1
 Island        |     2
 Great Britain |     2
(12 rows)
--------------------------------------------------------------------

mydb=# SELECT programming_language, COUNT(id) FROM info GROUP BY programming_language;
 programming_language | count 
----------------------+-------
 Python               |    12
 Javascript           |    11
(2 rows)
---------------------------------------------------------------------------------------------------------------------------------------------------------------


35. Функция AVG() примеры:
mydb=# SELECT AVG(experiance) FROM info;
        avg         
--------------------
 3.4347826086956522
(1 row)
--------------------------------------------------------------------

mydb=# SELECT AVG(experiance) FROM info WHERE country = 'USA';
        avg         
--------------------
 3.0000000000000000
(1 row)
--------------------------------------------------------------------

mydb=# SELECT country, ROUND(AVG(experiance), 2) FROM info GROUP BY country;
    country    | round 
---------------+-------
 USA           |  3.00
 Germany       |  9.00
 Canada        |  2.00
 India         |  6.00
 Kyrgyzstan    |  1.83
 Japan         |  7.00
 China         |  3.00
 Russia        |  2.00
 Norway        |  5.00
 Australia     |  6.00
 Island        |  2.50
 Great Britain |  4.00
(12 rows)
---------------------------------------------------------------------------------------------------------------------------------------------------------------

36. Функция MAX() примеры:
mydb=# SELECT MAX(age), name FROM info GROUP BY name;

 max |  name   
-----+---------
  25 | Shan
  50 | Kianu
  28 | Emil
  23 | Alice
  26 | Kani
  18 | Sandy
 200 | Nimuea
  34 | Talant
  30 | Biatrix
  38 | Ryan
  43 | John
     | Kate
  25 | Atai
  23 | Emely
  34 | Jannet
  26 | Zain
 300 | Loky
  16 | Xia
  23 | Alima
  22 | Andy
  29 | Alex
  17 | Jean
  34 | Maria
(23 rows)
---------------------------------------------------------------------------------------------------------------------------------------------------------------

37. ФУНКЦИЯ LENGHT(),  пример:

mydb=# SELECT name, LENGTH(name) AS len_name FROM makers ORDER by len_name;     (показать таблицу имя и длину имени, отсортировав по длине имени)
   name    | len_name 
-----------+----------
 Max       |        3
 Sam       |        3
 Andy      |        4
 Jade      |        4
 Suzy      |        4
 John      |        4
 Bill      |        4
 Alice     |        5
 Karen     |        5
 Anvar     |        5
 Peter     |        5
 Bailee    |        6
 Martin    |        6
 Suisane   |        7
 Antonio   |        7
 Catherine |        9
(16 rows)
---------------------------------------------------------------------------------------------------------------------------------------------------------------

37. Использование выражения HAVING примеры:

mydb=# SELECT programming_language, ROUND(AVG(age),2) FROM info GROUP BY programming_language HAVING AVG(experiance) > 2;

 programming_language | round 
----------------------+-------
 Python               | 51.33
 Javascript           | 44.80
(2 rows)
----------------------------------------------------------------------------

mydb=# SELECT programming_language, ROUND(AVG(age),2) FROM info GROUP BY programming_language HAVING AVG(experiance) > 3;

 programming_language | round 
----------------------+-------
 Javascript           | 44.80
(1 row)
----------------------------------------------------------------------------

mydb=# SELECT country, ROUND(AVG(experiance), 2) FROM info GROUP BY country HAVING AVG(experiance) >= 2;

    country    | round 
---------------+-------
 USA           |  3.00
 Germany       |  9.00
 Canada        |  2.00
 India         |  6.00
 Japan         |  7.00
 China         |  3.00
 Russia        |  2.00
 Norway        |  5.00
 Australia     |  6.00
 Island        |  2.50
 Great Britain |  4.00
(11 rows)
----------------------------------------------------------------------------

mydb=# SELECT country, ROUND(AVG(experiance), 2) FROM info GROUP BY country HAVING AVG(experiance) >= 3;
    country    | round 
---------------+-------
 USA           |  3.00
 Germany       |  9.00
 India         |  6.00
 Japan         |  7.00
 China         |  3.00
 Norway        |  5.00
 Australia     |  6.00
 Great Britain |  4.00
(8 rows)

===============================================================================================================================================================

38. ОБНОВЛЕНИЕ ТАБЛИЦЫ (UPDATE) !!!  
    ПРИМЕРЫ:

mydb=# UPDATE info SET last_name='Summers', country='Canada' WHERE id=24;

UPDATE 1
mydb=# SELECT * FROM info;
 id |  name   |   last_name    |    country    |          email          | age | programming_language | experiance 
----+---------+----------------+---------------+-------------------------+-----+----------------------+------------
  1 | John    | Snow           | Island        | jsnow@gmail.com         |  43 | Python               |          3
  2 | Alice   | Snow           | Island        | asnow@hotmail.com       |  23 | Javascript           |          2
  3 | Sandy   | Smith          | USA           | ssandy@yahoo.com        |  18 | Javascript           |          4
  5 | Andy    | Sacks          | USA           | sandrea@yahoo.com       |  22 | Python               |          3
  6 | Emely   | Chart          | Great Britain | cemely@gmail.com        |  23 | Python               |          5
  7 | Emil    | Avazov         | Kyrgyzstan    | eayvazov@yahoo.com      |  28 | Python               |          1
  8 | Talant  | Talantbekov    | Kyrgyzstan    | talasuper@gmail.com     |  34 | Javascript           |          1
  9 | Alima   | Dzhanybayeva   | Kyrgyzstan    | dalima@hotmail.com      |  23 | Python               |          1
 10 | Jannet  | Jannetova      | Kyrgyzstan    | jjannet@yahoo.com       |  34 | Python               |          1
 11 | Atai    | Ataibekov      | Kyrgyzstan    | atai_atai@gmail.com     |  25 | Javascript           |          3
 12 | Kani    | Mentor         | Kyrgyzstan    | kani@yahoo.com          |  26 | Javascript           |          4
 13 | Biatrix | Kiddo          | Australia     | bikiddo@hotmail.com     |  30 | Python               |          6
 14 | Kianu   | Reeves         | Japan         | kianu@gmail.com         |  50 | Javascript           |          7
 15 | Alex    | Smartungschaft | Germany       | alexsmart@gmail.com     |  29 | Javascript           |          9
 16 | Maria   | Sharapova      | Russia        | sugarpova@gmail.com     |  34 | Python               |          2
 17 | Loky    | Asgardson      | Norway        | lokyloky@gmail.com      | 300 | Python               |          5
 18 | Jean    | Gray           | USA           | white_pheonix@gmail.com |  17 | Javascript           |          3
 19 | Ryan    | Deadpool       | Canada        | dead_pool@gmail.com     |  38 | Python               |          2
 20 | Zain    | Malik          | India         | zain@hotmail.com        |  26 | Javascript           |          6
 21 | Shan    | Chi            | China         | 10rings@yahoo.com       |  25 | Python               |          5
 22 | Xia     | Nihua          | China         | nihua@yahoo.com         |  16 | Python               |          1
 23 | Nimuea  | Murriel        | Great Britain | nimuea@yahoo.com        | 200 | Javascript           |          3
 24 | Kate    | Summers        | Canada        | katty@hotmail.com       |     | Javascript           |          2
(23 rows)
---------------------------------------------------------------------------------

mydb=# UPDATE info SET age=25 WHERE id=24;

UPDATE 1
mydb=# SELECT * FROM info;
 id |  name   |   last_name    |    country    |          email          | age | programming_language | experiance 
----+---------+----------------+---------------+-------------------------+-----+----------------------+------------
  1 | John    | Snow           | Island        | jsnow@gmail.com         |  43 | Python               |          3
  2 | Alice   | Snow           | Island        | asnow@hotmail.com       |  23 | Javascript           |          2
  3 | Sandy   | Smith          | USA           | ssandy@yahoo.com        |  18 | Javascript           |          4
  5 | Andy    | Sacks          | USA           | sandrea@yahoo.com       |  22 | Python               |          3
  6 | Emely   | Chart          | Great Britain | cemely@gmail.com        |  23 | Python               |          5
  7 | Emil    | Avazov         | Kyrgyzstan    | eayvazov@yahoo.com      |  28 | Python               |          1
  8 | Talant  | Talantbekov    | Kyrgyzstan    | talasuper@gmail.com     |  34 | Javascript           |          1
  9 | Alima   | Dzhanybayeva   | Kyrgyzstan    | dalima@hotmail.com      |  23 | Python               |          1
 10 | Jannet  | Jannetova      | Kyrgyzstan    | jjannet@yahoo.com       |  34 | Python               |          1
 11 | Atai    | Ataibekov      | Kyrgyzstan    | atai_atai@gmail.com     |  25 | Javascript           |          3
 12 | Kani    | Mentor         | Kyrgyzstan    | kani@yahoo.com          |  26 | Javascript           |          4
 13 | Biatrix | Kiddo          | Australia     | bikiddo@hotmail.com     |  30 | Python               |          6
 14 | Kianu   | Reeves         | Japan         | kianu@gmail.com         |  50 | Javascript           |          7
 15 | Alex    | Smartungschaft | Germany       | alexsmart@gmail.com     |  29 | Javascript           |          9
 16 | Maria   | Sharapova      | Russia        | sugarpova@gmail.com     |  34 | Python               |          2
 17 | Loky    | Asgardson      | Norway        | lokyloky@gmail.com      | 300 | Python               |          5
 18 | Jean    | Gray           | USA           | white_pheonix@gmail.com |  17 | Javascript           |          3
 19 | Ryan    | Deadpool       | Canada        | dead_pool@gmail.com     |  38 | Python               |          2
 20 | Zain    | Malik          | India         | zain@hotmail.com        |  26 | Javascript           |          6
 21 | Shan    | Chi            | China         | 10rings@yahoo.com       |  25 | Python               |          5
 22 | Xia     | Nihua          | China         | nihua@yahoo.com         |  16 | Python               |          1
 23 | Nimuea  | Murriel        | Great Britain | nimuea@yahoo.com        | 200 | Javascript           |          3
 24 | Kate    | Summers        | Canada        | katty@hotmail.com       |  25 | Javascript           |          2
(23 rows)
---------------------------------------------------------------------------------

mydb=# UPDATE info SET email='lokkky@hotmail.com', experiance=11 WHERE id=17;

UPDATE 1
mydb=# SELECT * FROM info;
 id |  name   |   last_name    |    country    |          email          | age | programming_language | experiance 
----+---------+----------------+---------------+-------------------------+-----+----------------------+------------
  1 | John    | Snow           | Island        | jsnow@gmail.com         |  43 | Python               |          3
  2 | Alice   | Snow           | Island        | asnow@hotmail.com       |  23 | Javascript           |          2
  3 | Sandy   | Smith          | USA           | ssandy@yahoo.com        |  18 | Javascript           |          4
  5 | Andy    | Sacks          | USA           | sandrea@yahoo.com       |  22 | Python               |          3
  6 | Emely   | Chart          | Great Britain | cemely@gmail.com        |  23 | Python               |          5
  7 | Emil    | Avazov         | Kyrgyzstan    | eayvazov@yahoo.com      |  28 | Python               |          1
  8 | Talant  | Talantbekov    | Kyrgyzstan    | talasuper@gmail.com     |  34 | Javascript           |          1
  9 | Alima   | Dzhanybayeva   | Kyrgyzstan    | dalima@hotmail.com      |  23 | Python               |          1
 10 | Jannet  | Jannetova      | Kyrgyzstan    | jjannet@yahoo.com       |  34 | Python               |          1
 11 | Atai    | Ataibekov      | Kyrgyzstan    | atai_atai@gmail.com     |  25 | Javascript           |          3
 12 | Kani    | Mentor         | Kyrgyzstan    | kani@yahoo.com          |  26 | Javascript           |          4
 13 | Biatrix | Kiddo          | Australia     | bikiddo@hotmail.com     |  30 | Python               |          6
 14 | Kianu   | Reeves         | Japan         | kianu@gmail.com         |  50 | Javascript           |          7
 15 | Alex    | Smartungschaft | Germany       | alexsmart@gmail.com     |  29 | Javascript           |          9
 16 | Maria   | Sharapova      | Russia        | sugarpova@gmail.com     |  34 | Python               |          2
 18 | Jean    | Gray           | USA           | white_pheonix@gmail.com |  17 | Javascript           |          3
 19 | Ryan    | Deadpool       | Canada        | dead_pool@gmail.com     |  38 | Python               |          2
 20 | Zain    | Malik          | India         | zain@hotmail.com        |  26 | Javascript           |          6
 21 | Shan    | Chi            | China         | 10rings@yahoo.com       |  25 | Python               |          5
 22 | Xia     | Nihua          | China         | nihua@yahoo.com         |  16 | Python               |          1
 23 | Nimuea  | Murriel        | Great Britain | nimuea@yahoo.com        | 200 | Javascript           |          3
 24 | Kate    | Summers        | Canada        | katty@hotmail.com       |  25 | Javascript           |          2
 17 | Loky    | Asgardson      | Norway        | lokkky@hotmail.com      | 300 | Python               |         11
(23 rows)
---------------------------------------------------------------------------------

mydb=# UPDATE info SET experiance=3 WHERE country='Kyrgyzstan';

UPDATE 6
mydb=# SELECT * FROM info;
 id |  name   |   last_name    |    country    |          email          | age | programming_language | experiance 
----+---------+----------------+---------------+-------------------------+-----+----------------------+------------
  1 | John    | Snow           | Island        | jsnow@gmail.com         |  43 | Python               |          3
  2 | Alice   | Snow           | Island        | asnow@hotmail.com       |  23 | Javascript           |          2
  3 | Sandy   | Smith          | USA           | ssandy@yahoo.com        |  18 | Javascript           |          4
  5 | Andy    | Sacks          | USA           | sandrea@yahoo.com       |  22 | Python               |          3
  6 | Emely   | Chart          | Great Britain | cemely@gmail.com        |  23 | Python               |          5
 13 | Biatrix | Kiddo          | Australia     | bikiddo@hotmail.com     |  30 | Python               |          6
 14 | Kianu   | Reeves         | Japan         | kianu@gmail.com         |  50 | Javascript           |          7
 15 | Alex    | Smartungschaft | Germany       | alexsmart@gmail.com     |  29 | Javascript           |          9
 16 | Maria   | Sharapova      | Russia        | sugarpova@gmail.com     |  34 | Python               |          2
 18 | Jean    | Gray           | USA           | white_pheonix@gmail.com |  17 | Javascript           |          3
 19 | Ryan    | Deadpool       | Canada        | dead_pool@gmail.com     |  38 | Python               |          2
 20 | Zain    | Malik          | India         | zain@hotmail.com        |  26 | Javascript           |          6
 21 | Shan    | Chi            | China         | 10rings@yahoo.com       |  25 | Python               |          5
 22 | Xia     | Nihua          | China         | nihua@yahoo.com         |  16 | Python               |          1
 23 | Nimuea  | Murriel        | Great Britain | nimuea@yahoo.com        | 200 | Javascript           |          3
 24 | Kate    | Summers        | Canada        | katty@hotmail.com       |  25 | Javascript           |          2
 17 | Loky    | Asgardson      | Norway        | lokkky@hotmail.com      | 300 | Python               |         11
  7 | Emil    | Avazov         | Kyrgyzstan    | eayvazov@yahoo.com      |  28 | Python               |          3
  8 | Talant  | Talantbekov    | Kyrgyzstan    | talasuper@gmail.com     |  34 | Javascript           |          3
  9 | Alima   | Dzhanybayeva   | Kyrgyzstan    | dalima@hotmail.com      |  23 | Python               |          3
 10 | Jannet  | Jannetova      | Kyrgyzstan    | jjannet@yahoo.com       |  34 | Python               |          3
 11 | Atai    | Ataibekov      | Kyrgyzstan    | atai_atai@gmail.com     |  25 | Javascript           |          3
 12 | Kani    | Mentor         | Kyrgyzstan    | kani@yahoo.com          |  26 | Javascript           |          3
(23 rows)

=============================================================================================================================================================

39. УДАЛЕНИЕ (DELETE) СТРОК !!!
    ПРИМЕРЫ:

mydb=# DELETE FROM info WHERE id=3;

DELETE 1
mydb=# SELECT * FROM info;
 id |  name   |   last_name    |    country    |          email          | age | programming_language | experiance 
----+---------+----------------+---------------+-------------------------+-----+----------------------+------------
  1 | John    | Snow           | Island        | jsnow@gmail.com         |  43 | Python               |          3
  2 | Alice   | Snow           | Island        | asnow@hotmail.com       |  23 | Javascript           |          2
  5 | Andy    | Sacks          | USA           | sandrea@yahoo.com       |  22 | Python               |          3
  6 | Emely   | Chart          | Great Britain | cemely@gmail.com        |  23 | Python               |          5
 13 | Biatrix | Kiddo          | Australia     | bikiddo@hotmail.com     |  30 | Python               |          6
 14 | Kianu   | Reeves         | Japan         | kianu@gmail.com         |  50 | Javascript           |          7
 15 | Alex    | Smartungschaft | Germany       | alexsmart@gmail.com     |  29 | Javascript           |          9
 16 | Maria   | Sharapova      | Russia        | sugarpova@gmail.com     |  34 | Python               |          2
 18 | Jean    | Gray           | USA           | white_pheonix@gmail.com |  17 | Javascript           |          3
 19 | Ryan    | Deadpool       | Canada        | dead_pool@gmail.com     |  38 | Python               |          2
 20 | Zain    | Malik          | India         | zain@hotmail.com        |  26 | Javascript           |          6
 21 | Shan    | Chi            | China         | 10rings@yahoo.com       |  25 | Python               |          5
 22 | Xia     | Nihua          | China         | nihua@yahoo.com         |  16 | Python               |          1
 23 | Nimuea  | Murriel        | Great Britain | nimuea@yahoo.com        | 200 | Javascript           |          3
 24 | Kate    | Summers        | Canada        | katty@hotmail.com       |  25 | Javascript           |          2
 17 | Loky    | Asgardson      | Norway        | lokkky@hotmail.com      | 300 | Python               |         11
  7 | Emil    | Avazov         | Kyrgyzstan    | eayvazov@yahoo.com      |  28 | Python               |          3
  8 | Talant  | Talantbekov    | Kyrgyzstan    | talasuper@gmail.com     |  34 | Javascript           |          3
  9 | Alima   | Dzhanybayeva   | Kyrgyzstan    | dalima@hotmail.com      |  23 | Python               |          3
 10 | Jannet  | Jannetova      | Kyrgyzstan    | jjannet@yahoo.com       |  34 | Python               |          3
 11 | Atai    | Ataibekov      | Kyrgyzstan    | atai_atai@gmail.com     |  25 | Javascript           |          3
 12 | Kani    | Mentor         | Kyrgyzstan    | kani@yahoo.com          |  26 | Javascript           |          3
(22 rows)
------------------------------------------------------------------------

mydb=# DELETE FROM info WHERE name='Kate';

DELETE 1
mydb=# SELECT * FROM info;
 id |  name   |   last_name    |    country    |          email          | age | programming_language | experiance 
----+---------+----------------+---------------+-------------------------+-----+----------------------+------------
  1 | John    | Snow           | Island        | jsnow@gmail.com         |  43 | Python               |          3
  2 | Alice   | Snow           | Island        | asnow@hotmail.com       |  23 | Javascript           |          2
  5 | Andy    | Sacks          | USA           | sandrea@yahoo.com       |  22 | Python               |          3
  6 | Emely   | Chart          | Great Britain | cemely@gmail.com        |  23 | Python               |          5
 13 | Biatrix | Kiddo          | Australia     | bikiddo@hotmail.com     |  30 | Python               |          6
 14 | Kianu   | Reeves         | Japan         | kianu@gmail.com         |  50 | Javascript           |          7
 15 | Alex    | Smartungschaft | Germany       | alexsmart@gmail.com     |  29 | Javascript           |          9
 16 | Maria   | Sharapova      | Russia        | sugarpova@gmail.com     |  34 | Python               |          2
 18 | Jean    | Gray           | USA           | white_pheonix@gmail.com |  17 | Javascript           |          3
 19 | Ryan    | Deadpool       | Canada        | dead_pool@gmail.com     |  38 | Python               |          2
 20 | Zain    | Malik          | India         | zain@hotmail.com        |  26 | Javascript           |          6
 21 | Shan    | Chi            | China         | 10rings@yahoo.com       |  25 | Python               |          5
 22 | Xia     | Nihua          | China         | nihua@yahoo.com         |  16 | Python               |          1
 23 | Nimuea  | Murriel        | Great Britain | nimuea@yahoo.com        | 200 | Javascript           |          3
 17 | Loky    | Asgardson      | Norway        | lokkky@hotmail.com      | 300 | Python               |         11
  7 | Emil    | Avazov         | Kyrgyzstan    | eayvazov@yahoo.com      |  28 | Python               |          3
  8 | Talant  | Talantbekov    | Kyrgyzstan    | talasuper@gmail.com     |  34 | Javascript           |          3
  9 | Alima   | Dzhanybayeva   | Kyrgyzstan    | dalima@hotmail.com      |  23 | Python               |          3
 10 | Jannet  | Jannetova      | Kyrgyzstan    | jjannet@yahoo.com       |  34 | Python               |          3
 11 | Atai    | Ataibekov      | Kyrgyzstan    | atai_atai@gmail.com     |  25 | Javascript           |          3
 12 | Kani    | Mentor         | Kyrgyzstan    | kani@yahoo.com          |  26 | Javascript           |          3
(21 rows)
------------------------------------------------------------------------

mydb=# DELETE FROM info WHERE email LIKE 'zain%';

DELETE 1
mydb=# SELECT * FROM info;
 id |  name   |   last_name    |    country    |          email          | age | programming_language | experiance 
----+---------+----------------+---------------+-------------------------+-----+----------------------+------------
  1 | John    | Snow           | Island        | jsnow@gmail.com         |  43 | Python               |          3
  2 | Alice   | Snow           | Island        | asnow@hotmail.com       |  23 | Javascript           |          2
  5 | Andy    | Sacks          | USA           | sandrea@yahoo.com       |  22 | Python               |          3
  6 | Emely   | Chart          | Great Britain | cemely@gmail.com        |  23 | Python               |          5
 13 | Biatrix | Kiddo          | Australia     | bikiddo@hotmail.com     |  30 | Python               |          6
 14 | Kianu   | Reeves         | Japan         | kianu@gmail.com         |  50 | Javascript           |          7
 15 | Alex    | Smartungschaft | Germany       | alexsmart@gmail.com     |  29 | Javascript           |          9
 16 | Maria   | Sharapova      | Russia        | sugarpova@gmail.com     |  34 | Python               |          2
 18 | Jean    | Gray           | USA           | white_pheonix@gmail.com |  17 | Javascript           |          3
 19 | Ryan    | Deadpool       | Canada        | dead_pool@gmail.com     |  38 | Python               |          2
 21 | Shan    | Chi            | China         | 10rings@yahoo.com       |  25 | Python               |          5
 22 | Xia     | Nihua          | China         | nihua@yahoo.com         |  16 | Python               |          1
 23 | Nimuea  | Murriel        | Great Britain | nimuea@yahoo.com        | 200 | Javascript           |          3
 17 | Loky    | Asgardson      | Norway        | lokkky@hotmail.com      | 300 | Python               |         11
  7 | Emil    | Avazov         | Kyrgyzstan    | eayvazov@yahoo.com      |  28 | Python               |          3
  8 | Talant  | Talantbekov    | Kyrgyzstan    | talasuper@gmail.com     |  34 | Javascript           |          3
  9 | Alima   | Dzhanybayeva   | Kyrgyzstan    | dalima@hotmail.com      |  23 | Python               |          3
 10 | Jannet  | Jannetova      | Kyrgyzstan    | jjannet@yahoo.com       |  34 | Python               |          3
 11 | Atai    | Ataibekov      | Kyrgyzstan    | atai_atai@gmail.com     |  25 | Javascript           |          3
 12 | Kani    | Mentor         | Kyrgyzstan    | kani@yahoo.com          |  26 | Javascript           |          3
(20 rows)

================================================================================================================================================================

40. ИЗМЕНЕНИЕ ТАБЛИЦЫ (СТОЛБЦОВ). ИСПОЛЬЗОВАНИЕ ALTER!!!
    ПРИМЕРЫ:

mydb=# \d info
                                           Table "public.info"
        Column        |          Type          | Collation | Nullable |             Default              
----------------------+------------------------+-----------+----------+----------------------------------
 id                   | integer                |           | not null | nextval('info_id_seq'::regclass)
 name                 | character varying(50)  |           | not null | 
 last_name            | character varying(150) |           |          | 
 country              | character varying(60)  |           |          | 
 email                | character varying(50)  |           |          | 
 age                  | integer                |           |          | 
 programming_language | language               |           | not null | 
 experiance           | integer                |           |          | 
Indexes:
    "info_pkey" PRIMARY KEY, btree (id)
    "info_email_key" UNIQUE CONSTRAINT, btree (email)


mydb=# ALTER TABLE info ALTER COLUMN name TYPE VARCHAR(80);         (внесли изменение типу данных столбца name);
ALTER TABLE
mydb=# \d info
                                           Table "public.info"
        Column        |          Type          | Collation | Nullable |             Default              
----------------------+------------------------+-----------+----------+----------------------------------
 id                   | integer                |           | not null | nextval('info_id_seq'::regclass)
 name                 | character varying(80)  |           | not null | 
 last_name            | character varying(150) |           |          | 
 country              | character varying(60)  |           |          | 
 email                | character varying(50)  |           |          | 
 age                  | integer                |           |          | 
 programming_language | language               |           | not null | 
 experiance           | integer                |           |          | 
Indexes:
    "info_pkey" PRIMARY KEY, btree (id)
    "info_email_key" UNIQUE CONSTRAINT, btree (email)
------------------------------------------------------------------------------------------------------------------------------------------------------------


mydb=# ALTER TABLE info ALTER COLUMN last_name SET NOT NULL;            (внесли ограничение к столбцу last_name)
ALTER TABLE
mydb=# \d info
                                           Table "public.info"
        Column        |          Type          | Collation | Nullable |             Default              
----------------------+------------------------+-----------+----------+----------------------------------
 id                   | integer                |           | not null | nextval('info_id_seq'::regclass)
 name                 | character varying(80)  |           | not null | 
 last_name            | character varying(150) |           | not null | 
 country              | character varying(60)  |           |          | 
 email                | character varying(50)  |           |          | 
 age                  | integer                |           |          | 
 programming_language | language               |           | not null | 
 experiance           | integer                |           |          | 
Indexes:
    "info_pkey" PRIMARY KEY, btree (id)
    "info_email_key" UNIQUE CONSTRAINT, btree (email)
------------------------------------------------------------------------------------------------------------------------------------------------------------


mydb=# ALTER TABLE info RENAME COLUMN last_name TO surname;         (поменяли название столбца last_name на surname)
ALTER TABLE
mydb=# \d info
                                           Table "public.info"
        Column        |          Type          | Collation | Nullable |             Default              
----------------------+------------------------+-----------+----------+----------------------------------
 id                   | integer                |           | not null | nextval('info_id_seq'::regclass)
 name                 | character varying(80)  |           | not null | 
 surname              | character varying(150) |           | not null | 
 country              | character varying(60)  |           |          | 
 email                | character varying(50)  |           |          | 
 age                  | integer                |           |          | 
 programming_language | language               |           | not null | 
 experiance           | integer                |           |          | 
Indexes:
    "info_pkey" PRIMARY KEY, btree (id)
    "info_email_key" UNIQUE CONSTRAINT, btree (email)
------------------------------------------------------------------------------------------------------------------------------------------------------------

mydb=# ALTER TABLE info ADD CONSTRAINT name_of_constraint UNIQUE (name);        (добавили ограничение "name_of_constraint" UNIQUE к столбцу name)
ALTER TABLE
mydb=# \d info
                                           Table "public.info"
        Column        |          Type          | Collation | Nullable |             Default              
----------------------+------------------------+-----------+----------+----------------------------------
 id                   | integer                |           | not null | nextval('info_id_seq'::regclass)
 name                 | character varying(80)  |           | not null | 
 surname              | character varying(150) |           | not null | 
 country              | character varying(60)  |           |          | 
 email                | character varying(50)  |           |          | 
 age                  | integer                |           |          | 
 programming_language | language               |           | not null | 
 experiance           | integer                |           |          | 
Indexes:
    "info_pkey" PRIMARY KEY, btree (id)
    "info_email_key" UNIQUE CONSTRAINT, btree (email)
    "name_of_constraint" UNIQUE CONSTRAINT, btree (name)

================================================================================================================================================================

41. ИЗМЕНЕНИЕ ТАБЛИЦЫ (СТОЛБЦОВ). ИСПОЛЬЗОВАНИЕ ALTER, DROP!!!
    ПРИМЕРЫ:

mydb=# ALTER TABLE info DROP age, DROP email;           (удаление столбцов age, email)
ALTER TABLE
mydb=# \d info
                                           Table "public.info"
        Column        |          Type          | Collation | Nullable |             Default              
----------------------+------------------------+-----------+----------+----------------------------------
 id                   | integer                |           | not null | nextval('info_id_seq'::regclass)
 name                 | character varying(80)  |           | not null | 
 surname              | character varying(150) |           | not null | 
 country              | character varying(60)  |           |          | 
 programming_language | language               |           | not null | 
 experiance           | integer                |           |          | 
Indexes:
    "info_pkey" PRIMARY KEY, btree (id)
    "name_of_constraint" UNIQUE CONSTRAINT, btree (name)

mydb=# SELECT * FROM info;
 id |  name   |    surname     |    country    | programming_language | experiance 
----+---------+----------------+---------------+----------------------+------------
  1 | John    | Snow           | Island        | Python               |          3
  2 | Alice   | Snow           | Island        | Javascript           |          2
  5 | Andy    | Sacks          | USA           | Python               |          3
  6 | Emely   | Chart          | Great Britain | Python               |          5
 13 | Biatrix | Kiddo          | Australia     | Python               |          6
 14 | Kianu   | Reeves         | Japan         | Javascript           |          7
 15 | Alex    | Smartungschaft | Germany       | Javascript           |          9
 16 | Maria   | Sharapova      | Russia        | Python               |          2
 18 | Jean    | Gray           | USA           | Javascript           |          3
 19 | Ryan    | Deadpool       | Canada        | Python               |          2
 21 | Shan    | Chi            | China         | Python               |          5
 22 | Xia     | Nihua          | China         | Python               |          1
 23 | Nimuea  | Murriel        | Great Britain | Javascript           |          3
 17 | Loky    | Asgardson      | Norway        | Python               |         11
  7 | Emil    | Avazov         | Kyrgyzstan    | Python               |          3
  8 | Talant  | Talantbekov    | Kyrgyzstan    | Javascript           |          3
  9 | Alima   | Dzhanybayeva   | Kyrgyzstan    | Python               |          3
 10 | Jannet  | Jannetova      | Kyrgyzstan    | Python               |          3
 11 | Atai    | Ataibekov      | Kyrgyzstan    | Javascript           |          3
 12 | Kani    | Mentor         | Kyrgyzstan    | Javascript           |          3
(20 rows)
---------------------------------------------------------------------------------------------------------------------------------------------


"""