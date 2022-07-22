import random

# generating random number from 1 to {num} numbers.
num = 10
randNumber = random.randrange(1, num)
print(randNumber)

# user input will repeat itself until the user guess the right number and track the number of tries of the user.
userGuess = None
guess = 0
while userGuess != randNumber:
    guess += 1
    userGuess = int(input('Insert your guess: '))
    if userGuess == randNumber:
        print('Your have guessed it right!')
    else:
        if userGuess < randNumber:
            print('Insert larger number!')
        else:
            print('insert smaller number!')

print(f'you have gussed right numbers in {guess} tries!')

# opening a file reading it if it has any previous high value.
with open('hiscore.txt', 'r') as f:
    highscore = int(f.read())
    
    
# storing new high value in text file and saving it.
if guess < highscore:
    with open('hiscore.txt', 'w') as f:
        f.write(str(guess))
