
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left_arr = arr[:mid]
        right_arr = arr[mid:]
        
        mergeSort(left_arr)
        mergeSort(right_arr)
        
        i = 0
        j = 0
        k = 0
        
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
            
        # print('current index', i, j, k)
        while i < len(left_arr):
            arr[k] = left_arr[i]
            print('i: ', i)
            i += 1
            k += 1
            
        while j < len(right_arr):
            arr[k] = right_arr[j]
            print('j: ', j)
            j += 1
            k += 1
            
arr = [2, 6, 5, 1, 7, 4, 3]
mergeSort(arr)
print(arr)










