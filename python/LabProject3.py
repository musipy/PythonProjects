import time
import random

def getname():
    print('What is the name of your character?')
    name=input()
    print (name)
    return name

def intro(name):
    print(str(name) +' enters a spooky part of the woods')
    print('There you see three caves')
    print('Only one of the caves has a friendly dragon which will give you a big hug and let you pass')

def choosecave(name):
    print('Which cave will '+str(name)+' enter?(1,2,or 3)')
    cave = input()
    while cave !='1' and cave !='2' and cave !='3':
        print('Which cave will '+name+' enter?(1,2, or 3)')
        cave = input()
    return cave

def goincave(cavenum, name):
    print(name +' enters cave '+str(cavenum))
    time.sleep(3)
    print(name+ ' sees a dragon...')
    time.sleep(3)
    print('And it...')
    time.sleep(3)
    hugcave=random.randint(1,3)
    if str(cavenum)==str(hugcave):
        print('gives '+name+' a big hug!')
    else:
        print('eats '+name+' for its snack!')

def play():
    print('Would you like to play again?(y/n)')
    playagain=input()
    while playagain != 'y' and playagain != 'n':
        print('Would you like to play again?(y/n)')
        playagain=str(input())
    if playagain == 'y':
        name=getname()
        intro(name)
        cave = choosecave(name)
        goincave(cave, name)
        play()
    elif playagain == 'n':
        print('Bye!')


name = getname()
intro(name)
cave = choosecave(name)
goincave(cave, name)
play()
    
