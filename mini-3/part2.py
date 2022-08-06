
def factorial(n):
    if n == 0: return 1
    return n * factorial(n-1)

def sortlist(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
        
def print_fibo(n):
    p = 1
    q = 1
    i = 2
    arr = [p,q]
    while i < n:
        fibo = p + q
        arr.append(fibo)
        p = q
        q = fibo
        i += 1 
    arr = ' '.join([str(x) for x in arr])
    print(arr)

