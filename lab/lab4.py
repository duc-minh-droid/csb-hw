
def bai1():
    n = int(input('Input number: '))
    for i in range(n):
        line = ''
        for j in range(i+1):
            line+='#'
        print(line)
    
def bai2():
    n = float(input('Input a positive number: '))
    if (n<=0):
        bai2()
    else:
        print('Thank you.')

def bai3():
    n = int(input('Input number: '))
    if n==0:
        print('0! == 1')
    elif n<0:
        print('Invalid')
    else:
        factorial = 1
        for i in range(1,n+1):
            factorial = factorial*i
        print(f'{n}! = {factorial}')
    
def bai4():
    n = input('Input number: ')
    n = [int(x) for x in n]
    sum = 0
    for i in n:
        sum = sum + i
    print(sum)

def bai5():
    def tong_chu_so(num):
        sum = 0
        n = [int(x) for x in str(num)]
        for i in n:
            sum = sum + i
        return sum

    result = ''
    num_count = 0
    for i in range(1000, 1500):
        if num_count == 10:
            break
        if tong_chu_so(i)==9:
            num_count = num_count+1
            result = result + str(i) + " "
        
    print(result)

from turtle import *  
     
def bai6():
    n = int(input('Input number of edges: '))
    if n <=2:
        bai6()
    
    angle = 180-(((n-2)*180)/n)
    for i in range(n):
        forward(50)
        left(angle)
    
    mainloop()
    
def bai7():
    speed(20)
    for i in range(100):
        circle(i+10,45)
    mainloop()
    