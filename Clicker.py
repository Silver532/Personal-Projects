#imports
from random import randint as rand
import pygame

#required setup & empty values
if True:
    mapsize = 10
    size = 50

    rectval = int(size/(mapsize/10))
    screen = pygame.display.set_mode((size*10,size*10))
    clock = pygame.time.Clock()

    tilemap = []
    row = []

#tilemap generation
for i in range(mapsize):
    for j in range(mapsize):
        row.append(0)
    tilemap.append(row)
    row = []

#map drawing
def drawmap():
    for i in range(len(tilemap)):
        for j in range(len(tilemap[i])):
            if tilemap[i][j] == 0:
                pygame.draw.rect(screen,("white"),(i*rectval,j*rectval,rectval,rectval))
            elif tilemap[i][j] == 1:
                pygame.draw.rect(screen,("red"),(i*rectval,j*rectval,rectval,rectval))
            elif tilemap[i][j] > 1:
                pygame.draw.rect(screen,("orange"),(i*rectval,j*rectval,rectval,rectval))
    pygame.display.flip()

#handling square clicking
def clicksquare(location_x,location_y):
    success = 0
    failure = 0
    if tilemap[location_x][location_y] >= 1:
        success = 1
        failure = 0
    elif tilemap[location_x][location_y] == 0:
        success = 0
        failure = 1
    tilemap[location_x][location_y] = 0
    return success, failure

#update tilemap
def tick():
    clock.tick(20)
    failure = 0
    for i in range(len(tilemap)):
        for j in range(len(tilemap[i])):
            if tilemap[i][j] > 1:
                tilemap[i][j] -= 1
                failure += 0
            elif tilemap[i][j] == 1:
                tilemap[i][j] = 0
                failure += 1
    return failure

#count number of targets
def gettargets():
    targetcount = 0
    for i in range(mapsize):
        for j in range(mapsize):
            if tilemap[i][j] >= 1:
                targetcount += 1
    return targetcount

#spawn targets
def spawntarget():
    placed = False
    while placed == False:
        posx,posy = rand(0,mapsize-1),rand(0,mapsize-1)
        if tilemap[posx][posy] == 0:
            tilemap[posx][posy] = 100
            placed = True
        else:
            pass

#handle targets
def targets():
    count = gettargets()
    if count <= 1:
        spawntarget()

#game loop
def main():
    running = True
    points = 0
    tries = 10
    while running:
        tries -= tick()
        targets()
        drawmap()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                outcome = [0,0]
                mouse = pygame.mouse.get_pos()
                clicklocation_x = (mouse[0]//rectval)
                clicklocation_y = (mouse[1]//rectval)
                outcome = (clicksquare(clicklocation_x,clicklocation_y))
                points += outcome[0]
                tries -= outcome[1]
        if tries == 0:
            running = False
        pygame.event.pump()
    pygame.quit()
    print(points)

if __name__ == "__main__":
    main()