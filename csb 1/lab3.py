#bai1

def bai1():
    num = int(input('Input number: '))
    print(f'{num} is even') if num%2==0 else print(f'{num} is odd')

#bai2

def bai2():
    num = input('Input number: ')
    try:
        num = int(num)
        print(f'{num} is an integer')
    except:
        num = float(num)
        print(f'{num} is not an integer')
    
#bai3

def bai3():
    num = input('Input character: ')
    try:
        num = int(num)
        print(f'{num} is a digit')
    except:
        try:
            num = float(num)
            print(f'{num} is a digit')
        except: 
            print(f'{num} is not a digit')
        
#bai4

def bai4():
    n = int(input('Input character: '))
    if n%3==0 and n%5==0:
        print(f'{n} is divisible by 3 and 5')
    elif n%3==0 and not (n%5==0):
        print(f'{n} is divisible by 3')
    elif not(n%3==0) and n%5==0:
        print(f'{n} is divisible by 5')
    else:
        print(f'{n} is not divisible by 3 or 5')
        
#bai5

def bai5():
    print('Welcome to The Ultimate Security System')
    u = input('Username: ')
    p = input('Password: ')
    print('You are logged in, admin.') if u=='admin' and p =='12345' else print('Wrong username or password.')

#bai6

def bai6():
    x = input('Input length 1: ')
    y = input('Input length 2: ')
    z = input('Input length 3: ')
    try:
        x = int(x)
        y= int(y)
        z = int(z)
        print('The 3 line segments can form a triangle.') if x+y>z and y+z>x and z+x>y else print('The 3 line segments cannot form a triangle.')
    except:
        x = float(x)
        y= float(y)
        z = float(z)
        print('The 3 line segments can form a triangle.') if x+y>z and y+z>x and z+x>y else print('The 3 line segments cannot form a triangle.')
            
#bai7
from turtle import *

def bai7():
    x = input('Input length 1: ')
    y = input('Input length 2: ')
    z = input('Input length 3: ')
    def run():
        if x+y>z and y+z>x and z+x>y: 
            if x==y and x==z:
                print('The 3 line segments can form an equilateral triangle.')
                for i in range(3):
                    forward(x)
                    left(120)
                mainloop()
            elif x**2+y**2==z**2 or y**2+z**2==x**2 or x**2+z**2==y**2:
                print('The 3 line segments can form a right triangle.')
            else:
                print('The 3 line segments can form a triangle.')
        else:
            print('The 3 line segments cannot form a triangle.')
        
    try:
        x = int(x)
        y= int(y)
        z = int(z) 
        run()
    except:
        x = float(x)
        y= float(y)
        z = float(z)
        run()
