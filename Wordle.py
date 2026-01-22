from random import randint as rand

wordlength, wordlewords, wordlist, counter, alphabet = int(input("Input Desired Length of Words: ")), open(r"Personal Projects\wordlist.txt",'r'), [], 10, []
for i in (wordlewords.read().split()):
    if len(i) == wordlength: wordlist.append(i)

chosenword = wordlist[rand(0,len(wordlist))]

print("_ "*wordlength)

for i in range(26): alphabet.append([chr(i+97),-1])
for counter in range(10):
    letterstates, responseword, prntab, vcount, victory = [], "", "", 0, 0
    for i in range(26): letterstates.append([0,chr(i+97)])
    while True:
        guess = input("Make Guess: ").lower()
        if len(guess) != wordlength: print("Please Input a word of proper length\n")
        else: break
    for i in range(len(guess)):
        if guess[i] in chosenword:
            if guess[i] != chosenword[i]: letterstates[ord(guess[i])-97][0] = 2; alphabet[ord(guess[i])-97][1] = 2
            else: letterstates[ord(guess[i])-97][0] = 1; alphabet[ord(guess[i])-97][1] = 1
        else: alphabet[ord(guess[i])-97][1] = 0
    for i in guess: responseword += f"\033[{str(41+letterstates[ord(i)-97][0])}m{i}\033[0m"
    for i in alphabet: prntab += f"\033[{str(41+i[1]) if i[1] != -1 else str(0)}m{i[0]}\033[0m"
    print(responseword,prntab)
    for i in guess:
        if alphabet[ord(i)-97][1] == 1: vcount += 1
    if vcount == wordlength: victory = 1; break
print(("You Win!"*victory)+("You Lose!"*(-victory+1)))