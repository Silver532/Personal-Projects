def cipherhandling(textinput,cList):
    from functools import reduce; return reduce(lambda _, cipher: eval(f"{cipher}Cipher(_)"), cList, textinput)

def caesarCipher(textinput):
    message, plaintext, shiftnum = "", textinput, int(input("CAESAR\nInput number to shift: ")) % 26
    for i in range(len(plaintext)): message += chr(overflow(ord(plaintext[i]) + shiftnum * (capshandling(plaintext[i]) != -1), capshandling(plaintext[i]), plaintext[i]))
    return message

def atbashCipher(textinput):
    message = "".join(chr(155 - ord(c) + caps*2) if (caps := capshandling(c)) != -1 else c for c in textinput)
    return message

def runningCipher(textinput):
    message, plaintext, key = "", textinput, str(input("RUNNING\nInput Key: "))
    while len(key) < len(plaintext): key += key
    for i in range(len(plaintext)): caps=capshandling(plaintext[i]);finalnum=ord(plaintext[i])+(ord(key[i])+caps)-(65+caps) if caps!=-1 else ord(plaintext[i]);message+=chr(overflow(finalnum, caps, plaintext[i]))
    return message

def baconianCipher(textinput):
    message = "".join(f"{ord(c):08b}" for c in textinput)
    for old, new in {"0":"a","1":"A","aaaaaa":"f","AAAAAA":"F","aaaaa":"e","AAAAA":"E","aaaa":"d","AAAA":"D","aaa":"c","AAA":"C","aa":"b","AA":"B"}.items(): message = message.replace(old, new)
    return message

def transpositionCipher(textinput):
    plaintext, shiftnum = textinput, int(input("TRANSPOSITION\nInput number to shift: ")) % len(textinput); message = plaintext[shiftnum:] + plaintext[:shiftnum]
    return message

def staticCipher(textinput):
    from random import randint as rand; message, plaintext = "", textinput
    for i in range(len(plaintext)): caps = capshandling(plaintext[i]); r = rand(65,90) + (32 if rand(0,1) else 0); message += (chr(overflow(ord(plaintext[i])+r,caps,plaintext[i])) if caps != -1 else plaintext[i]) + chr(r)
    return message

def affineCipher(textinput):
    from math import gcd; message, plaintext, mult, add = "", textinput, int(input("AFFINE\nInput Multiplicative: ")), int(input("AFFINE\nInput Additive: ")) % 26
    for i in range(len(plaintext)): message += (lambda c, caps: chr(overflow((ord(c) - (65 + caps)) * (mult * (gcd(mult, 26) == 1) or 5) + add + 65 + caps, caps, c)) if caps != -1 else c)(plaintext[i], capshandling(plaintext[i]))
    return message

def divisorCipher(textinput):
    from random import randint as rand; message, plaintext, div = "", textinput, int(input("DIVISOR\nInput Divisor: "))
    for i in range(len(plaintext)):
        caps = capshandling(plaintext[i]); fNum = [(ord(plaintext[i])-(64+caps))//div,(ord(plaintext[i])-(64+caps))%div]
        message += "AAA " if plaintext[i] == " " else f"{chr(rand(65,77) if caps==32 else rand(78,90))}{chr(65+fNum[0])}{chr(65+fNum[1])} " if caps+1 else plaintext[i]+" "
    return message

def switchCipher(textinput):
    message, plaintext = "", textinput
    for i in range(len(plaintext)): message += plaintext[i].lower() if plaintext[i].isupper() else plaintext[i].upper()
    return message

def reverseCipher(textinput):
    message, plaintext = "", textinput
    for i in range(len(plaintext)): message += plaintext[len(plaintext)-(i+1)]
    return message

def railCipher(textinput):
    plaintext, idx, direction, railmatrix = textinput, 0, 1, [[] for _ in range(int(input("RAIL\nInput Rails: ")))]
    for char in plaintext: railmatrix[idx].append(char); idx += direction; direction *= -1 if idx in [0, len(railmatrix) - 1] else 1
    message = ''.join(char for rail in railmatrix for char in rail)
    return message

def vowelCipher(textinput):
    message, plaintext, vowels= "", textinput, "AEIOU"
    for char in plaintext: caps = capshandling(char); message += char if char.upper() not in vowels else chr(ord(vowels[(vowels.index(char.upper())+1)%5])+caps)
    return message

def standardMode(text, c_dict):
    c_list = []; print("Ciphers:",", ".join(c_dict).upper()+"\nUse : for preset")
    while (cipher := input("Input Cipher (Done to finish)\n").lower()) != "done": (c_list.append(cipher) if cipher[0] != ":" and cipher in c_dict else (c_list := preset(cipher[1:], c_dict)) if cipher[0] == ":" else None)
    return (f"{''.join(chr(913 + c_dict[item]+(c_dict[item] >= 17)) for item in c_list)}: {cipherhandling(text, c_list)}")

def randomMode(text, c_dict):
    from random import choice; c_list = [choice((" ".join(c_dict)).split()) for _ in range(int(input("Input Number of Ciphers:\n")))]
    return (f"{''.join(chr(913 + c_dict[item]+(c_dict[item] >= 17)) for item in c_list)}: {cipherhandling(text, c_list)}")

def optimalMode(text, c_dict):
    reversedict = {v: k for k, v in c_dict.items()}; c_list = [reversedict[item] for item in [0, 1, 6, 2, 9, 4, 10, 8, 5, 7, 3, 11]]
    return (f"{''.join(chr(913 + c_dict[item]+(c_dict[item] >= 17)) for item in c_list)}: {cipherhandling(text, c_list)}")

def testMode(text, c_dict):
    reversedict = {v: k for k, v in c_dict.items()}; c_list = [reversedict[i] for i in range(len(c_dict))]
    return (f"{''.join(chr(913 + c_dict[item]+(c_dict[item] >= 17)) for item in c_list)}: {cipherhandling(text, c_list)}")

def main():
    modelist = ["standard","random","optimal","test"]; print("Modes:",", ".join(modelist).upper()); mode, text = input("Input Mode: ").lower(), input("Input starting text:\n")
    c_dict = {"caesar":0,"atbash":1,"running":2,"baconian":3,"transposition":4,"static":5,"affine":6,"divisor":7,"reverse":8,"switch":9,"rail":10, "vowel":11}
    print(ftext := eval(f"{mode if mode in modelist else "standard"}Mode(text, c_dict)")); return ftext
    
if True:
    from cipherBackend import *; exec("ftext = main()") if __name__ == "__main__" else exec("print(\"Cipher Encryption\")")
    from pyperclip import copy as copy; exec("copy(ftext.split(\":\")[1])") if input("").lower() == "copy" else exec("print(\"\")")