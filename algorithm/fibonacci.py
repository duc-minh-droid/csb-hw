
def fibonacci(n):
    x = 0
    y = 1
    while x < n:
        z = x+y
        x = y
        y = z
        print(z)

fibonacci(15)