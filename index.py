from numpy.random import *

    
def sum(arr):
    sum = 0
    i = len(arr)-1
    while i >= 0:
        sum += arr[i]
        i -= 1
    return sum

def max(arr):
    max = arr[0]
    for i in arr:
        if i >= max:
            max = i
    return max

def randomList(len):
    rdn_list = []
    for i in range(len):
        rdn = randint(0, 100)
        rdn_list.append(rdn)
    return rdn_list

num = randomList(10)

def sort(arr):
    for i in range(len(arr)):
            j = i
            while arr[j-1] > arr[j] and j > 0:
                arr[j-1], arr[j] = arr[j], arr[j-1]
                j -= 1
    return arr

print(sort(num))
        
    