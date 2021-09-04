import random
board = { '1' : ' ', '2' : ' ', '3' : ' ',
          '4' : ' ', '5' : ' ', '6' : ' ',
          '7' : ' ', '8' : ' ', '9' : ' '}
print ('Imagine a tic-tac-toe board labeled with the numbers from 1 through 9, one number in each box.')
blank = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
for x in board:
    print ("x=" ,x)
    comp_choice = str(random.randint(1,9))
    print ("computer choses", comp_choice)
    if (board[comp_choice] == 'x') or (board[comp_choice] not in blank):
        i = blank.index(comp_choice)
        blank.pop(i)
        comp_choice = random.choice(blank)
        board[comp_choice] = 'o'
        i = blank.index(comp_choice)
        blank.pop(i)
    elif board[comp_choice] == ' ':
        board[comp_choice] = 'o'
        i = blank.index(comp_choice)
        blank.pop(i)
    if board[comp_choice] not in blank:
        comp_choice = random.choice(blank)
    print (board)
#################################
    print ('Choose a number from 1 through 9.')
    spot = input()
    while ((board[spot] == 'o') or (board[spot] not in blank)):
        print ('choose another number.')
        spot = input()
        if board[spot] == ' ':
            board[spot] = 'x'
            j = blank.index(spot)
            blank.pop(j)
            break
################################
    if board['1'] == 'x' and board['2'] == 'x' and board['3'] == 'x':
        print ('You won!')
        break
    elif board['1'] == 'o' and board['2'] == 'o' and board['3'] == 'o':
        print ('You loose')
        break
    if board['4'] == 'x' and board['5'] == 'x' and board['6'] == 'x':
        print ('You won!')
        break
    elif board['4'] == 'o' and board['5'] == 'o' and board['6'] == 'o':
        print ('You loose')
        break
    if board['7'] == 'x' and board['8'] == 'x' and board['9'] == 'x':
        print ('You win!')
        break
    elif board['7'] == 'o' and board['8'] == 'o' and board['9'] == 'o':
        print ('You loose!')
        break
    if board['1'] == 'x' and board['4'] == 'x' and board['7'] == 'x':
        print ('You won!')
        break
    elif board['1'] == 'o' and board['4'] == 'o' and board['7'] == 'o':
        print ('You loose.')
        break
    if board['2'] == 'x' and board['5'] == 'x' and board['8'] == 'x':
        print ('You win!')
        break
    elif board['2'] == 'o' and board['5'] == 'o' and board['8'] == 'o':
        print ('You loose.')
        break
    if board['3'] == 'x' and board['6'] == 'x' and board['9'] == 'x':
        print ('You win!')
        break
    elif board['3'] == 'o' and board['6'] == 'o' and board['9'] == 'o':
        print ('You loose.')
        break
    if board['1'] == 'x' and board['5'] == 'x' and board['9'] == 'x':
        print ('You win!')
        break
    elif board['1'] == 'o' and board['5'] == 'o' and board['9'] == 'o':
        print ('You loose.')
        break
    if board['3'] == 'x' and board['5'] == 'x' and board['7'] == 'x':
        print ('You win!')
        break
    elif board['3'] == 'o' and board['5'] == 'o' and board['7'] == 'o':
        print ('You loose.')
        break
    else:
        if blank == []:
            print ('It\'s a draw!')
            break
   
        
    
    
