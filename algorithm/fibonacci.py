
def fibonacci(n):
    x = 0
    y = 1
    arr = []
    i = 1
    while i < n:
        z = x+y
        x = y
        y = z
        arr.append(z)
        i += 1
    print(arr)
        
def fib(n):
    if n == 1 or n == 2: 
        res = 1
    else:
        res = fib(n-1) + fib(n-2)
    return res

print(fib(15))
fibonacci(15)