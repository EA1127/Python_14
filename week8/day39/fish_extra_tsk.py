"""

You are given two non-empty arrays A and B consisting of N integers. 
Arrays A and B represent N voracious fish in a river, 
ordered downstream along the flow of the river.

The fish are numbered from 0 to N − 1. If P and Q are two fish and P < Q, 
then fish P is initially upstream of fish Q. Initially, each fish has a unique position.

Fish number P is represented by A[P] and B[P]. Array A contains the sizes of the fish. 
All its elements are unique. Array B contains the directions of the fish. 
It contains only 0s and/or 1s, where:

0 represents a fish flowing upstream,
1 represents a fish flowing downstream.

If two fish move in opposite directions and there are no other (living) fish between them, 
they will eventually meet each other. Then only one fish can stay alive − the larger fish 
eats the smaller one. More precisely, we say that two fish P and Q meet each other when P < Q,
 B[P] = 1 and B[Q] = 0, and there are no living fish between them. After they meet:

If A[P] > A[Q] then P eats Q, and P will still be flowing downstream,
If A[Q] > A[P] then Q eats P, and Q will still be flowing upstream.
We assume that all the fish are flowing at the same speed. That is, fish moving in the same 
direction never meet. The goal is to calculate the number of fish that will stay alive.

For example, consider arrays A and B such that:

  A[0] = 4    B[0] = 0
  A[1] = 3    B[1] = 1
  A[2] = 2    B[2] = 0
  A[3] = 1    B[3] = 0
  A[4] = 5    B[4] = 0
Initially all the fish are alive and all except fish number 1 are moving upstream. 
Fish number 1 meets fish number 2 and eats it, then it meets fish number 3 and eats it too. 
Finally, it meets fish number 4 and is eaten by it. The remaining two fish, number 0 and 4, 
never meet and therefore stay alive.

Write a function:

def solution(A, B)

that, given two non-empty arrays A and B consisting of N integers, returns the number of 
fish that will stay alive.

For example, given the arrays shown above, the function should return 2, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [0..1,000,000,000];
each element of array B is an integer that can have one of the following values: 0, 1;
the elements of A are all distinct.

=============================================================================================================
"""

"""
Условие задчи:

Вам даны два непустых массива A и B, состоящих из N целых чисел. Массивы A и B 
представляют N прожорливых рыб в реке, упорядоченных вниз по течению реки.

Рыбы пронумерованы от 0 до N - 1. Если P и Q - две рыбы и P < Q, то рыба P изначально 
находится выше по течению от рыбы Q. Изначально каждая рыба занимает уникальное положение.

Число рыб P обозначается буквами A[P] и B[P]. 

Массив A содержит размеры рыбы. Все его элементы уникальны. 
Массив B содержит направления движения рыбы. Он содержит только нули и/или единицы, где:

    0 представляет рыбу, плывущую вверх по течению,
    1 изображает рыбу, плывущую вниз по течению.

Если две рыбы движутся в противоположных направлениях и между ними нет другой (живой) рыбы,
 они рано или поздно встретятся друг с другом. Тогда в живых может остаться только одна 
 рыба - большая рыба поедает меньшую. Точнее, мы говорим, что две рыбы P и Q встречаются, 
 когда P < Q, B[P] = 1 и B[Q] = 0, и между ними нет живых рыб. После встречи:

Если A [P]> A [Q], тогда P ест Q, и P все равно будет течь вниз по потоку,
Если A [Q]> A [P], тогда Q ест P, и Q все равно будет течь вверх по течению.

Мы предполагаем, что все рыбы движутся с одинаковой скоростью. То есть рыбы, движущиеся 
в одном направлении, никогда не встречаются. Цель состоит в том, чтобы подсчитать количество рыб, 
которые останутся в живых.

Например, рассмотрим массивы A и B такие, что:

  A[0] = 4  B[0] = 0
  A[1] = 3  B[1] = 1
  A[2] = 2  B[2] = 0
  A[3] = 1  B[3] = 0
  A[4] = 5  B[4] = 0

Изначально все рыбы живы и все, кроме рыбы №1, движутся вверх по течению. Рыба № 1 встречает рыбу 
№ 2 и ест ее, затем она встречает рыбу № 3 и ест ее тоже. Наконец, он встречает рыбу номер 4 и 
съедается ею. Остальные две рыбы, номер 0 и 4, никогда не встречаются и поэтому остаются в живых.


Напишите функцию:

def решение (A, B)

это, учитывая два непустых массива A и B, состоящих из N целых чисел, возвращает количество рыб, 
которые останутся в живых.

Например, учитывая массивы, показанные выше, функция должна вернуть 2, как объяснено выше.

Напишите эффективный алгоритм для следующих предположений:

N - целое число в диапазоне [1..100,000];
каждый элемент массива A является целым числом в диапазоне [0..1,000,000,000];
каждый элемент массива B является целым числом, которое может иметь одно из следующих значений: 0, 1;
все элементы A различны.

"""

import random

def fish_eater(f_size, f_direction):
    fish_stack = []
    fish_alive = len(f_size)
    if not len(f_size):
        return 0
    for i in range(len(f_size)):
        if f_direction[i] == 1:
            fish_stack.append(f_size[i])
            # print(fish_stack)
        else:
            while len(fish_stack):
                if fish_stack[-1] > f_size[i]:
                    fish_alive -= 1
                    break
                if fish_stack[-1] < f_size[i]:
                    fish_alive -= 1
                    fish_stack.pop()
                    # print(fish_stack)           
    return fish_alive

A = []
for i in range(1, 100000):
 i = random.randint(1, 1000000000)
 A.append(i)
# print(A)

B = []
for j in range(1, 100000):
 j = random.randint(0, 1)
 B.append(j)
# print(B)

print(fish_eater(A, B))
