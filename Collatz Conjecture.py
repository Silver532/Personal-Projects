from time import sleep; from random import randint as rand; number,count = rand(0,10**100),0
while True:
    sleep(0.01)
    if number%2 == 0: number = int(number/2)
    else: number *= 5; number += 1
    count += 1; print(number)
    if number == 1: print(f"{count} Iterations"); break