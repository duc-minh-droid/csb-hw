from re import sub


arr = [4, 13, 8, 17, 29, 11]


def find_min_by_index(arr, n):
    sub_array = arr[n:]
    min = 0
    for i, idx in enumerate(sub_array):
        i2 = i + 1
        if idx+1 == len(sub_array):
            break
        if i < i2:
            i = min
    return min


def selection_sort(arr):
    
    return


print(find_min_by_index(arr, 1))
