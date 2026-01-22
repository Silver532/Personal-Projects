"""
Do Next:
    Finish creating item class
    Finish setting up creation of loot tables
    Item Types, used in item creation to determine stats

Need to Do:
    Implement Monsters
    Implement Shops
    Cant Loot or leave rooms when monsters are in without taking damage
    More Room Types, maybe in seperate document?
"""

from random import randint as rand
from time import sleep
import os

#initialization
if True:
    directiondict = {"North": 1, "East": 2, "South": 3, "West": 4, "Dungeon Exit": 5}
    roomtypes = {"Hall":"Long Hallway", "Lbry":"Library", "Brks": "Barracks", "Crwd": "Crowded Room",
                "Empt": "Empty Room", "Lrge": "Large Room", "Ovhw": "Overgrown Hallway", "Ovrm": "Overgrown Room",
                "Flhw": "Flooded Hallway", "Flrm": "Flooded Room"}

class Room:
    def __init__(self, name, description, exits, monsters, loot = True):
        self.name = name
        self.description = description
        self.exits = exits
        self.loot = loot
        self.monsters = monsters
    
    def describe(self):
        exits = ""
        for i in range(len(self.exits)): exits += f"{self.exits[i]}, " if i <= (len(self.exits)-2) else  f"and {self.exits[i]}"
        print(f"[{self.name}] You are in a {self.description}. There are {len(self.exits)} exits: {exits}")
        print(f"There {"is a monster" if self.monsters == 1 else "are no monsters" if self.monsters == 0 else f"are {self.monsters} monsters"} in the room.")
        print(f"This room has been looted." if (self.loot == False) else f"This room has not been looted.")

    def lootRoom(self, level, lootingplayer):
        if self.loot == False:
            print("No Loot")
            return
            #No Loot
        if self.monsters >= 1:
            print("Cant Loot When Monster is Alive")
            return
            #Cant Loot While Monster is Alive
        lootlist = createRoomloot(level)
        self.loot = False
        addLootToPlayer(lootlist, lootingplayer)

class Player:
    def __init__(self, name, money = 0, health = 100, maxhealth = 100, inventory = None, weapon = None, location = None):
        self.name = name
        self.money = money
        self.health = health
        self.maxhealth = maxhealth
        self.inventory = inventory if inventory is not None else []
        self.weapon = weapon
        self.location = location

    def addmoney(self, amount):
        self.money += int(amount)
        print(f"Collected {amount}g! {self.name} now has {self.money}g.")

    def spendmoney(self, amount):
        if self.money >= amount: self.money -= amount
        print(f"Spent {amount}g! {self.name} now has {self.money}g")

    def losehealth(self, amount):
        self.health = max(self.health - amount, 0)
        print(f"{self.name} took {amount} damage! {self.name} is now at {self.health} hp.")
    
    def gainhealth(self, amount):
        self.health = min(self.health + amount, self.maxhealth)
        print(f"{self.name} healed {amount} hp! {self.name} is now at {self.health} hp.")
    
    def losemaxhealth(self, amount):
        self.maxhealth = max(self.maxhealth - amount, 1); self.health = min(self.health, self.maxhealth)
        print(f"{self.name} took {amount} permanent damage! {self.name} now has {self.maxhealth} max hp.\n{self.name} has {self.health} hp left.")

    def gainmaxhealth(self, amount):
        self.maxhealth += amount; self.health = self.maxhealth
        print(f"{self.name} increased their max hp by {amount}! {self.name} now has {self.maxhealth} max hp.\n{self.name} has healed to full.")

    def pickupitem(self, item, count=1):
        for _ in range(count): self.inventory.append(item)
        if count == 1: print(f"{self.name} has collected {item.name}!")
        else: print(f"{self.name} has picked up {count} {item.name}s!")

    def dropitem(self, item):
        if item in self.inventory: self.inventory.remove(item); print(f"{self.name} has dropped {item.name}.")
        else: print(f"{self.name} does not have {item.name} in their inventory.")

    def playermove(self, direction, exits):
        movedirection = {"North": 1, "East": 2, "South": 3, "West": 4}
        mvdr = {"North":(-1,0), "East":(0,1), "South":(1,0), "West":(0,-1)}
        if direction in list(movedirection.keys()):
            if direction in list(exits):
                self.location = tuple(x + y for x, y in zip(self.location, mvdr[direction]))
            else: print("You cannot move in this direction.")
            input("")
        elif (0 <= int(direction) <= 4):
            reversedict = {v:k for k,v in movedirection.items()}
            numtodir = reversedict[int(direction)]
            if numtodir in list(exits):
                self.location = tuple(x + y for x, y in zip(self.location, mvdr[numtodir]))
            else: print("You cannot move in this direction.")
            input("")
        else:
            print("You cannot move in this direction.")
            input("")

    def looting(self, level, room):
        room.lootRoom(level, self)

    def describe(self):
        print(f"{self.name}:\nMoney: {self.money}\nHealth: {self.health}/{self.maxhealth}")

