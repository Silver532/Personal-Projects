if True:
    from random import randint as rand

    maxval = 99999
    runcount = 200

    average = 0
    meanList = []

def getplayernum(vRange):
    return (vRange[1] + vRange[0])//2

def getdirection(playernum):
    direction = -1 if playernum > compnum else 1 if playernum < compnum else 0
    #-1 for lower
    #1 for higher
    return direction

def fixrange(direction,playernum):
    valrange[0 if direction > 0 else 1] = playernum
    return valrange

def resolve(valrange):
    for i in range(2):
        if getdirection(valrange[i]) == 0:
            return valrange[i]

if True:
    for i in range(runcount):
        valrange = [1,maxval]
        compnum = rand(1,maxval)
        i = 0

        while True:
            i += 1
            #print(valrange)
            pNum = getplayernum(valrange)
            #print(pNum)
            pDirect = getdirection(pNum)
            valrange = fixrange(pDirect, pNum)
            if valrange[1] == valrange[0] or valrange[1] == valrange[0]+1 or pDirect == 0:
                pNum = resolve(valrange)
                print(f"Answer: {compnum}\n" + str(i) + " iterations\n")
                meanList.append(i)
                break

    print(f"{meanList}")
    for i in range(len(meanList)):
        average += meanList[i]
    average /= len(meanList)
    print(f"Average: {average}")