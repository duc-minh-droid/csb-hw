from turtle import *

def sequence3to12():
    for x in range(3,13):
        print(x)
        
def sequence0toN():
    n = int(input('Input a number: '))
    if n > 0:
        for i in range(n+1):
            print(i)
        
def sequence0toNodd():
    n = int(input('Input a number: '))
    if n > 0:
        for i in range(n+1):
            if i%2==1:
                print(i)
            
def custom_polygon():
    edge = int(input('Input number of edges: '))
    angle = 180 - ((edge-2)*180/edge)
    for i in range(edge):
        forward(100)
        left(angle)
    mainloop()
    
