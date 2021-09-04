import time

def playername():
    #asks player for their name
    print('Hello to the detective game.')
    print('This is a single player.')
    print('What is your name detective?')
    return input()

def whichcase():
    #asks which forensic case the player wants to play
    print('Which case will you like to take?(1 or 2)')
    casenum=input()
    while casenum!='1' and casenum!='2':
        #if their input isn't 1 or 2, asks again till it is.
        print('Please enter 1 or 2')
        casenum=input()
    print('You have chosen case '+casenum)
    return casenum

def playcase(casenum):
    #calls the corresponding function for the case
    if casenum=='1':
        case1(name, points)
    elif casenum=='2':
        case2(name, points)

scene11=['a body with a stab wound','buttered knife with blood','a witness','camera footage']
witness1='I couldn\'t see clearly. The person was a man.\nHe robbed the cafe and was wearing a black parka, red sweatpants, and a black ski mask.\nHis parka had a sybol that looked like this:'
parkasymbol1 = ['''
       |______|
      |        |
     <><><><><><>
      |        |
       |------|           ''']


camera1='He robbed the bank and stabbed the body.\nHe was holding a swiss army pocket knife\nand used it with his left hand.'

def scene1():
    #starts off the game if you chose case 1. The program that puts this as part of the full program will be made later on, after finishing all the scenes and cases.
    keepgoing=True
    print('You have entered crimescene 1')
    time.sleep(1)
    print('At the crimescene, you find these evidences:')
    for i in scene11:
        print(i)
    time.sleep(2)
    while keepgoing == True:
        print('What would you like to investigate further?')
        investigate=input()
        if 'witness' in investigate:
            print('Here is the witness\'s satatement:')
            print(witness1)
            for i in parkasymbol1:
                print(i)
        elif 'knife' in investigate:
            print('The blood on the knife matches the body\'s blood. There are no fingerprints.')
        elif 'camera' in investigate:
            print(camera1)
        print('would you like to investigate something else?')
        response=input()
        if response.startswith('y'):
            keepgoing = True
        else:
            keepgoing = False
Bob=[]
Joe=[]
Jack=[]
suspectspointers={'Bob':Bob, 'Joe':Joe, 'Jack':Jack}
Bobresponse='I am his friend. We knew each other since 7th grade.\nI have not been able to contact him for sometime. During the time of crime, I was at Joe\'s house along with Jack.'
Joeresponse='Me, Bob, and Joe were at my house having lunch. We were just hanging out. While we were talking, Bob said he\'ll go out to get some snacks.\nMy house is close to the cafe, and the grocery store is on the other side of the cafe.'
Jackresponse='I was at Joe\'s house. I went there with Bob. He was walking out in the cold without any jacket, so I kept teasing him for it.On our way there, he asked about a knife for hunting. I gave him my pocket knife, finding it wierd for him to as, a question.\nHe doesn\'t go hunting. He left to get snacks for us and came back about 2 hours later.'
def scene2responses():
    keepgoing=True
    print('You move on to investigate further about the scene.\n You found three suspects, and one of them is the one that committed the crime.')
    print('You ask them questions about the crime scene.')
    time.sleep(1)
    print('Here are their responses.')
    print('Bob:',Bobresponse)
    time.sleep(10)
    print('Joe:',Joeresponse)
    time.sleep(10)
    print('Jack:',Jackresponse)
    time.sleep(10)

def scene2finish():
    i=0
    keepgoing = True
    print('what points would you like to add under each person\'s name?\n(ex:Joe parka)')
    note=str(input().lower())
    name=note[:4]
    bullet=note[4:]
    print(name)
    while name != 'bob ' and name != 'joe ' and name != 'jack':
        print('please enter the name of the suspect,a space, and the bullet point\nEx: Joe parka')
        note = str(input().lower())
        print(note)
        name = note[:4]
        bullet=note[4:]
    if name =='bob ':
        Bob.append(bullet)
    elif name == 'joe ':
        Joe.append(bullet)
    elif name == 'jack':
        Jack.append(bullet)
    while keepgoing==True:
        print('Would you like to see what you have under the name of the suspects?')
        answer=str(input().lower())
        print(answer)
        if 'y' in answer:
            print(suspectspointers)
        print('Would you like to add something else?')
        response=input().lower()
        if 'y' in answer:
            print('What would you like to add?')
                note=str(input().lower())
                name=note[:4]
                bullet=note[4:]
                print(name)
                while name != 'bob ' and name != 'joe ' and name != 'jack':
                    print('please enter the name of the suspect,a space, and the bullet point\nEx: Joe parka')
                    note = str(input().lower())
                    print(note)
                    name = note[:4]
                    bullet=note[4:]
                if name =='bob ':
                    Bob.append(bullet)
                elif name == 'joe ':
                    Joe.append(bullet)
                elif name == 'jack':
                   Jack.append(bullet)
        elif 'n' in answer:
            keepgoing == False

def finale(tries,points):
    print('We have reached the end of the game')
    print('Who do you think is the murderer?')
    print('If you get it right on the first try, then you get 5 points.\nSecond try three points\nand third try 1 point.')
    print('If you take more than three tries, you will get 0 points.')
    time.sleep(5)
    print('who do you think is the murderer?')
    gameanswer=input().lower()
    if gameanswer=='bob' and tries==0:
        points=5
        print('congrats! you get',points,'points!')
    elif gameanswer == 'bob' and tries == 1:
        points=3
        print('congrats! you get',points,'points!')
    elif gameanswer == 'bob' and tries == 2:
        points=1
        print('congrats! you get',points,'point!')
    elif gameanswer == 'bob' and tries > 2:
        points=0
        print('congrats! you get',points,'points.')
    if gameanswer != 'bob':
        tries += 1
        
        
def game():
    tries=0
    points=0
    name=playername()
    scene1()
    scene2responses()
    scene2finish()
    finale(tries,points)
   
game()
