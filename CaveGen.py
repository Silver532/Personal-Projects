import pygame
from random import randint as rand

#Values you can input for mapsize is 10, 20, 25, 40, 50, 100, 125

wallchance = 70
size = 100
mapsize = 20
rectval = int(size/(mapsize/10))

pygame.init()
screen = pygame.display.set_mode((size*10,size*10))
running = True

tilemap = []
row = []
for y in range(mapsize):
    for x in range(mapsize):
        row.append(0)
    tilemap.append(row)
    row = []

for i in range(int(((mapsize**2)/100)*wallchance)):
    tilemap[rand(1,mapsize-2)][rand(1,mapsize-2)] = 1

def fixwall(count):
    for i in range(count):
        for i in range(len(tilemap)-1):
            for j in range(len(tilemap[i])-1):
                cellauto = 0
                if i == 0 or i == mapsize - 1:
                    tilemap[i][j] = 2
                if j == 0 or j == mapsize - 1:
                    tilemap[i][j] = 2
                if tilemap[i-1][j-1] >= 1:
                    cellauto += 1
                if tilemap[i-1][j] >= 1:
                    cellauto += 1
                if tilemap[i-1][j+1] >= 1:
                    cellauto += 1
                if tilemap[i][j-1] >= 1:
                    cellauto += 1
                if tilemap[i][j+1] >= 1:
                    cellauto += 1
                if tilemap[i+1][j-1] >= 1:
                    cellauto += 1
                if tilemap[i+1][j] >= 1:
                    cellauto += 1
                if tilemap[i+1][j+1] >= 1:
                    cellauto += 1
                if cellauto > 5:
                    tilemap[i][j] = 1
                elif cellauto < 4:
                    tilemap[i][j] = 0
def drawmap():
    for i in range(len(tilemap)):
        for j in range(len(tilemap[i])):
            if i == 1 or i == mapsize - 2:
                tilemap[i][j] = 1
            if j == 1 or j == mapsize - 2:
                tilemap[i][j] = 1
            if i == 0 or i == mapsize - 1:
                tilemap[i][j] = 2
            if j == 0 or j == mapsize - 1:
                tilemap[i][j] = 2
            
            if tilemap[i][j] == 1:
                pygame.draw.rect(screen,("black"),(j*rectval,i*rectval,rectval,rectval))
            elif tilemap[i][j] == 0:
                pygame.draw.rect(screen,("white"),(j*rectval,i*rectval,rectval,rectval))
            elif tilemap[i][j] == 2:
                pygame.draw.rect(screen,(100,0,0),(j*rectval,i*rectval,rectval,rectval))

    """for i in range(mapsize):
                pygame.draw.rect(screen,("black"),(rectval, i*rectval, (mapsize*rectval)-2*rectval, 1))
    for i in range(mapsize):
                pygame.draw.rect(screen,("black"),(i*rectval, rectval, 1, (mapsize*rectval)-2*rectval))"""

drawmap()
fixwall(5)
drawmap()

keys = pygame.key.get_pressed()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
    pygame.event.pump()
pygame.quit()