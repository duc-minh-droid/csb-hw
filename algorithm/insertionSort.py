

def insertionSort(arr, reverse=False):
    if reverse == False:
        for i in range(1, len(arr)):
            j = i
            while arr[j-1] > arr[j] and j > 0:
                arr[j-1], arr[j] = arr[j], arr[j-1]
                j -= 1
    elif reverse == True:
        for i in range(1, len(arr)):
            j = i
            while arr[j-1] < arr[j] and j > 0:
                    arr[j-1], arr[j] = arr[j], arr[j-1]
                    j -= 1 
    return arr
            
arr = [3, 9, 2, 8, 6, 7, 1, 5, 4, 0]
print(insertionSort(arr, reverse=True))

