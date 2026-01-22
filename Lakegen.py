import pygame
from random import randint as rand

waterchance = 2

pygame.init()
screen = pygame.display.set_mode((800,800))
running = True

tilemap = []
row = []
for y in range(100):
    for x in range(100):
        tilestate = rand(0,10000)
        if tilestate <= waterchance:
            row.append(0)
        elif tilestate > waterchance:
            row.append(1)
    tilemap.append(row)
    row = []
def spreadwater(spreadcount):
    for i in range(spreadcount):
        for i in range(len(tilemap)):
            for j in range(len(tilemap[i])):
                if tilemap[i][j] == 0:
                    if rand(1,100) == 1 and i-1 > -1:
                        tilemap[i-1][j] = 0
                    if rand(1,100) == 1 and i+1 < 100:
                        tilemap[i+1][j] = 0
                    if rand(1,100) == 1 and j-1 > -1:
                        tilemap[i][j-1] = 0
                    if rand(1,100) == 1 and j+1 < 100:
                        tilemap[i][j+1] = 0
spreadwater(800)
def drawmap():
    for i in range(len(tilemap)):
        for j in range(len(tilemap[i])):
            if tilemap[i][j] == 1:
                pygame.draw.rect(screen,(0,rand(217,223),0),(j*8,i*8,8,8))
            elif tilemap[i][j] == 0:
                pygame.draw.rect(screen,(0,rand(125,131),255),(j*8,i*8,8,8))
drawmap()
keys = pygame.key.get_pressed()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if keys[pygame.K_w]:
            screen.fill("White")
    pygame.display.flip()
pygame.quit()