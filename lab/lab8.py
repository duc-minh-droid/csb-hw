from datetime import datetime as dt 

def is_int(num):
    try:
        num = float(num)
        if num % 1 == 0:
            return True
        else:
            return False
    except:
        num = int(num)
        return True
        
def is_prime(num):
    isprime = True
    if num <= 1: isprime = False
    if num > 1:
        for i in range(2, num):
            if (num%i)==0:
                isprime = False
                break
    return isprime

def print_prime(n):
    res = []
    i = 0
    j = 0
    while j < n:
        if is_prime(i):
            res.append(i)
            j += 1
        i += 1
    return res

def bai4(num):
    def factorial(n):
        if n==1: return 1
        return n * factorial(n-1)
    sum = 0
    for i in range(1,num+1):
        x =float(factorial(i)/i)
        sum += x
    return int(sum)

def bai5():
    now = dt.now()
    today = now.strftime("%Y/%m/%d")
    time = now.strftime("%H:%M:%S")
    print(f"Today is {today}")
    print(f"Time right now: {time}")

bai5()

















