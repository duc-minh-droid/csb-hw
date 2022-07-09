from turtle import *  
import turtle
from time import sleep

def bai1():
    name = str(input('Input your name: '))
    print('Welcome,Mich',name,' !')

def bai2():
    fname = str(input('First name: '))
    lname = str(input('Last name: '))
    pnumber = str(input('Phone number: '))
    
    print('Your registered name is',fname,lname+'.')
    print('Your phone number is',pnumber+'.')


def bai3():
    print('Name\t\t:\tMichael')
    print('Birthdate\t:\t01/01/2001')



def bai4():
    year = str(input('What year is it? '))
    newyear = f'!!! {year} !!!  '
    
    a = '. : .'.rjust(30,' ') + '\n'
    b = '\'.  :  .\''.rjust(32,' ') + '\n'
    c = ('HAPPY NEW YEAR  '+'.  \'.:.\'  .').rjust(33,' ') + '\n'
    d = (newyear+'.  .\':\'.  .').rjust(33,' ') + '\n'
    e = '.\'  :  \'.'.rjust(32,' ') + '\n'
    f = '\' : \''.rjust(30,' ') + '\n'
    
    print(a+b+c+d+e+f)
  

s = turtle.getscreen()
t = turtle.Turtle()


def bai5():
    t.forward(50)

    for i in range(2):
        t.left(120)
        t.forward(100)

    t.left(120)
    t.forward(50)
    t.left(90)
    sleep(3)
  
def bai6():
    for i in range(4):
        t.forward(100)
        t.left(90)
        
    t.penup()
    
    for i in range(2):
        t.right(90)
        t.forward(25)
    
    t.pendown()
    t.width(2)
    
    for i in range(4):
        t.right(90)
        t.forward(150)
    
    sleep(5)
    
def bai7():
    for i in range(4):
        t.forward(100)
        t.left(90)
        
    t.penup()
    t.forward(50)
    t.right(90)
    t.forward(25)
    t.left(135)
    t.pendown()
    
    for i in range(4):
        t.forward(100)
        t.left(90)
    
    sleep(3)