class Item:
    def __init__(self,name,description,type,onuse,damage = 1):
        #types of item: [standard, weapon, usable]
        self.name = name
        self.description = description
        self.damage = damage
        self.type = type
        self.onuse = onuse

    def describe(self):
        print(f"{self.name}\n{self.description}\n{self.damage}\n{self.type}\n{self.onuse}")

def generateDungeon(roomcount, level):
    mapsize = (roomcount//2)+1
    tilemap = []
    for i in range(mapsize):
        row = []
        for j in range(mapsize):
            row.append(0)
        tilemap.append(row)
    tilemap[len(tilemap)//2][len(tilemap)//2] = 1
    
    placedrooms = 0

    while placedrooms < roomcount:
        rand1, rand2 = rand(0,(mapsize)-1),rand(0,(mapsize)-1)
        if tilemap[rand1][rand2] == 0 and isNextTo(rand1,rand2,tilemap): tilemap[rand1][rand2] = 1; placedrooms += 1
            
    return tilemap, roomgen(tilemap, roomtypes, level)

def isNextTo(pos1, pos2, tilemap):
    rows = len(tilemap)
    cols = len(tilemap[0])
    if pos1 > 0 and tilemap[pos1 - 1][pos2] == 1:
        return True
    if pos1 < rows - 1 and tilemap[pos1 + 1][pos2] == 1:
        return True
    if pos2 > 0 and tilemap[pos1][pos2 - 1] == 1:
        return True
    if pos2 < cols - 1 and tilemap[pos1][pos2 + 1] == 1:
        return True
    return False

def roomgen(tilemap, roomtypes, level):
    rooms = {}
    for i in range(len(tilemap)):
        for j in range(len(tilemap[i])):
            if tilemap[i][j] == 1:
                coord = (i,j)
                rtype = list(roomtypes.keys())[rand(0,len(roomtypes)-1)]
                rooms[coord] = Room(rtype, roomtypes[rtype], connectrooms(coord, tilemap), monstercount(level, rtype), True)
    return rooms

def connectrooms(coord, tilemap):
    rows, cols, pos1, pos2 = len(tilemap), len(tilemap[0]), coord[0], coord[1]
    directionlist = []
    if pos1 > 0 and tilemap[pos1 - 1][pos2] == 1:
        directionlist.append("North")
    if pos1 < rows - 1 and tilemap[pos1 + 1][pos2] == 1:
        directionlist.append("South")
    if pos2 > 0 and tilemap[pos1][pos2 - 1] == 1:
        directionlist.append("East")
    if pos2 < cols - 1 and tilemap[pos1][pos2 + 1] == 1:
        directionlist.append("West")
    if pos1 == len(tilemap)//2 and pos2 == len(tilemap)//2:
        directionlist.append("Dungeon Exit")
    return directionlist

def monstercount(level, rtype):
    extramonster = (1 if (rtype == "Brks") or (rtype == "Crwd") else 0)
    return (int(level) // 10 + (1 if rand(0, 9) < int(level) % 10 else 0) + (1 if rand(0, 9) < 1 else 0)) + extramonster

def createRoomloot(level):
    #Money for money
    #Tuples, with (Item, Count) format
    #Return List
    return [(Item("Money", "Coins", "Money", None), 1)]

def addLootToPlayer(loot, player):
    for i in range(len(loot)):
        if loot[i][0].name != "Money":
            player.pickupitem(loot[i])
        else:
            player.addmoney(loot[i][1])

def clear():
    os.system('cls')

def sentencecase(word):
    lowerword = word.lower()
    return lowerword[0].upper() + lowerword[1:]

def startnewgame():
    clear()
    name = input("Input Player Name: ")
    pc = Player(name)
    sleep(1); clear()
    opencamp(pc)

def opencamp(pc):
    pc.describe(); sleep(1.5); clear()
    while True:
        clear()
        pc.location = None
        print("Village\n\nEnter Dungeon     Shop     Blacksmith     Tutorial\nStats")
        choice = input("What would you like to do?\n").lower()
        if "dungeon" in choice or choice == "1":
            enterdungeon(pc)
        elif "shop" in choice or choice == "2":
            pass
            #entershop()
        elif "blacksmith" in choice or choice == "3":
            pass
            #enterblacksmith()
        elif "stats" in choice or choice == "4":
            clear(); pc.describe(); input("")
        elif "exit" in choice or "done" in choice:
            endgame(); break
        else:
            entertutorial()

def entertutorial():
    clear()
    print("Use the input on terminal in order to control the game.\nIn many places, numbers are supported instead of words.\n")
    print("When you enter a Dungeon, you will have the option to see the dungeon specific controls")
    input("")

def enterdungeon(pc):
    clear()
    dnsc = (input("Small    Medium    Large    Extra Large\nInput Dungeon Size: ")).lower()
    if "small" in dnsc or dnsc == "1":
        dnsz = rand(6, 8)
    elif "extra" in dnsc or dnsc == "4":
        dnsz = rand(18, 20)
    elif "large" in dnsc or dnsc == "3":
        dnsz = rand(14, 16)
    else:
        dnsz = rand(10, 12)
    clear()
    lv = input("Easy    Medium    Hard    Extra Hard    Impossible\n\x1B[3mInput numbers for exact difficulty\x1B[0m\nInput Dungeon Level: ").lower()
    dnlv = rand(1,2) if "easy" in lv else rand(5,6) if "hard" in lv else rand(7,8) if "extra" in lv else rand(9,10) if "imp" in lv else lv if lv.isnumeric() else rand(3,4)
    clear()
    input(f"Dungeon Size: {dnsz}\nDungeon Level : {dnlv}\n")
    tilemap, rooms = generateDungeon(dnsz, dnlv)
    pc.location = (len(tilemap)//2,len(tilemap)//2)
    playdungeon(pc,tilemap,rooms,dnlv)

def playdungeon(pc, tilemap, rooms, level):
    while True:
        clear()
        rooms[pc.location].describe()
        action = input("").split()
        if action[0] == "go":
            pc.playermove(sentencecase(action[1]), rooms[pc.location].exits)
        elif action[0] == "fight":
            #fightenemy
            pass
        elif action[0] == "run":
            #runfromenemy
            pass
        elif action[0] == "loot":
            pc.looting(level, rooms[pc.location])
        elif action[0] == "map":
            for i in tilemap:print(i)
            print(pc.location)
            input("")
        elif action[0] == "exit":
            if "Dungeon Exit" in rooms[pc.location].exits:
                print("Exiting Dungeon")
                sleep(1)
                break

def endgame():
    #save to a file
    clear()

def main():
    while True:
        clear()
        print("Dungeon Crawl: A Text Adventure")
        gameaction = input("New\nLoad\nExit\n\n")
        if gameaction.lower() == "new": startnewgame()
        elif gameaction.lower() == "load": pass
        elif gameaction.lower() == "exit": clear(); break
        else: print("")

if __name__ == "__main__":
    main()