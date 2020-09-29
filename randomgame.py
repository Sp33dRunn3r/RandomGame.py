#Random game exercise:
from random import randint
import sys

answer = randint(int(sys.argv[1]), int(sys.argv[2]))


while True:
    try:
        guess = int(input('guess a number 1~10: '))
        if 0 < guess < 11:
            if guess == answer:
                print("You are a genius! Thank you for playing!")
                break
                quit()
            else:
                print("Try again!")
                continue
    except ValueError:
        print('Please enter a number... ')
        continue
