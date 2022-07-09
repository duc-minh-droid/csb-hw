arr = [3, 12, 43, 93, 1, 27, 36, 78]

def my_sort(arr):
    for index in range(len(arr)):
        i2 = index+1
        if i2 >= len(arr):
            break
        if arr[i2] < arr[index]:
            arr[index] = arr[i2]
            arr[i2] = arr[index]
    print(arr)

my_sort(arr)