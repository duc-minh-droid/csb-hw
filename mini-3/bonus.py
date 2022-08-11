from getch import getch
from numpy import random
import os
import time 

def convertMap(array_2d):
    map = ''
    for i in range(len(array_2d)):
        for j in array_2d[i]:
            map += str(j) + ' '
        map += '\n'
    return map
    
def initMap(row, column):
    map = []
    for i in range(row):
        map.append(['_' for i in range(column)])
    return map

level = int(input('Choose a level (1 to 10): '))
row = 5 #6
column = 10 #12
wall_counts = 1 #4
trap_counts = 1
for i in range(1, level):
    row += 1
    column += 2
    wall_counts += 2
    trap_counts += 1
start_time = time.time()

map = initMap(row, column)
rowPos, columnPos = [0, 0]
map[rowPos][columnPos] = 'P'
maxRowPos = len(map) - 1
maxColumnPos = len(map[0]) - 1

doorRowPos, doorColumnPos = [random.randint(row), random.randint(column)]
map[doorRowPos][doorColumnPos] = 'D'

keyRowPos, keyColumnPos = [random.randint(row), random.randint(column)]
map[keyRowPos][keyColumnPos] = 'K'

list_trapPos = []
for i in range(trap_counts):
    trapRowPos, trapColumnPos = [random.randint(row), random.randint(column)]
    map[trapRowPos][trapColumnPos] = 'T'
    list_trapPos.append([trapRowPos, trapColumnPos])
print(list_trapPos)
list_wallPos = []
for i in range(wall_counts):
    wallRowPos, wallColumnPos = [random.randint(row), random.randint(column)]
    map[wallRowPos][wallColumnPos] = 'W'
    list_wallPos.append([wallRowPos, wallColumnPos])
    

hasKey = False
isWin = False
isLose = False
shouldBreak = False

while not isWin:
    os.system('clear')
    print(convertMap(map))
    prevRowPos, prevColumnPos = rowPos, columnPos
    map[rowPos][columnPos] = '_'
    key = getch()
    if key == 'w':
        rowPos -= 1
    elif key == 'a':
        columnPos -= 1
    elif key == 's':
        rowPos += 1
    elif key == 'd':
        columnPos += 1
    
    if rowPos > maxRowPos: rowPos = 0
    if rowPos < 0: rowPos = maxRowPos
    if columnPos > maxColumnPos: columnPos = 0
    if columnPos < 0: columnPos = maxColumnPos
    
    for i in range(len(list_trapPos)):
        if rowPos == list_trapPos[i][0] and columnPos == list_trapPos[i][1]:
            isLose = True
            map[rowPos][columnPos] = 'P'
            break
        
    if rowPos == keyRowPos and columnPos == keyColumnPos:
        hasKey = True
    for i in range(len(list_wallPos)):
        if (rowPos == list_wallPos[i][0] and columnPos == list_wallPos[i][1]):
            rowPos, columnPos = prevRowPos, prevColumnPos
    if (rowPos == doorRowPos and columnPos == doorColumnPos) and not hasKey:
        rowPos, columnPos = prevRowPos, prevColumnPos
    if (rowPos == doorRowPos and columnPos == doorColumnPos) and hasKey:
        isWin = True
        
    map[rowPos][columnPos] = 'P'

os.system('clear')
print(convertMap(map))

if (not isLose):
    print("Winner winner chicken dinner!")
else:
    print("Loser !!!")
print("finished in %s seconds " % (int(time.time() - start_time)))