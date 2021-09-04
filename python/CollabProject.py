import random


class game:
    def inputPlayerLetter():
        # Lets the player type which letter they want to be.
        # Returns a list with the player's letter as the first item, and the computer's letter as the second.
        letter = ''
        while not (letter == 'X' or letter == 'O'):
            print('Does player 1 want to be X or O?')
            letter = input().upper()
            if letter == 'X':
                print('Player 2 will be O.')
            elif letter == 'O':
                print('Player 2 will be X.')
        # the first element in the tuple is the player's letter, the second is the computer's letter.
        if letter == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']

    def whoGoesFirst():
        # Randomly choose the player who goes first.
        if random.randint(0, 1) == 0:
            return 'player 2'
        else:
            return 'player 1'
    
    def run_game():
        theBoard, playLetter, computerLetter, turn = Start.start_game()
        gameIsPlaying = True
        while gameIsPlaying:
            if turn == 'player 1':
                # Player 1 turn.
                player1 = Player.playgame(playLetter, theBoard, turn)

                if End_game.isWinner(theBoard, playLetter):
                    Player_move.drawBoard(theBoard)
                    print('Hooray! Player 1 won the game!')
                    gameIsPlaying = False
                else:
                    if End_game.isBoardFull(theBoard):
                        Player_move.drawBoard(theBoard)
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'player 2'

            elif turn == 'player 2':
                player2 = Player.playgame(computerLetter, theBoard, turn)
    
                if End_game.isWinner(theBoard, computerLetter):
                    Player_move.drawBoard(theBoard)
                    print('Hooray! Player 2 won the game!')
                    gameIsPlaying = False
                else:
                    if End_game.isBoardFull(theBoard):
                        Player_move.drawBoard(theBoard)
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'player 1'

        if End_game.playAgain():
            theBaord = [' ']*10
            game.run_game()
        

class Player_move:
    def __init__(self, board, move):
        self.board = board
        self.move = move
        
    def makeMove(board, letter, move):
        board[move] = letter
        
    def isSpaceFree(board, move):
        # Return true if the passed move is free on the passed board.
        return board[move] == ' '
    
    def getPlayerMove(turn, board):
        # Let the player type in his move.
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not Player_move.isSpaceFree(board, int(move)):
            print('What is ' +turn+'\'s move? (1-9)')
            move = input()
        return int(move)
    
    def drawBoard(board):
        # This function prints out the board that it was passed.
    
        # "board" is a list of 10 strings representing the board (ignore index 0)
        print('7   |8   |9')
        print('  '+ board[7] + ' | ' + board[8] + '  | ' + board[9])
        print('    |    |')
        print('--------------')
        print('4   |5   |6')
        print('  ' + board[4] + ' | ' + board[5] + '  | ' + board[6])
        print('    |    |')
        print('--------------')
        print('1   |2   |3')
        print('  '  +board[1] + ' | ' + board[2] + '  | ' + board[3])
        print('    |    |')
        
class Player:
    def playgame(playLetter, theBoard, turn):
        Player_move.drawBoard(theBoard)
        move = Player_move.getPlayerMove(turn, theBoard)
        Player_move.makeMove(theBoard, playLetter, move)

class End_game:
    def isBoardFull(board):
        # Return True if every space on the board has been taken. Otherwise return False.
        for i in range(1, 10):
            if Player_move.isSpaceFree(board, i):
                return False
        return True
    
    def isWinner(bo, le):
        # Given a board and a player's letter, this function returns True if that player has won.
        # We use bo instead of board and le instead of letter so we don't have to type as much.
        return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
        (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
        (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
        (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
        (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
        (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
        (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
        (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

    def playAgain():
        # This function returns True if the player wants to play again, otherwise it returns False.
        print('Do you want to play again? (yes or no)')
        return input().lower().startswith('y')

class Start:
        def start_game():
            theBoard = [' ']*10
            print('Welcome to the game of Tic Tac Toe!')
            print('There are two players, player 1 and player 2')
            playLetter, computerLetter = game.inputPlayerLetter()
            turn = game.whoGoesFirst()
            print('The '+ turn +' will go first.')
            return [theBoard, playLetter, computerLetter, turn]
  

game.run_game()

