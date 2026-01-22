def cipherhandling(textinput,cList):
    from functools import reduce; return reduce(lambda _, cipher: eval(f"{cipher}Decipher(_)"), cList, textinput)

def caesarDecipher(textinput):
    message, plaintext, shiftnum = "", textinput, int(input("CAESAR\nInput original shiftnum: ")) % 26
    for i in range(len(plaintext)): message += chr(overflow(ord(plaintext[i]) - shiftnum * (capshandling(plaintext[i]) != -1), capshandling(plaintext[i]), plaintext[i]))
    return message

def atbashDecipher(textinput):
    message = "".join(chr(155 - ord(c) + caps*2) if (caps := capshandling(c)) != -1 else c for c in str(textinput))
    return message

def runningDecipher(textinput):
    message, plaintext, key = "", str(textinput), str(input("RUNNING\nInput Key: "))
    while len(key) < len(plaintext): key += key
    for i in range(len(plaintext)):
        caps = capshandling(plaintext[i]); finalnum = ord(plaintext[i]) - (ord(key[i])+caps) + (65+caps) if caps != -1 else ord(plaintext[i]); message += chr(overflow(finalnum, caps, plaintext[i]))
    return message

def baconianDecipher(textinput):
    for old, new in {"f":"aaaaaa","F":"AAAAAA","e":"aaaaa","E":"AAAAA","d":"aaaa","D":"AAAA","c":"aaa","C":"AAA","b":"aa","B":"AA","a":"0","A":"1"}.items(): textinput = textinput.replace(old, new)
    message = "".join(chr(int(textinput[i:i+8], 2)) for i in range(0, len(textinput), 8))
    return message

def transpositionDecipher(textinput):
    plaintext, shiftnum = str(textinput), int(input("TRANSPOSITION\nInput original shiftnum: ")) % len(textinput); message = plaintext[-shiftnum:] + plaintext[:-shiftnum]
    return message

def staticDecipher(textinput):
    message, x, y = "", textinput[::2], textinput[1::2]
    for i in range(len(x)): caps = capshandling(x[i]); message += chr(overflow(ord(x[i])-ord(y[i]), caps, x[i])) if caps != -1 else x[i]
    return message

def affineDecipher(textinput):
    from math import gcd; message, ciphertext, mult, add = "", textinput, int(input("AFFINE\nInput Multiplicative: ")), int(input("AFFINE\nInput Additive: ")) % 26; mult_inv = pow((mult * (gcd(mult, 26) == 1) or 5), -1, 26)
    for i in range(len(ciphertext)): message += (lambda c, caps: chr(overflow((ord(c) - (65 + caps) - add) * mult_inv + 65 + caps, caps, c)) if caps != -1 else c)(ciphertext[i], capshandling(ciphertext[i]))
    return message

def divisorDecipher(textinput):
    message, sList, divisor = "", textinput.split(), int(input("DIVISOR\nInput Divisor: "))
    for item in sList: message += (chr(ord(item[2]) + ((ord(item[1])-65)*divisor)-1 + (32 if (ord(item[0])-65)//13 == 0 else 0))) if item != "AAA" and item.isalpha() else " " if item.isalpha() else item[0]
    return message

def switchDecipher(textinput):
    message, plaintext = "", str(textinput)
    for i in range(len(plaintext)): message += plaintext[i].lower() if plaintext[i].isupper() else plaintext[i].upper() if plaintext[i].islower() else plaintext[i]
    return message

def reverseDecipher(textinput):
    message, plaintext = "", str(textinput)
    for i in range(len(plaintext)): message += plaintext[len(plaintext)-(i+1)]
    return message

def railDecipher(textinput):
    rails=int(input("RAIL\nInput Rails: ")); plaintext=['']*len(textinput); order=sorted(range(len(textinput)),key=lambda x:(x%(2*rails-2) if x%(2*rails-2)<rails else 2*rails-2-x%(2*rails-2)))
    for position,value in zip(order,textinput):plaintext[position]=value
    return''.join(plaintext)

def vowelDecipher(textinput):
    message, plaintext, vowels= "", textinput, "AEIOU"
    for char in plaintext: caps = capshandling(char); message += char if char.upper() not in vowels else chr(ord(vowels[(vowels.index(char.upper())-1)%5])+caps)
    return message

def main():
    cipherdict, cipherlist, text = {"caesar":0,"atbash":1,"running":2,"baconian":3,"transposition":4,"static":5,"affine":6,"divisor":7,"reverse":8,"switch":9,"rail":10,"vowel":11},[],input("Input encrypted text:\n")
    print("Ciphers:",", ".join(cipherdict).upper()+"\nUse : for preset")
    while (cipher := input("Input Cipher (Done to finish)\n").lower()) != "done": (cipherlist.append(cipher) if cipher[0] != ":" and cipher in cipherdict else (cipherlist := preset(cipher[1:], cipherdict)) if cipher[0] == ":" else None)
    cipherlist.reverse(); print(f"{''.join(chr(913 + cipherdict[item]+(1 if cipherdict[item] >= 17 else 0)) for item in cipherlist)}: {cipherhandling(text, cipherlist)}")

if True:
    from cipherBackend import preset, overflow, capshandling; exec("main()") if __name__ == "__main__" else exec("print(\"Cipher Decryption\")")