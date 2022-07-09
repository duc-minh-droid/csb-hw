from code import interact
import math

# bai 1
def bai1():
    pi = math.pi
    rad = float(input('Radius: '))
    p = round(pi*2*rad, 5)
    s = round(pi*(rad**2), 5)
    print(f'Perimeter: {p}')
    print(f'Area: {s}')
    
# bai 2
def bai2():
    a = float(input('Length of edge: '))
    b = math.sqrt(2*(a**2))
    print(f'Length of diagonal line: {b}')
    
def bai3():
    an = str(input('Account name: '))
    dn = str(input('Domain name: '))
    fe = '@'.join([an, dn])
    print(f'Full email: {fe}')

def bai4():
    inp = str(input('Date in MM/DD/YYYY format: '))
    day = inp[3:5]
    month = inp[0:2]
    year = inp[6:]
    output = '/'.join([day,month,year])
    print(f'Date in DD/MM/YYYY format: {output}')

def bai5():
    deposit = float(input('Deposit: '))
    
    def account_interest(year):
        print(f'Account after {year} years: {deposit*((105/100)**year)}')
    account_interest(1)
    account_interest(2)
    account_interest(10)
    
from turtle import *

def bai6():
    forward(200)
    pencolor('#de5246')
    pensize(10)
    left(90)
    forward(180)
    left(135)
    forward(145)
    right(90)
    forward(145)
    left(135)
    forward(180)
    backward(180)
    left(90)
    pencolor('black')
    pensize(1)
    penup()
    forward(5)
    pendown()
    forward(200)
    
def bai7():
    def thoi(color):
        pencolor(color)
        pensize(10)
        left(30)
        forward(100)
        left(120)
        forward(100)
        left(60)
        forward(100)
        left(120)
        forward(100)
    
    thoi('#cf8f03')
    penup()
    left(30)
    forward(50)
    pendown()
    thoi('#0b2c3c')
    

mainloop()