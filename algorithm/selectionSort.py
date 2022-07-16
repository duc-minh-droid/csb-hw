
def getmin(arr, n):
    sub = arr[n:]
    min = sub[0]
    min_idx = 0
    for idx, i in enumerate(sub):
        idx2 = idx + 1
        if idx2 >= len(sub):
            break
        if sub[idx] < sub[idx2]:
            if sub[idx] > min:
                continue
            min = sub[idx]
            min_idx = idx
        else:
            if sub[idx2] < min or sub[idx] < min:
                min = sub[idx2]
                min_idx = idx2
    return [min_idx, min]

def swap(arr, idx1, idx2):
    temp = arr[idx1]
    arr[idx1] = arr[idx2]
    arr[idx2] = temp
    return arr
    

def selection_sort(arr):
    for i in range(len(arr)):
        [min_idx, min] = getmin(arr, i)
        if i == 0:
            swap(arr, i, min_idx)
        if arr[i] > min:
            swap(arr, i, min_idx+i)
    return arr


arr = [0, 9, 1, 4, 13, 8, 1, 3, 17, 29, 0, 11, 2]
print(selection_sort(arr))