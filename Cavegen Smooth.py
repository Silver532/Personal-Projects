#imports
from random import randint as rand
import pygame
import TROC

#adaptability
if True:
    size = 100
    mapsize = 500
    startercaves = 4
    cellauto = 5

#initialization values
if True:
    """
    !!DO NOT TOUCH UNDER ANY CIRCUMSTANCES!!
    """
    #math
    spreadcount = ((mapsize)//startercaves)
    rectval = int(size/(mapsize/10))

    #dictionaries
    directiondict = {1:[0,-1],2:[-1,0],3:[0,1],4:[1,0]}
    colourdict = [{0:"black",1:"white"},{0:"white",1:"black"},{0:(0,220,0),1:(0,128,255)},{0:(0,128,255),1:(0,220,0)}]

    #pygame
    pygame.init()
    pygame.display.set_caption('Cave Generator v2')
    screen = pygame.display.set_mode((size*10,size*10))

    #display modification
    coloursetting = 0

    #empty lists
    tilemap = []
    row = []
    nearbytilemap = []
    nearbyrow = []

#tilemap generation
for i in range(mapsize):
    for j in range(mapsize):
        row.append(0)
    tilemap.append(row)
    row = []

#map drawing function
def drawmap():
    for i in range(len(tilemap)):
        for j in range(len(tilemap[i])):
            pygame.draw.rect(screen,(colourdict[coloursetting][tilemap[i][j]]),(i*rectval,j*rectval,rectval,rectval))

#parent function for caves
def spawncaves(cavecount):
    caves = 0
    while caves < cavecount:
        rand1, rand2 = rand(0,(mapsize)-1),rand(0,(mapsize)-1)
        if tilemap[rand1][rand2] == 0:
            caves += 1
            tilemap[rand1][rand2] = 1
    for i in range(spreadcount):
        spreadcaves()
    handlewalls(cellauto)

#initial cave spreading
def spreadcaves():
    for i in range(mapsize):
        for j in range(mapsize):
            if tilemap[i][j] == 1:
                direction = directiondict[rand(1,4)]
                try:
                    tilemap[i+direction[0]][j+direction[1]] = 1
                except:
                    pass

#parent function for counting and fixing walls
def handlewalls(count):
    for i in range(count):
        countwalls()
        fixwalls()

#counting walls around each tile
def countwalls():
    for g in range(mapsize):
        nearbyrow = []
        for h in range(mapsize):
            walls = 0
            if g == 0:
                if h == 0:
                    for i in range(1,3):
                        for j in range(1,3):
                            if tilemap[h-1+i][g-1+j] == 1:
                                walls += 1
                elif h != 0:
                    for i in range(3):
                        for j in range(1,3):
                            try:
                                if tilemap[h-1+i][g-1+j] == 1:
                                    walls += 1
                            except:
                                pass
            elif h == 0 and g != 0:
                for i in range(1,3):
                    for j in range(3):
                        try:
                            if tilemap[h-1+i][g-1+j] == 1:
                                walls += 1
                        except:
                            pass
            else:
                for i in range(3):
                    for j in range(3):
                        try:
                            if tilemap[h-1+i][g-1+j] == 1:
                                walls += 1
                        except:
                            pass
            nearbyrow.append(walls)
        nearbytilemap.append(nearbyrow)

#cellular automata to smooth out walls
def fixwalls():
    global nearbytilemap
    for i in range(len(tilemap)):
        for j in range(len(tilemap[i])):
            if nearbytilemap[i][j] > 5:
                tilemap[i][j] = 1
            elif nearbytilemap[i][j] <= 4:
                tilemap[i][j] = 0

#function to handle colour changing
def changecolour(key):
    global coloursetting
    if key == pygame.K_UP:
        if coloursetting < len(colourdict)-1:
            coloursetting += 1
        else:
            coloursetting = 0
    elif key == pygame.K_DOWN:
        if coloursetting >= 1:
            coloursetting -= 1
        else:
            coloursetting = len(colourdict)-1

#check for any offset due to rectangle calculations
def checkoffset():
    if TROC.offset(mapsize,size) == True:
        return True
    else:
        print(f"Compatible Mapsize values for your selected size:\n{TROC.getsizes(size)}")
        if input("Continue Y/N\n").upper() == "Y":
            return True
        else:
            return False

#while loop to handle game
def main():
    if checkoffset() == True:
        global coloursetting
        running = True
        spawncaves(startercaves)
        while running:
            drawmap()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    changecolour(event.key)
            pygame.display.flip()
            pygame.event.pump()
        pygame.quit()

#initializing main
if __name__ == "__main__" :
    main()