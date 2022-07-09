from turtle import *
# DUc MiNH

def fullname():
    fn = input('First name: ')
    ln = input('Last name: ')
    print(f'Your full name is {fn} {ln}')
    
def capitalized_name():
    inp = input('Your input: ')
    print(f'Your input: {inp}')
    print(f'Capitalized: {inp.upper()}')

def square_number():
    num = int(input('Input a number: '))
    print(f'Input a number: {num}')
    print(f'Square input: {num**2}')
    
def custom_radius():
    rad = float(input("Input circle's radius: "))
    circle(rad)
    mainloop()
    
