'''nums=[396, 461, 701, 852, 377, 957, 521, 714, 573, 814, 534, 121, 345, 513, 643, 411, 643, 280, 329, 474, 756, 855, 816, 389, 618, 484, 921, 395, 480, 608, 733, 768, 839, 815, 319, 886, 456, 269, 683, 829, 811, 783, 264, 415, 943, 751, 744, 849, 935, 713, 293, 653, 748, 475, 453, 401, 368, 780, 995, 533, 619, 953, 279, 195, 688, 988, 843, 428, 984, 979, 385, 898, 230, 249, 566, 903, 967, 519, 967, 416, 295, 391, 422, 743, 726, 237, 588, 764, 979, 133, 818, 744, 688, 749, 225, 935, 338, 865, 171, 345, 379, 210, 675, 802, 234, 999, 657, 136, 403, 681, 345, 191, 776, 738, 301, 678, 980, 111, 755, 199, 410, 231, 955, 257, 759, 661, 758, 241, 715, 547, 186, 629, 125, 325, 779, 357, 896, 740, 215, 253, 485, 294, 844, 862, 653, 995, 796, 509, 353, 383, 992, 618, 378, 408, 369, 842, 403, 950, 415, 542, 380, 116, 740, 470, 437, 451, 658, 369, 647, 406, 229, 457, 337, 970, 162, 124, 728, 285, 716, 428, 408, 422, 373, 689, 198, 165, 888, 372, 444, 710, 228, 984, 802, 880, 920, 561, 654, 174, 881, 479]
choosenums=[153, 486, 729, 183, 426, 759]
def checknums(num):
    if num in nums:
        print(str(num) +' is in the list.')
    elif num not in nums:
        print(str(num)+' is not in the list.')
    else:
        print('whoops')
for i in choosenums:
    checknums(i)

namelist=[]
def namelistcreator():
    print('Give me a name that you would like to add to the list.')
    name=input()
    namelist.append(str(name))
    print('Do you want to add another name?\nType yes if you want to add another names or anything else if you want to stop.')
    response=input()
    if response=='yes':
        namelistcreator()
    elif response != 'yes':
        namelist.reverse()
        print(namelist)
namelistcreator()

names=['Gilberto', 'Christiana', 'Amie', 'Vance', 'Denise', 'Rutha', 'Otha', 'Reita', 'Yuriko', 'Jacques']
for i in names:
    print('would you like to have the name upper or lower case?')
    case=input()
    case=case.lower()
    if 'lower' in case:
        i=i.lower()
        print(i)
    elif 'upper' in case:
        i=i.upper()
        print(i)

nums=list(range(0,10))
print(nums)

for i in range(1,11):
    print(i)
    print('hi')

cheese = ['mozzarella', 'cheddar', 'provolone', 'caprice des dieux'] 
selection = cheese[2:]
print(selection)

def chooseCave(): 
     cave = '' 
     while cave != '1' and cave != '2': 
          print('Which cave will you go into? (1 or 2)') 
          cave = input() 
     return cave
chooseCave()

i = 0 
while i < 5: 
     print(i) 
     i= i + 1 
     if i == 3: 
          break

def dayOfWeek(): 
     d5=d1 
d5='Friday' 
d1='Monday' 
dayOfWeek() 
print(d5)

def colorPrinter(green): 
     print(green) 
green='blue' 
colorPrinter(green)

spam = 'yummy' 
def spamNotYummy(): 
     spam = 'gross' 
spamNotYummy() 
print(spam)

words = {'bumfuzzle': 'confuse; perplex; fluster', 'cattywampus': 'askew, awry, kitty-corner', 'taradiddle': 'a fib or pretentious nonsense', 'billingsgate': 'coarsely abusive language', 'snickersnee': 'a large knife', 'widdershins': 'in a left-handed or contrary direction; counterclockwise', 'collywobbles': 'pain in the abdomen and expecially in the stomach; a bellyache', 'dipthong': 'two vowel sounds joined in one syllable to form one speech sound, e.g. the sounds of "ou" in out and of "oy" in boy'} 

print('What word would you like to know the definition of?')
word=input().lower()
while word not in words:
    print('That word is not in the list.\nPlease try again.')
    word=input().lower()

print(words[word])'''




























