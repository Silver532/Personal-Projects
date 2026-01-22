import pygame
from random import randint as rand

size = 50
mapsize = 10
rectval = int(size/(mapsize/10))

tilemap = []
row = []

snakeDirection = {1:[-1,0],2:[0,1],3:[1,0],4:[0,-1]}
snakeLength = 3
facing = 2
clock = pygame.time.Clock()

running = True

for i in range(mapsize):
    for j in range(mapsize):
        row.append(0)
    tilemap.append(row)
    row = []

snakepos = [4,4]

def drawmap():
    for i in range(len(tilemap)):
        for j in range(len(tilemap[i])):
            if tilemap[i][j] == 0:
                pygame.draw.rect(screen,("white"),(j*rectval,i*rectval,rectval,rectval))
            elif tilemap[i][j] == snakeLength:
                pygame.draw.rect(screen,(0,0,255),(j*rectval,i*rectval,rectval,rectval))
            elif tilemap[i][j] >= 1:
                pygame.draw.rect(screen,("black"),(j*rectval,i*rectval,rectval,rectval))
            elif tilemap[i][j] == -1:
                pygame.draw.rect(screen,("red"),(j*rectval,i*rectval,rectval,rectval))
            pygame.draw.rect(screen,("black"),(j*rectval,i*rectval,rectval,rectval),1)

def testchange(facing,number):
    if facing == 1:
        if number == 2 or number == 4:
            return True
        else:
            return False
    elif facing == 2:
        if number == 1 or number == 3:
            return True
        else:
            return False
    elif facing == 3:
        if number == 2 or number == 4:
            return True
        else:
            return False
    elif facing == 4:
        if number == 1 or number == 3:
            return True
        else:
            return False

def movesnake(direction,length):
    for i in range(len(tilemap)):
        for j in range(len(tilemap[i])):
            if tilemap[i][j] >= 1:
                tilemap[i][j] -= 1
    try:
        if tilemap[snakepos[0]+direction[0]][snakepos[1]+direction[1]] == 0:
            tilemap[snakepos[0]+direction[0]][snakepos[1]+direction[1]] = length
            snakepos[0] += direction[0]
            snakepos[1] += direction[1]
        elif tilemap[snakepos[0]+direction[0]][snakepos[1]+direction[1]] == -1:
            global snakeLength
            snakeLength += 1
            tilemap[snakepos[0]+direction[0]][snakepos[1]+direction[1]] = length
            snakepos[0] += direction[0]
            snakepos[1] += direction[1]
        elif tilemap[snakepos[0]+direction[0]][snakepos[1]+direction[1]] >= 1:
            global running
            running = False
    except:
        if facing == 2:
            tilemap[snakepos[0]+direction[0]][0] = length
            snakepos[0] += direction[0]
            snakepos[1] = 0
        elif facing == 3:
            tilemap[0][snakepos[1]+direction[1]] = length
            snakepos[0] = 0
            snakepos[1] += direction[1]

def apples():
    applecount = 0
    for i in range(len(tilemap)):
        for j in range(len(tilemap[i])):
            if tilemap[i][j] == -1:
                applecount += 1
    
    while applecount < 1:
        rand1 = rand(0,mapsize-1)
        rand2 = rand(0,mapsize-1)
        if tilemap[rand1][rand2] >= 1:
            pass
        else:
            tilemap[rand1][rand2] = -1
            applecount += 1
    

pygame.init()
pygame.display.set_caption('Snake')
screen = pygame.display.set_mode((size*10,size*10))


while running:
    clock.tick(8)
    drawmap()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if testchange(facing,1) == True:
                    facing = 1
            if event.key == pygame.K_RIGHT:
                if testchange(facing,2) == True:
                    facing = 2
            if event.key == pygame.K_DOWN:
                if testchange(facing,3) == True:
                    facing = 3
            if event.key == pygame.K_LEFT:
                if testchange(facing,4) == True:
                    facing = 4
    movesnake(snakeDirection[facing],snakeLength)
    apples()
    pygame.display.flip()
    pygame.event.pump()
pygame.quit()
print(f"Game Over\nYou ate {snakeLength-3} apple",end="")
if snakeLength-3 != 1:
    print("s")
    if snakeLength >= 28:
        print("Amazing Job!")
    elif snakeLength >= 13:
        print("Great Job!")
    elif snakeLength >= 8:
        print("Good Job!")
    elif snakeLength < 8:
        print("Skill Issue")