#Imports
import pygame
from random import randint as rand

#Initialization
try:
    #Adaptability Variables
    size = 50
    mapsize = 10

    #Empty Values !!DO NOT TOUCH!!
    global clicks
    clicks = 0
    minecount = 0

    #Rectangle Calculation !!DO NOT TOUCH!!
    rectval = int(size/(mapsize/10))

    #Empty Lists !!DO NOT TOUCH!!
    tilemap = []
    row = []
    squareclicked = []

    #Values !!DO NOT TOUCH!!
    running = True
    victory = False

    #Pygame Initialization !!DO NOT TOUCH!!
    pygame.init()
    pygame.display.set_caption('Minesweeper')
    screen = pygame.display.set_mode((size*10,size*10))
except:
    print("Error in Initialization")

#Creating Full Tilemap
for i in range(mapsize):
    for j in range(mapsize):
        row.append(0)
    tilemap.append(row)
    row = []

#Placing Mines
while minecount < mapsize:
    pos1 = rand(0,mapsize-1)
    pos2 = rand(0,mapsize-1)
    if tilemap[pos1][pos2] == 0:
        tilemap[pos1][pos2] = 1
        minecount += 1

#Function to Draw Tilemap on Screen
def drawmap():
    colourdict = {1:"white",0:"white",-1:"green",-2:"red",-3:"black"} 
    for i in range(len(tilemap)):
        for j in range(len(tilemap[i])):
            if tilemap[i][j] >= 2 and tilemap[i][j] <= 19:
                pygame.draw.rect(screen,(200-(24*(tilemap[i][j])),200-(24*(tilemap[i][j])),200-(24*(tilemap[i][j]))),(j*rectval,i*rectval,rectval,rectval))
            elif tilemap[i][j] >= 20:
                pygame.draw.rect(screen,(100,0,0),(j*rectval,i*rectval,rectval,rectval))
            else:
                pygame.draw.rect(screen,colourdict[tilemap[i][j]],(j*rectval,i*rectval,rectval,rectval))
            mouserect()

#Function to Highlight what Tile the Mouse is over
def mouserect():
    coords = pygame.mouse.get_pos()
    squareclicked = [(coords[0])//rectval,(coords[1])//rectval]
    pygame.draw.rect(screen,("black"),(squareclicked[0]*rectval,squareclicked[1]*rectval,rectval,rectval),1)

#Function to Process Clicks
def clicksquare(position):
    squareclicked = [(position[0])//rectval,(position[1])//rectval]
    global clicks
    if (tilemap[squareclicked[1]][squareclicked[0]]) == 1 and clicks == 0:
        tilemap[squareclicked[1]][squareclicked[0]] = 0
        pos1 = rand(0,mapsize-1)
        pos2 = rand(0,mapsize-1)
        if tilemap[pos1][pos2] == 0:
            tilemap[pos1][pos2] = 1
    elif (tilemap[squareclicked[1]][squareclicked[0]]) == 1:
        tilemap[squareclicked[1]][squareclicked[0]] = -3
        drawmap()
        pygame.display.flip()
        pygame.time.wait(500)
        for i in range(len(tilemap)):
            for j in range(len(tilemap[i])):
                tilemap[i][j] = -2
        print("You Lose!")
    if (tilemap[squareclicked[1]][squareclicked[0]]) == 0:
        clicks += 1
        reveal(squareclicked)

#Function to Reveal a Tile
def reveal(position):
    minecount = 0
    if position[0] == 0:
        if position[1] == 0:
            for i in range(1,3):
                for j in range(1,3):
                    if tilemap[position[1]-1+i][position[0]-1+j] == 1 or tilemap[position[1]-1+i][position[0]-1+j] == 21:
                        minecount += 1
        elif position[1] != 0:
            for i in range(3):
                for j in range(1,3):
                    try:
                        if tilemap[position[1]-1+i][position[0]-1+j] == 1 or tilemap[position[1]-1+i][position[0]-1+j] == 21:
                            minecount += 1
                    except:
                        pass
    elif position[1] == 0 and position[0] != 0:
        for i in range(1,3):
            for j in range(3):
                try:
                    if tilemap[position[1]-1+i][position[0]-1+j] == 1 or tilemap[position[1]-1+i][position[0]-1+j] == 21:
                        minecount += 1
                except:
                    pass
    else:
        for i in range(3):
            for j in range(3):
                try:
                    if tilemap[position[1]-1+i][position[0]-1+j] == 1 or tilemap[position[1]-1+i][position[0]-1+j] == 21:
                        minecount += 1
                except:
                    pass

    tilemap[position[1]][position[0]] = minecount+2
    #print(minecount+2)
    return(minecount)

#Function to Place a Flag
def flag(position):
    global clicks
    flagsquare = [(position[0])//rectval,(position[1])//rectval]
    if (tilemap[flagsquare[1]][flagsquare[0]]) < 20:
        tilemap[flagsquare[1]][flagsquare[0]] += 20
        clicks += 1
    elif tilemap[flagsquare[1]][flagsquare[0]] >= 20:
        tilemap[flagsquare[1]][flagsquare[0]] -= 20
        clicks -= 1

#Pygame Running Processor
while running:
    if victory == False:
        drawmap()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            if event.button == 1:
                clicksquare(mouse)
                if clicks == (mapsize**2):
                    drawmap()
                    pygame.display.flip()
                    pygame.time.wait(500)
                    for i in range(len(tilemap)):
                        for j in range(len(tilemap[i])):
                            tilemap[i][j] = -1
                    print("You Win!")
            elif event.button == 3:
                flag(mouse)
            elif event.button == 2:
                print([(mouse[0])//rectval,(mouse[1])//rectval])
    pygame.display.flip()
    pygame.event.pump()