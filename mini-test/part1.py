arr = ['blue', 'green', 'yellow', 'orange']
print('Color list: ')

# bai 2
def getColorList(arr):
    str = ""
    for i in arr:
        if i == arr[-1]:
            str += i
        else:
            str += i + ', '
    return str
print(getColorList(arr))

# bai 3
color = input('Input a new color: ')

if color not in arr:
    arr.append(color)
print('New color list: ')
print(getColorList(arr))