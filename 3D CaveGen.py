import pygame
from random import randint as rand

#Variables
wallchance = 70
size = 50
mapsize = 20

#Rectangle Calculation
rectval = int(size/(mapsize/10))

#Empty Lists for Map Generation
tilemap = []
row = []
column = []

for z in range(mapsize):
    for y in range(mapsize):
        for x in range(mapsize):
            row.append(0)
        column.append(row)
        row = []
    tilemap.append(column)
    column = []

for i in range(int(((mapsize**3)/100)*wallchance)):
    tilemap[rand(1,mapsize-2)][rand(1,mapsize-2)][rand(1,mapsize-2)] = 1

def drawmap(layer):
    for i in range(len(tilemap)):
        for j in range(len(tilemap[i])):
            if i == 0 or i == mapsize - 1:
                tilemap[i][j][layer] = 2
            if j == 0 or j == mapsize - 1:
                tilemap[i][j][layer] = 2
            if layer == 0 or layer == mapsize - 1:
                tilemap[i][j][layer] = 2
            
            if tilemap[i][j][layer] == 1:
                if layer > 2:
                    if tilemap[i][j][layer-1] != 1:
                        pygame.draw.rect(screen,("black"),(j*rectval,i*rectval,rectval,rectval),1)
                    else:
                        pygame.draw.rect(screen,(201,252,255),(j*rectval,i*rectval,rectval,rectval))
                        pygame.draw.rect(screen,("black"),(j*rectval,i*rectval,rectval,rectval),1)
                elif layer < 2:
                    pygame.draw.rect(screen,(0,0,255),(j*rectval,i*rectval,rectval,rectval))
                    pygame.draw.rect(screen,("black"),(j*rectval,i*rectval,rectval,rectval),1)
                elif layer == 2:
                    if tilemap[i][j][layer-1] != 1:
                        pygame.draw.rect(screen,("black"),(j*rectval,i*rectval,rectval,rectval),1)
                    else:
                        pygame.draw.rect(screen,(0,0,255),(j*rectval,i*rectval,rectval,rectval))
                        pygame.draw.rect(screen,("black"),(j*rectval,i*rectval,rectval,rectval),1)
            elif tilemap[i][j][layer] == 0:
                pygame.draw.rect(screen,("black"),(j*rectval,i*rectval,rectval,rectval))
            elif tilemap[i][j][layer] == 2:
                pygame.draw.rect(screen,(100,0,0),(j*rectval,i*rectval,rectval,rectval))

def fixwalls(count):
    for c in range(count):
        for h in range(len(tilemap)-1):
            for i in range(len(tilemap[h])-1):
                for j in range(len(tilemap[i])-1):
                    cellauto = 0

                    if h == 0:
                        tilemap[h][i][j] = 2

                    if tilemap[h-1][i-1][j-1] >= 1:
                        cellauto += 1
                    if tilemap[h-1][i-1][j] >= 1:
                        cellauto += 1
                    if tilemap[h-1][i-1][j+1] >= 1:
                        cellauto += 1
                    if tilemap[h-1][i][j-1] >= 1:
                        cellauto += 1
                    if tilemap[h-1][i][j] >= 1:
                        cellauto += 1
                    if tilemap[h-1][i][j+1] >= 1:
                        cellauto += 1
                    if tilemap[h-1][i+1][j-1] >= 1:
                        cellauto += 1
                    if tilemap[h-1][i+1][j] >= 1:
                        cellauto += 1
                    if tilemap[h-1][i+1][j+1] >= 1:
                        cellauto += 1

                    if tilemap[h][i-1][j-1] >= 1:
                        cellauto += 1
                    if tilemap[h][i-1][j] >= 1:
                        cellauto += 1
                    if tilemap[h][i-1][j+1] >= 1:
                        cellauto += 1
                    if tilemap[h][i][j-1] >= 1:
                        cellauto += 1
                    if tilemap[h][i][j+1] >= 1:
                        cellauto += 1
                    if tilemap[h][i+1][j-1] >= 1:
                        cellauto += 1
                    if tilemap[h][i+1][j] >= 1:
                        cellauto += 1
                    if tilemap[h][i+1][j+1] >= 1:
                        cellauto += 1
                    
                    if tilemap[h+1][i-1][j-1] >= 1:
                        cellauto += 1
                    if tilemap[h+1][i-1][j] >= 1:
                        cellauto += 1
                    if tilemap[h+1][i-1][j+1] >= 1:
                        cellauto += 1
                    if tilemap[h+1][i][j-1] >= 1:
                        cellauto += 1
                    if tilemap[h+1][i][j] >= 1:
                        cellauto += 1
                    if tilemap[h+1][i][j+1] >= 1:
                        cellauto += 1
                    if tilemap[h+1][i+1][j-1] >= 1:
                        cellauto += 1
                    if tilemap[h+1][i+1][j] >= 1:
                        cellauto += 1
                    if tilemap[h+1][i+1][j+1] >= 1:
                        cellauto += 1

                    if cellauto >= 13:
                        tilemap[h][i][j] = 1
                    elif cellauto < 12:
                        tilemap[h][i][j] = 0
viewlayer = (2)

pygame.init()
screen = pygame.display.set_mode((size*10,size*10))
running = True

fixwalls(5)

clock = pygame.time.Clock()
while running:
    clock.tick(60)
    screen.fill((255,255,255))
    drawmap(viewlayer)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                if viewlayer > 0:
                    viewlayer -= 1
            if event.key == pygame.K_UP:
                if viewlayer < mapsize-1:
                    viewlayer += 1
    pygame.display.flip()
    pygame.event.pump()
pygame.quit()