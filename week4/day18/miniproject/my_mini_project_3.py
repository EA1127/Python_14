words = ['summer', 'autumn', 'winter', 'spring', 'love']

import random
word_chosen = random.choice(words)
print(word_chosen)
word_hidden = len(word_chosen)*'*'
print(word_hidden)

guess_letter = input('Enter a letter you guess: ')

attempts = sum(list(map(lambda x: len(x), words)))
# print(attempts)


for index_c in range(len(list(word_chosen))):
    if guess_letter == list(word_chosen)[index_c]:
        print(list(word_chosen)[index_c])
        print(index_c)
        # list(word_hidden)[index_c] = list(word_chosen)[index_c]
        # print(list(word_hidden)[index_c])
        word_hidden_l = list(map(lambda i: list(word_chosen)[index_c], word_hidden))
        print(word_hidden_l)
            
 

