from contextlib import nullcontext


def bai1():
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    add2 = [x+2 for x in arr]
    mul2 = [x*2 for x in arr]
    sft2 = arr[2:] + arr[:2]
    
    print("Orignal list:", arr)
    print("Add 2:", add2)
    print("Multiply by 2:", mul2)
    print("Shift 2:", sft2)

def bai2():
    arr = ['l', 'o', 'o', 'h', 'c', 'S', ' ', 'y', 'g', 'o', 'l', 'o', 'n', 'h', 'c', 'e', 'T', ' ', 'X', 'd', 'n', 'i', 'M']
    i = len(arr)-1
    res = ""
    while i >= 0:
        res += arr[i]
        i -= 1
    print(res)
    
def bai3():
    n = int(input('Input a positive number: '))
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
    print(f'First {n} Fibonacci number(s): {arr}')
    
def bai4():
    arr = [('Ribeye Steak', 30.5), ('Potato Salad', 5), ('Sparkling Wine', 7), ('Smoked Salmon', 12), ('Chicken Soup', 8.5), ('Tiramisu Cake', 4.5)]
    print(f'Number of items: {len(arr)}\n')
    for i in range(len(arr)):
        print(f'Item {i}: {arr[i][0]}')
        print(f'Price of item {i}: {arr[i][1]}\n')
    # count average price
    avr_arr = map(lambda x: x[1], arr)
    avr = sum(avr_arr) / len(arr)
    print(f'Average price: {avr}')
    # get above average items
    above_avr = []
    for i in range(len(arr)):
        if arr[i][1] > avr:
            above_avr.append(arr[i])
    print(f'Item(s) above average price: {above_avr}')
    
def bai5():
    input_str = input('Write a sentence: ')
    word_list = input_str.split(' ')
    number_unique_words = len(list(dict.fromkeys(word_list)))     
    print(f'Number of unique words: {number_unique_words}')
    
bai5()