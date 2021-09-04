#Area calculator#
import math

def numAsk():
    print('How many sides does the shape you want to find the area of have? Please enter a whole(positive) number.')
    side_num=input()
    while side_num.isdigit() != True:
        print('Enter a valid value.')
        side_num = input()
    return (int(side_num))

def rect_check_area():
    print('What is the height?')
    height=input()
    while height.isdigit() != True:
        print('Enter a valid value.')
        height = input()
    print('What is the width?')
    width = input()
    while width.isdigit() != True:
        print('Enter a valid value.')
        width = input()
    area=(int(height)*int(width))
    return (area)

def lengthAsk():
    print('What is the length of each side? Please enter a whole number.')
    side_length=input()
    while side_length.isdigit() != True:
        print('Enter a valid value.')
        side_length = input()
    return (int(side_length))

def circle(side_length):
    area=math.pi*(side_length*side_length)
    return (area)

def equal_triangle(side_length):
    area=(side_length*side_length*((math.sqrt(3))/4))
    return (area)

def right_triangle():
    print('What is the length of the base?')
    base = input()
    while base.isdigit() != True:
        print('Enter a valid value.')
        base = input()
    print('What is the length of the height?')
    height = input()
    while height.isdigit() != True:
        print('Enter a valid value.')
        height = input()
    area = (int(base)*int(height))/2
    return (area)

def iso_triangle():
    print('What is the length of the base?')
    base = input()
    while base.isdigit() != True:
        print('Enter a valid value.')
        base = input()
    print('What is the length of one of the legs?')
    leg = input()
    while leg.isdigit() != True:
        print('Enter a valid value.')
        leg = input()
    base_half = (int(base))/2
    height = math.sqrt((int(leg)*int(leg))-(base_half*base_half))
    area = (height*int(base))
    return (area)

def square (side_length):
    area = (side_length*side_length)
    return (area)

def shape_area(side_num, side_length):
    tri_angle = 360/(side_num*2)
    height = (side_length/2)/(math.tan(math.radians(tri_angle)))
    mini_area = (side_length*height)/2
    area = mini_area*side_num
    return(area)

def playAgain():
    print('Would you like to play again (y/n)?')
    again = input().lower()
    if again.startswith('y'):
        play(menu)
    else:
        pass

def shape_greater_than5(side_num):
    side_length = lengthAsk()
    area = shape_area(side_num, side_length)
    print('Area =', area)
    playAgain()
        
menu = ['1. Circle', '2. Equilateral Triangle','3. Right Triangle', '4. Isosceles Triangle', '5. Rectangle', '6. Square', '7. Pentagon', '8. Hexagon', '9. Heptagon (7 sides)', '10. Octagon', '11. Other Polygon']

def play(option_list):
    print('Welcome to the area finder!')
    print('Below is a menu where you can choose which shape you want to find the area of.')
    for i in option_list:
        print(i)
    print('Select a number corresponding to a shape on the menu.(1-11)')
    shape_option = input()
    while shape_option != '1' and shape_option != '2' and shape_option != '3' and shape_option != '4' and shape_option != '5' and shape_option != '6' and shape_option != '7' and shape_option != '8' and shape_option != '9' and shape_option != '10' and shape_option != '11' :
        print('Enter a valid option.')
        shape_option = input()
    if shape_option == '1':
        print('What is the length of the radius?')
        side_length=input()
        while side_length.isdigit() != True:
            print('Enter a valid value.')
            side_length = input()
        area = circle(int(side_length))
        print('Area =', area)
        playAgain()
    elif shape_option == '2':
        side_length = lengthAsk()
        area = equal_triangle(side_length)
        print('Area =', area)
        playAgain()
    elif shape_option == '3':
        area = right_triangle()
        print('Area =', area)
        playAgain()
    elif shape_option == '4':
        area = iso_triangle()
        print('Area =', area)
        playAgain()
    elif shape_option == '5':
        area = rect_check_area()
        print('Area =', area)
        playAgain()
    elif shape_option == '6':
        side_length = lengthAsk()
        area = square(side_length)
        print ('Area =', area)
        playAgain()
    elif shape_option == '7':
        side_num = 5
        shape_greater_than5(side_num)
    elif shape_option == '8':
        side_num = 6
        shape_greater_than5(side_num)
    elif shape_option == '9':
        side_num = 7
        shape_greater_than5(side_num)
    elif shape_option == '10':
        side_num = 8
        shape_greater_than5(side_num)
    elif shape_option == '11':
        side_num = numAsk()
        while side_num <= 8:
            print('Enter a value above 8.')
            side_num = input()
        side_num = int(side_num)
        shape_greater_than5(side_num)


play(menu)                    
            
                


    
    
    
    
    
    
