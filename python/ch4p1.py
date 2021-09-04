'''list1=[1,2,3,4,5]
list2=[6,7,8,9,10]
i=0
i2=0

while i2 <= len(list2):
    print(list1[i]*list2[i2])
    i2 += 1
    if i2==len(list2):
        i2=0
        i += 1
        if i==len(list1):
            break
numDigits = 3 
numbers = [9, 4, 5, 1, 2, 7, 0, 3, 6, 8] 
secretNum = '' 
for i in range(numDigits): 
    secretNum += str(numbers[i]) 
print(secretNum)

board = [] 
number = 0 

for x in range(100): 
    board.append([]) 
    for y in range(50): 
        board[x].append(number) 
        number += 1 
print(board)'''

values = [[3, 4, 4, 1], [7, 10, 1, 2]] 

v = values[0][0] 
for row in range(0, len(values)): 
    for column in range(0, len(values[row])): 
         if v < values[row][column]: 
              v = values[row][column] 
print(v)

    
    
        

    
    
