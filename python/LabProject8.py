file = open("world.txt")
 
languagelist=[]
print('What language would you like to find?')
key = input().lower()
i=0
for line in file:
    line=line.strip().lower()
    languagelist.append(line)
while i<len(languagelist) and languagelist[i] != key:
    i += 1
if i < len(languagelist):
    print( "The language is at position", i)
else:
    print( "The language was not in the list." )
def insertion_sort(languagelist):
    for key_pos in range(1, len(languagelist)):
        key_value = languagelist[key_pos]
        scan_pos = key_pos - 1
        while (scan_pos >= 0) and (languagelist[scan_pos] > key_value):
            languagelist[scan_pos + 1] = languagelist[scan_pos]
            scan_pos = scan_pos - 1
        languagelist[scan_pos + 1] = key_value
    for i in languagelist:
        print (i)
        
def check_order(languagelist,i):
    i=0
    while True:
        if languagelist[i] < languagelist[i+1]:
            i += 1
            return True
        else:
            return False

def return_check(languagelist):
    if check == True:
        print('We have checked your list')
    elif check == False:
        print('The list is not in order')

insertion_sort(languagelist,)
check = check_order(languagelist,i)
return_check(languagelist)
file.close()
