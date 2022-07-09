
def larger_than13():
    n = int(input('Input a number: '))
    if n > 13:
        print('This number is not larger than 13')
    else: 
        print('This number is larger than 13')
        
def even_check():
    n = int(input('Input a number: '))
    if n % 2 == 0:
        print(f'{n} is even')
    else:
        print(f'{n} is not even')
        
def days_of_month():
    n = int(input('Input a month: '))
    res = 0
    if n <= 7:
        for i in range(7):
            if n%2==0:
                res = 30
            else:
                res = 31
    else:
        for i in range(8, 13):
            if n%2==1:
                res = 30                 
            else:
                res = 31
    print(f'This month has {res} days')
    
