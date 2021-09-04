import time
import random

def intro():
    print('You enter a spooky part of the woods')
    print('There you see three caves')
    print('Only one of the caves has a friendly dragon which will give you a big hug and let you pass')

def choosecave():
    print('Which cave will you enter?(1,2,or 3)')
    cave = input()
    while cave !='1' and cave !='2' and cave !='3':
        print('Which cave will you enter?(1,2, or 3)')
        cave = input()
    return cave

def goincave(cavenum):
    print('You enter cave '+str(cavenum))
    time.sleep(3)
    print('You see a dragon...')
    time.sleep(3)
    print('And it...')
    time.sleep(3)
    hugcave=random.randint(1,3)
    if str(cavenum)==str(hugcave):
        print('It gives you a big hug!')
    else:
        print('It eats you for its snack!')

def play():
    intro()
    cave = choosecave()
    goincave(cave)
    print('Would you like to play again?(y/n)')
    playagain=input()
    while playagain != 'y' and playagain != 'n':
        print('Would you like to play again?(y/n)')
        playagain=str(input())
    if playagain == 'y':
        cave = choosecave()
        goincave(cave)
    elif playagain == 'n':
        print('Bye!')

play()
    
