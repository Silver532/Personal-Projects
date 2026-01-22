import random
import time

#Defining Variables and Getting our Random Numbers
guessnum = random.randint(1,100)
answer = 0
triesleft = 10

#Print Opening Message
print("Welcome to the Guessing Game!")
while answer ==0:
    if(triesleft ==0):
        answer=2
        break
    pguess = int(input("What would you like to guess?\n"))
    if(pguess > guessnum):
        time.sleep(1)
        print("Try guessing Lower!")
        triesleft -=1
    elif(pguess < guessnum):
        time.sleep(1)
        print("Try guessing Higher!")
        triesleft-=1
    elif(pguess == guessnum):
        time.sleep(1)
        print("You Got It!")
        answer = 1
        break
if(answer==1):
    print("Congradulations!")
    time.sleep(1)
    print("You had "+str(triesleft)+" Tries Left")
elif(answer==2):
    print("You ran out of Tries")
print("The End")