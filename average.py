# python version 3.10.5

print('\n*** This programme will generate the average for you ***')

# primary loop
while True:

    # list to add user added values
    li0 = []

    print('Insert the word calculate when you are finished with the values')
    print('Insert the nubmers one by one to get the average\n')

    # logic: user can add unlimited values unless he/she types calculate
    # note values are in string format
    while True:
        
        #getting user input
        inp = input('Insert the nubmer: ')
        if inp == 'calculate':
            break
        else:
            li0.append(inp)
    
    # converting string list into integer list
    li1 = list(map(int, li0))

    # average formula
    avg = sum(li1)/len(li1)

    print(f'\nAverage of the given numbers are: {avg}')

    # asking user to quite/continue program
    conf = input(f'\nIf you want you exit insert yes: ')

    # condition to exit primary loop
    if conf == 'yes':
        break
