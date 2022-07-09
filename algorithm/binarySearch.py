arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num = 2
    
def binary_search(arr, num, min, max):
    guess = 0
    while max >= min:
        guess = guess + 1
        avr = round((min+max)/2)
        if arr[avr] == num:
            print('Total guesses: ', guess)
            return avr
        elif arr[avr] > num:
            max = avr - 1
        else:
            min = avr + 1
    return -1

max = len(arr) - 1
min = 0
# x = binary_search(arr, num, min, max)

def factorialCompare(n):
    res = 1
    for i in range(n):
        res = res * (i+1)
    if res == n*n:
        print('Equal!')
    if res > n*n:
        print('Big dif')
    else:
        print('smol')

