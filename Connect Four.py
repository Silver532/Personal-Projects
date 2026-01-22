from random import randint as rand
import pygame

size = 50
mapsize = 8

tilemap = []
row = []

rectval = int(size/(mapsize/10))

running = True
victory = False

global playerturn
playerturn = 1

global points
points = []

pygame.display.set_caption('Connect Four')
screen = pygame.display.set_mode((rectval*mapsize,rectval*mapsize))

for i in range(mapsize):
    for j in range(mapsize):
        row.append(0)
    tilemap.append(row)
    row = []

def drawmap():
    for i in range(len(tilemap)):
            for j in range(len(tilemap[i])):
                if tilemap[i][j] == 0:
                    pygame.draw.rect(screen,("white"),(j*rectval,i*rectval,rectval,rectval))
                if tilemap[i][j] == 1:
                    pygame.draw.rect(screen,("blue"),(j*rectval,i*rectval,rectval,rectval))
                if tilemap[i][j] == 2:
                    pygame.draw.rect(screen,("red"),(j*rectval,i*rectval,rectval,rectval))
                if tilemap[i][j] == 3:
                    pygame.draw.rect(screen,("blue"),(j*rectval,i*rectval,rectval,rectval))
                if tilemap[i][j] == 4:
                    pygame.draw.rect(screen,("red"),(j*rectval,i*rectval,rectval,rectval))
                pygame.draw.rect(screen,("black"),(j*rectval,i*rectval,rectval,rectval),1)

def clicksquare(position):
    global playerturn
    for i in range(mapsize):
        if i < mapsize-1:
            if tilemap[i+1][position] != 0:
                tilemap[i][position] = playerturn
                break
        elif i == mapsize-1:
            tilemap[i][position] = playerturn
            break
    if checkvictory([i,position]) != 3:
        if playerturn == 1:
            playerturn = 2
        elif playerturn == 2:
            playerturn = 1
    else:
        for i in range(len(tilemap)):
            for j in range(len(tilemap[i])):
                tilemap[i][j] = playerturn + 2

def checkvictory(position):
    global points
    points = 0
    #Horizontal
    horizontalpoints = 0
    for i in range(1,4):
        try:
            tilemap[position[1]+i]
        except:
            pass
        else:
            if tilemap[position[0]][position[1]+i] == playerturn:
                horizontalpoints += 1
            else:
                break
    for i in range(1,4):
        if position[1] != 0:
            if tilemap[position[0]][position[1]-i] == playerturn:
                horizontalpoints += 1
            else:
                break
        else:
            break
    #Vertical
    verticalpoints = 0
    for i in range(1,4):
        try:
            tilemap[position[0]+i]
        except:
            pass
        else:
            if tilemap[position[0]+i][position[1]] == playerturn:
                verticalpoints += 1
            else:
                break
    #Diagonal
    diagonalpoints = 0
    for i in range(1,4):
        try:
            tilemap[position[0]+i][position[1]+i]
        except:
            pass
        else:
            if tilemap[position[0]+i][position[1]+i] == playerturn:
                diagonalpoints += 1
            else:
                break
    for i in range(1,4):
        try:
            tilemap[position[0]-i][position[1]-i]
        except:
            pass
        else:
            if tilemap[position[0]-i][position[1]-i] == playerturn:
                diagonalpoints += 1
            else:
                break
    #Diagonal 2
    diagonalpoints2 = 0
    for i in range(1,4):
        try:
            tilemap[position[0]-i][position[1]+i]
        except:
            pass
        else:
            if tilemap[position[0]-i][position[1]+i] == playerturn:
                diagonalpoints2 += 1
            else:
                break
    for i in range(1,4):
        try:
            tilemap[position[0]+i][position[1]-i]
        except:
            pass
        else:
            if tilemap[position[0]+i][position[1]-i] == playerturn:
                diagonalpoints2 += 1
            else:
                break
    points = [horizontalpoints,verticalpoints,diagonalpoints,diagonalpoints2]
    for i in range(4):
        if points[i] == 3:
            return(points[i])

while running:
    drawmap()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            clicklocation = (mouse[0]//rectval)
            clicksquare(clicklocation)
    pygame.display.flip()
    pygame.event.pump()
pygame.quit()