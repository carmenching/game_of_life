# -*-coding: utf-8 -*-
def borderTopLeft(x, y, grid):
    liveNeighbours = 0
    if grid[x+1][y]:
        liveNeighbours += 1
    if grid[x+1][y-1]:
        liveNeighbours += 1
    if grid[x][y-1]: 
        liveNeighbours += 1

def borderLeft(x, y, grid):
    liveNeighbours = 0
    if grid[x][y+1]:
        liveNeighbours += 1
    if grid[x+1][y+1]:
        liveNeighbours += 1
    if grid[x+1][y]:
        liveNeighbours += 1
    if grid[x+1][y-1]:
        liveNeighbours += 1
    if grid[x][y-1]: 
        liveNeighbours += 1
    return liveNeighbours

def borderBottomLeft(x, y, grid):
    liveNeighbours = 0
    if grid[x][y+1]:
        liveNeighbours += 1
    if grid[x+1][y+1]:
        liveNeighbours += 1
    if grid[x+1][y]:
        liveNeighbours += 1
    return liveNeighbours

def borderBottom(x, y, grid):
    liveNeighbours = 0
    if grid[x][y-1]:
        liveNeighbours += 1
    if grid[x-1][y-1]:
        liveNeighbours += 1
    if grid[x-1][y]:
        liveNeighbours += 1
    if grid[x-1][y+1]:
        liveNeighbours += 1
    if grid[x][y+1]:
        liveNeighbours += 1
    return liveNeighbours

def borderBottomRight(x, y, grid):
    liveNeighbours = 0
    if grid[x-1][y]:
        liveNeighbours += 1
    if grid[x][y-1]:
        liveNeighbours += 1
    if grid[x-1][y-1]:
        liveNeighbours += 1
    return liveNeighbours

def borderRight(x, y, grid):
    liveNeighbours = 0
    if grid[x+1][y]:
        liveNeighbours += 1
    if grid[x+1][y-1]:
        liveNeighbours += 1
    if grid[x][y-1]: 
        liveNeighbours += 1
    if grid[x-1][y-1]:
        liveNeighbours += 1
    if grid[x-1][y]:
        liveNeighbours += 1
    return liveNeighbours

def borderTopRight(x, y, grid):
    liveNeighbours = 0
    if grid[x-1][y]: 
        liveNeighbours += 1
    if grid[x-1][y-1]:
        liveNeighbours += 1
    if grid[x][y-1]:
        liveNeighbours += 1
    return liveNeighbours

def borderTop(x, y, grid):
    liveNeighbours = 0
    if grid[x+1][y]:
        liveNeighbours += 1
    if grid[x+1][y-1]:
        liveNeighbours += 1
    if grid[x][y-1]: 
        liveNeighbours += 1
    if grid[x-1][y-1]:
        liveNeighbours += 1
    if grid[x-1][y]:
        liveNeighbours += 1
    return liveNeighbours

def noBorder(x,y,grid):
    liveNeighbours = 0
    if grid[x-1][y+1]:
        liveNeighbours += 1
    if grid[x][y+1]:
        liveNeighbours += 1
    if grid[x+1][y+1]:
        liveNeighbours += 1
    if grid[x+1][y]:
        liveNeighbours += 1
    if grid[x+1][y-1]:
        liveNeighbours += 1
    if grid[x][y-1]: 
        liveNeighbours += 1
    if grid[x-1][y-1]:
        liveNeighbours += 1
    if grid[x-1][y]:
        liveNeighbours += 1
    return liveNeighbours

def verifyNeighbour(x,y, grid):
    liveNeighbours = 0
    gridRow = len(grid)
    gridColumn = len(grid[0])

    if x==0 and y==0:
        liveNeighbours = borderTopLeft(x, y, grid)
    elif x==0:
        liveNeighbours = borderTop(x, y, grid)
    elif x==0 and y==gridColumn-1:
        liveNeighbours = borderTopRight(x, y, grid)
    elif y==gridColumn-1 and x!= gridRow-1:
        liveNeighbours = borderRight(x, y, grid)
    elif x==gridRow-1 and y==gridColumn-1:
        liveNeighbours = borderBottomRight(x, y, grid)
    elif x==gridRow-1 and y!=gridColumn-1:
        liveNeighbours = borderBottom(x, y, grid)
    elif x==gridRow-1 and y==0:
        liveNeighbours = borderBottomLeft(x, y, grid)
    elif y==0:
        liveNeighbours = borderLeft(x, y, grid)
    else :
        liveNeighbours = noBorder(x, y, grid)
    
    if liveNeighbours == 2 or liveNeighbours == 3 :
        return True
    else :
        return False

def nextCycle(currentState):
    nextState = [[False for x in range(len(currentState))] for y in range(len(currentState[0]))]
    for i in range (len(currentState)):
        for j in range (len(currentState[i])):
            # print("("+str(i) + ","+str(j)+"):")
            isAlive = verifyNeighbour(i, j, currentState)
            # print(isAlive)
            if isAlive:
                nextState[i][j] = True
    return nextState

def staticData():
    coordinates = [(1,2),(3,5),(3,3),(3,4)]
    return coordinates

def imprimeGrid(grid):
    for i in range (len(grid)):
        for j in range (len(grid[i])):
            if grid[i][j] :
                # print("from imprimeGrid : "+str(grid[i][j]))
                grid[i][j] = 'X|'
            else : 
                grid[i][j] = '_|'

            if j == len(grid[i])-1: 
                # row += str(grid[i][j]) + '|'
                # print(row)
                print(grid[i][j])
            else :
                # row += str(grid[i][j]) + '|'
                print(grid[i][j], end='')
        # print(row)

def createGrid(ligne, colonne):
    i = ligne
    j = colonne
    grid = [[False for x in range(i)] for y in range(j)]
    return grid

def insertGridWithBlocks(grid):
    blocks = staticData()
    for i in blocks:
        grid[i[0]][i[1]] = True
    return grid

def main():
    currentState = createGrid(6,6)
    currentState = insertGridWithBlocks(currentState)
    print("T1:")
    imprimeGrid(currentState)
    print("begin cycles")
    cycles = 20
    for i in range(cycles) : 
        nextState = nextCycle(currentState)
        imprimeGrid(nextState)
        currentState = nextState
        print("----------------------")

    

#cet embranchement conditionnel 
#permet de vérifier si le programme a été lancé en execution ou par importation 
if __name__ == '__main__':
    main()