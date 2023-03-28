import random

p_again = 'yes'

while p_again == 'yes':
    number = random.randint(1, 100)
    guesses_left = 5
    
    while guesses_left > 0:
        guess = input("Guess the number between 1 to 100: ")
        
        try:
            guess = int(guess)
        except ValueError:
            print("Please enter only number.")
            continue  
        
        if guess == number:
            print("Congrats!, you guessed the right number!")
            break
        
        elif guess > number:
            print("You guessed a high number.")
        
        elif guess < number:
            print("You guessed a low number.")
        
        guesses_left -= 1
    
    else:
        print("Sorry, the number was", number)
    
    p_again = input("Do you want to play again? yes or no: ")
    
print("Thanks for playing!")

