print('Hello, guess what number I am thinking of:')

import random

# set initial values
#examples used from http://codereview.stackexchange.com/questions/65140/guess-my-number-classic-edition

numChosen = random.randint(1,100)
guess = int(input("Take a guess: "))
tries = 1


while guess != numChosen:
    if guess > numChosen:
          print("Try a lower number...")
    else:
          print("Try a higher number...")

    guess = int(input("Take a guess: "))
    tries += 1


    if tries == 5:
        print("You only get 5 tries! Sorry, you loose!")
        break

    if guess == numChosen:
        print("You guessed it! The number was:", numChosen)
        print("It took", tries, "guesses!")
