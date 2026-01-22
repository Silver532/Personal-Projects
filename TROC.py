def offset(mapsize, size):
    rectval = int(size/(mapsize/10))
    distortion = (size/(mapsize/10))
    try:
        if float(rectval) == (distortion):
            return True
        else:
            return False
    except:
        return False

def getsizes(size):
    i = 0
    fitting = 0
    listing = []
    while i < 1000:
        i += 1
        tf = offset(i, size)
        if tf == True:
            fitting += 1
            listing.append(i)
        elif tf == False:
            pass
        else:
            print("Error")
    return listing

print(offset(25*25,1000))
print(getsizes(1000))