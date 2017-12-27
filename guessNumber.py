# Guess the number game

import random
secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')
print('You have 5 tries.')

# Ask the player for a guess
for guessTaken in range(1, 6):
    if guessTaken > 1:
        print('Guess again.')
    else:
        print('Take a guess.')
        
    guess = int(input())

    if guess > secretNumber:
        print('Your number is too high.')
    elif guess < secretNumber:
        print('Your number is too low.')
    else:
        break # Guessed correctly!

if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessTaken) + ' guesses!')
else:
    print('Sorry, the number I was thinking of was ' + str(secretNumber) + '.')