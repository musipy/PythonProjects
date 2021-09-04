import database
#open/submit database.py file too.
def add(filename):
    print('Please enter the first and last name: ')
    key=input()
    print('Please enter the phone number: ')
    value=input()
    database.insert(filename, key, value)

def find(filename):
    print('Please enter the contact name to search: ')
    key = input()
    if is_name_exists(key,filename):
        numbercheck = database.select_one(filename,key)
        if numbercheck == None:
            print('The contact cannot be found.\n')
        else:
            print(numbercheck)
            
 
def delete(filename):
    print('Please enter the contact name to remove: ')
    key = input()
    if is_name_exists(key,filename):
        numbercheck = database.select_one(filename,key)
        if numbercheck == None:
            print('The contact cannot be found.\n')       
    database.delete(filename, key)

def update(filename):
    print('Please enter the contact name to update: ')
    key = input()
    if is_name_exists(key,filename):
        numbercheck = database.select_one(filename,key)
        if numbercheck == None:
            print('The contact cannot be found.\n')
        else:
            print('Please enter the new number to update: ')
            value = input()
            number = database.update(filename, key, value)
    
def is_name_exists(key,filename):
    f=open(filename, 'r')
    if key.lower() not in f.read().lower():
        #made program case insensitive
        #changed the case insenstive in original database module code
        print('The contact cannot be found.\n')
        f.close()
        return False
    f.close()
    return True

while True:
    print('What would you like to do with your telephone book?\nTo add a number press a\nTo find a number press f\nTo delete a number press d\nTo update a number press u\nTo quit press q')
    command = input().lower()
    if command == 'a':
        add('telephone_book.txt')
    elif command == 'f':
        find('telephone_book.txt')
    elif command == 'd':
        delete('telephone_book.txt')
    elif command == 'u':
        update('telephone_book.txt')
    elif command == 'q':
        break
        
