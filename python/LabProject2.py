import random

def guessnumgame():
    num=random.randint(0,50)
    print('I am thinking of a number between 0-50')
    print('You have a total of 5 guesses')
    print('What is your guess?')
    guessnum=input()
    if guessnum==str(num):
        print('congrats! you got it')
    guess=0
    while guessnum!=str(num):
        print('Nope try again!')
        guessnum=input()
        guess+=1
        if guess==4:
            print('You are out of guesses! the number was: '+str(num))
            break

guessnumgame()
    
    





