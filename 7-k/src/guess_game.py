# coding: utf-8
# Guess number game
from random import randint


if __name__== '__main__':

    x = randint(0, 10)
    while True:
        
        guess = int(input('Skazhi chislo '))

        if guess > x:
            print(f'It a little bit smaller!')
        elif x == guess:
            print(f'You find X!', x)
        else:
            print(f'It little bigger, try again!')
        
