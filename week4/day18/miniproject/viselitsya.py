import random

words = ['summer', 'autumn', 'winter', 'spring', 'love']
secret = random.choice(words)
hidden_word = list("*" * len(secret))
attempts = 5

while attempts > 0:
    letter = input(f'\n\n\nGuess the word {hidden_word}\nNumber of attempts {attempts}\nEnter letter: ').lower().strip()
    if letter == secret:
        print(f'You found the word "{secret}"! Congrats!')
        break
    if letter in secret:
        for index, value in enumerate(secret):
            if letter == value:
                hidden_word[index] = letter
        if '*' not in hidden_word:
            print(f'You found the word "{secret}"! Congrats!')
            break
    else:
        attempts -= 1
        if attempts < 5: print('  |  ')
        if attempts < 4: print('  O  ')
        if attempts < 3: print(' /|\ ')
        if attempts < 2: print('  |  ')
        if attempts < 1: print(' / \ ')
    if attempts == 0:
        print(f'You loose, secret word was "{secret}":(')
        break