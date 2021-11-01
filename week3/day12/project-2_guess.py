import random
name = input('Your name: ')
number = random.randint(1, 15)
wish = input('would you like to play?: ')
print(number)


lives = 0
while True:
    lives += 1
    if lives > 6:
        print('You loose =(')
        wish = input('would you like to play again?: ')
        number = random.randint(1, 15)
        lives = 0
        continue
    if wish.lower().strip() == 'yes':
        try:
            guess_number = int(input(f'Guess number from 1 till 15. You have 6 attempts. Guess number. Attempt # {lives}: '))
        except ValueError:
            print('Enter number not string')
            continue
        if guess_number == number:
            print(f'{name}, You win!')
            number = random.randint(1, 15)
            wish = input('would you like to play again?: ')
            lives = 0
    elif wish.lower().strip() == 'no':
        print(f'Till next time, {name}')
        break
    else:
        print('Enter "yes" or "no"')
        lives = 0
        break