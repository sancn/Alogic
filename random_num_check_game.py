
# #program that check guess the random number if guess is correct 
# #print congrats otherwise give five more chance to guess.

import random

number = random.randint(1, 100)

guess = int(input("Guess a number between 1 & 100: "))

if guess == number:
    print("Congratulations!, Guess number is:",guess)
    print("*****************************")

else:
    for i in range(5):
        guess = int(input("Incorrect. Guess again: "))
        if guess == number:
            print("Congratulations!, Guess number is:",guess)
            break
    else:
        print("Sorry, you are wrong. It was", number)
