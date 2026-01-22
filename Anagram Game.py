from random import randint as rand

anagramwords, wordlength, wordlist = open(r"wordlist.txt",'r'), int(input("Input Desired Word Length: ")), []

for i in (anagramwords.read().split()):
    if len(i) == wordlength: wordlist.append(i)

chosenword = wordlist[rand(0,len(wordlist))]
finallist = []
for i in chosenword: finallist.insert(rand(0,len(finallist)),i)
finalword = "".join(i for i in finallist)

print(finalword)

victory = -1

while 1:
    guess = input("Input Guess: ")
    if guess == chosenword: victory = 1 if victory != 0 else 0; break
    elif guess == "!exit": victory = 0; break
    elif guess == "!word": (print(finalword))
    elif guess == "!cheat": (print(chosenword)); victory = 0
    else: pass
print(("You Win!"*victory)+("You Lose!"*(-victory+1)))