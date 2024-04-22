from random import choice, randint
from identiconsGenerator import getImage

COUNT = 5

def getGrid():
    grid = []
    for _ in range(COUNT):
        row = []
        for _ in range(COUNT):
            row.append(choice([0,1]))

        for i in range(COUNT//2):
           row[COUNT-i-1] = row[i]

        grid.append(row)
    return grid

def randomAvatar(size:int):
    matrix = getGrid()
    color = (randint(0,255), randint(0,255), randint(0,255))
    return getImage(matrix,color,size)
    