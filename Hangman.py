from random import randint as rand

hangmanwords = open(r"wordlist.txt",'r')
word = (hangmanwords.read().split())[rand(0,58108)]

letters = []
revealed = []
guessed = []

running = True

wrongcount = 0

for i in range(len(word)):
    letters.append(word[i])
    revealed.append(0)

def showletters():
    for i in range(len(letters)):
        if revealed[i] == 1:
            print(letters[i],end = " ")
        elif revealed[i] == 0:
            print("_",end = " ")

def guessedadd(letter):
    listContainsLetter = False
    for i in range(len(guessed)):
        if letter == guessed[i]:
            listContainsLetter = True
        else:
            pass
    if listContainsLetter == False:
        guessed.append(letter)

def guessletter(letter):
    wrong = 0
    for i in range(len(letters)):
        if letter == letters[i]:
            revealed[i] = 1
            wrong += 1
        else:
            pass
    guessedadd(letter)
    if wrong == 0:
        print("Wrong")
        return(int(1))
    else:
        return(int(0))

def showguessed(wrong):
    print("Guessed Letters: ", end = "")
    for i in range(len(guessed)):
        print(guessed[i], end = " ")
    print("  Tries Left: " + str(5-wrong))

def checkvictory():
    victory = 0
    for i in range(len(revealed)):
        if revealed[i] == 0:
            victory += 1
        elif revealed[i] == 1:
            pass
    if victory == 0:
        return(False)
    else:
        return(True)

while running:
    print("___________________")
    showletters()
    showguessed(wrongcount)
    wrongcount += guessletter((input("\nGuess a letter: ").lower())[0])
    running = checkvictory()
    if wrongcount == 5:
        running = False
    if not running and wrongcount < 5:
        showletters()
        print("\n___________________")
        print(f"You Win, the word was {word}")
    elif not running and wrongcount == 5:
        showletters()
        print("\n___________________")
        print(f"You Lose, the word was {word}")