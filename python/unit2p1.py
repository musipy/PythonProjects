'''import random
num1=random.randint(1,50)
num2=random.randint(1,50)
prod=num1*num2
print(prod)

i=0
while i<100:
    print ("I will not run i the hall")
    i=i+1

print('what do you want to buy?')
product=input()
print ('How much does '+product+' cost?')
price=input()
print('How much do you have?')
saving=input()
if saving<product:
    print('You don\'t have enough!')
elif saving>=product:
    print('you have enough')

print('Let\'s see if you are willing to wait long enough')
print('Enter only numbers')
print('How much are you willing to invest a month?')
willing=input()
willing=int(willing)
print('How much do you need?')
need=input()
need=int(need)
print('How many months are you wiling to wait?')
wait=input()
wait=int(wait)
if willing*wait<need:
    print('You are not patient.')
elif willing*wait>=need:
    print('You are very patient')'''

print ('Do you want to play again?')
response=input()
response=response.lower()
if response=='yes':
    print('okay')
elif response=='no':
    print('okay bye')
else:
    while response != 'yes' or response != 'no':
        print('Do you want to play again?')
        response=input()
        response=response.lower()
    
    
       
