import random

# defining game logic
def gameLogic(comp, player):
    if comp == player:
        return None

    elif comp == 'r':
        if player == 's':
            return False
        if player == 'p':
            return True

    elif comp == 'p':
        if player == 'r':
            return False
        elif player == 's':
            return True

    elif comp == 's':
        if player == 'p':
            return False
        elif player == 'r':
            return True

# generating random number and assigning it a value from rock, paper and scissor
print('\nComputer Chose its value now its your turn!')
rNo = random.randint(1, 3)
if rNo == 1:
    comp = 'r'
elif rNo == 2:
    comp = 'p'
elif rNo == 3:
    comp = 's'

# user input 
player = input('Enter Rcok(r), Paper(p) or Scissor(s): ')

res = gameLogic(comp, player)

if res == None:
    print('Match Tied!')
elif res:
    print('Congrates You Won!')
else:
    print('You Lost.')

print(f'Computer Chose: {comp}')
print(f'You Chose: {player}')
