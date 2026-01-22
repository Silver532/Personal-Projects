from random import randint as rand

ciphertype = input("What type of cipher would you like to use?\n").lower().replace(" ","")
message = ""

if ciphertype == "runningkey" or ciphertype == "running":
    #Cipher will only encrypt plain text, non alphabetical characters will remain the same
    #Do NOT use non alphabetical characters as part of your key
    encrypt = input("Would you like to encrypt or decrypt a message?\n").lower()
    if encrypt == "encrypt":
        key = str(input("What is the key you are using?\n").upper())
        plaintext = str(input("\nWhat is the text you want to encrypt?\n").upper())
        while len(key) < len(plaintext):
            key = key + key
        for i in range(len(plaintext)):
            if ord(plaintext[i]) <=90 and ord(plaintext[i]) >=65:
                finalnum = ord(plaintext[i]) + ord(key[i])-65
                while finalnum >90:
                    finalnum -=26
                finaltext = chr(finalnum)
                message = message + finaltext
            else:
                finalnum = ord(plaintext[i])
                finaltext = chr(finalnum)
                message = message + finaltext
        print("Your Encrypted Message Is: " + str(message.lower()))
    elif encrypt == "decrypt":
        key = str(input("What is the key are you using?\n").upper())
        undotext = str(input("\nWhat is the text you want to decrypt?\n").upper())
        while len(key) < len(undotext):
            key = key + key
        for i in range(len(undotext)):
            if ord(undotext[i]) <= 90 and ord(undotext[i]) >= 65:
                finalnum = ord(undotext[i])-ord(key[i])+65
                while finalnum < 65:
                    finalnum += 26
                finaltext = chr(finalnum)
                message = message + finaltext
            else:
                finalnum = ord(undotext[i])
                finaltext = chr(finalnum)
                message = message + finaltext
        print("Your Decrypted Message Is: " + str(message.lower()))
    elif encrypt == "grabkey":
        plaintext = str(input("What is the starting text?\n").upper())
        endingtext = str(input("What is the encrypted text?\n").upper())
        for i in range(len(plaintext)):
            if ord(plaintext[i]) <= 90 and ord(plaintext[i]) >=65:
                keycode = ord(endingtext[i])-ord(plaintext[i])+65
                while keycode <65:
                    keycode += 26
                message = message + str(chr(keycode))
            else:
                keycode = "\\\\"
                message = message + str(keycode)
        print("The Key Is: " + str(message.lower()))
    elif encrypt == "key":
        for i in range(rand(10,15)):
            keypart = chr(rand(65,90))
            message = message + keypart
        print("Your Key Is: " + str(message.lower()))
    else:
        print("\033[3mPlease use one of the Available Tools\033[0m\nencrypt\ndecrypt\nkey\ngrabkey")

elif ciphertype == "caesar":
    #Cipher will only encrypt plain text, non alphabetical characters will remain the same
    #Do NOT use non numeric characters for the shift value
    encrypt = input("Would you like to encrypt or decrypt a message?\n").lower()
    if encrypt == "encrypt":
        plaintext = str(input("Please Input a string to encode\n").upper())
        shiftnum = int(input("\nPlease input the shift value\n"))
        for i in range(len(plaintext)):
            if ord(plaintext[i]) >= 65 and ord(plaintext[i])<= 90:
                modnum = ord(plaintext[i])
                modnum += shiftnum
                while modnum >90:
                    modnum -= 26
                message = message + chr(modnum)
            else:
                modnum = ord(plaintext[i])
                message = message + chr(modnum)
        print("\nYour Encrypted Message Is: "+ message.lower())
    elif encrypt == "decrypt":
        plaintext = str(input("Please Input the encrypted text\n").upper())
        shiftnum = -int(input("\nPlease input the shift value\n"))
        for i in range(len(plaintext)):
            if ord(plaintext[i]) >= 65 and ord(plaintext[i]) <= 90:
                modnum = ord(plaintext[i])
                modnum -= shiftnum
                while modnum <65:
                    modnum += 26
            else:
                modnum = ord(plaintext[i])
            message += chr(modnum)
        print("Your decrypted message is: " + message.lower())
    else:
        print("\033[3mPlease use one of the Available Tools\033[0m\nencrypt\ndecrypt")

elif ciphertype == "atbash":
    #Cipher will only encrypt plain text, non alphabetical characters will remain the same
    encrypt = input("Would you like to encypt or decrypt a message?\n").lower()
    if encrypt == "encrypt":
        plaintext = input("Input the string to encode\n").upper()
        for i in range(len(plaintext)):
            if ord(plaintext[i]) <= 90 and ord(plaintext[i]) >= 65:
                keypart = chr(90-(ord(plaintext[i])-65))
            else:
                keypart = plaintext[i]
            message += keypart
        print("Your Encrypted Message Is: " + str(message).lower())
    elif encrypt == "decrypt":
        plaintext = input("Input the string to decode\n").upper()
        for i in range(len(plaintext)):
            if ord(plaintext[i]) <= 90 and ord(plaintext[i]) >= 65:
                keypart = chr(90-(ord(plaintext[i])-65))
            else:
                keypart = plaintext[i]
            message += keypart
        print("Your Decrypted Message Is: " + str(message).lower())
    else:
        print("\033[3mPlease use one of the Available Tools\033[0m\nencrypt\ndecrypt")

elif ciphertype == "baconian":
    encrypt = input("Would you like to encrypt or decrypt a message?\n").lower()
    if encrypt == "encrypt":
        plaintext = input("Input the string to encode\n").upper()
        for i in range(len(plaintext)):
            keypart = bin(ord(plaintext[i]))[2:]
            while len(keypart) < 8:
                keypart = "0" + keypart
            message += keypart
        message = message.replace("0","a").replace("1","A").replace("aaaaaa","f").replace("AAAAAA","F").replace("aaaaa","e").replace("AAAAA","E").replace("aaaa","d").replace("AAAA","D").replace("aaa","c").replace("AAA","C").replace("aa","b").replace("AA","B")
        print("Your Encrypted Message Is: " + message)
    elif encrypt == "decrypt":
        plaintext = input("Input the string to decode\n")
        plaintext = plaintext.replace("f","aaaaaa").replace("F","AAAAAA").replace("e","aaaaa").replace("E","AAAAA").replace("d","aaaa").replace("D","AAAA").replace("c","aaa").replace("C","AAA").replace("b","aa").replace("B","AA").replace("a","0").replace("A","1")
        for i in range(int(len(plaintext)/8)):
            keypart = chr(int(str(plaintext[0 + 8*i:8+8*i]), 2))
            message += keypart
        print("Your Decrypted Message Is: " + message.lower())
    else:
        print("\033[3mPlease use one of the Available Tools\033[0m\nencrypt\ndecrypt")

elif ciphertype == "autokey":
    encrypt = input("Would you like to encrypt or decrypt a message?\n").lower()
    if encrypt == "encrypt":
        plaintext = input("What is the string you would like to encrypt?\n").replace(" ","").replace(",","").upper()
        startingkey = input("What is the starting key that you are using?\n").upper()
        for i in range(len(plaintext)):
            if i+1 <= len(startingkey):
                keypart = startingkey[i]
            else:
                keypart = plaintext[i-1]
            messagepart = ord(plaintext[i])+ord(keypart)-65
            if messagepart > 90:
                messagepart -= 26
            message += chr(messagepart)
        print("Your Encrypted Message Is: " + str(message))
    elif encrypt == "decrypt":
        plaintext = input("What is the string you would like to decrypt?\n").upper()
        startingkey = input("What is the starting key that you are using?\n").upper()
        for i in range(len(plaintext)):
            if i+1 <= len(startingkey):
                keypart = startingkey[i]
            else:
                keypart = message[i-1]
            messagepart = ord(plaintext[i])-ord(keypart)+65
            if messagepart < 65:
                messagepart += 26
            message += chr(messagepart)
        print("Your Decrypted Message Is: " + message)
    else:
        print("\033[3mPlease use one of the Available Tools\033[0m\nencrypt\ndecrypt")

elif ciphertype == "static":
    encrypt = input("Would you like to encrypt or decrypt a message?\n").lower()
    if encrypt == "encrypt":
        plaintext = input("What is the string you would like to encrypt?\n").upper().replace(" ","").replace(",","")
        key = input("What is the key you are using?\n").upper()
        while len(key) < len(plaintext):
            key += key
        for i in range(len(plaintext)):
            finalpart = ord(plaintext[i])+ord(key[i])-65
            if finalpart > 90:
                finalpart -= 26
            finaltext = chr(finalpart) + chr(rand(32,126))
            message += finaltext
        print("Your Encrypted Message Is: " + str(message))
    elif encrypt == "decrypt":
        plaintext = input("What is the string you would like to decrypt?\n").upper()
        key = input("What is the key you are using?\n").upper()
        plaintext = plaintext[::2]
        while len(key) < len(plaintext):
            key += key
        for i in range(len(plaintext)):
            finalpart = ord(plaintext[i])-ord(key[i])+65
            if finalpart < 65:
                finalpart += 26
            message += chr(finalpart)
        print("Your Decrypted Message Is: " + message)
    else:
        print("\033[3mPlease use one of the Available Tools\033[0m\nencrypt\ndecrypt")

elif ciphertype == "transposition":
    encrypt = input("Would you like to encrypt or decrypt a message?\n").lower()
    if encrypt == "encrypt":
        plaintext = input("What is the string you would like to encrypt?\n").upper()
        shiftnum = int(input("What is the amount you would like to shift?\n"))
        for i in range(len(plaintext)):
            if i >= len(plaintext)-shiftnum:
                finaltext = plaintext[i+shiftnum-len(plaintext)]
            else:
                finaltext = plaintext[i+shiftnum]
            message += finaltext
        print("Your Decrypted Message Is: " + message)
    elif encrypt == "decrypt":
        plaintext = input("What is the string you would like to decrypt?\n").upper()
        shiftnum = int(input("What is the amount you would like to shift\n"))
        for i in range(len(plaintext)):
            if i >= len(plaintext)+shiftnum:
                finaltext = plaintext[i-shiftnum+len(plaintext)]
            else:
                finaltext = plaintext[i-shiftnum]
            message += finaltext
        print("Your Decrypted Message Is: " + message)
    else:
        print("\033[3mPlease use one of the Available Tools\033[0m\nencrypt\ndecrypt")

else:
    print("\033[3mPlease use one of the Available Ciphers\033[0m")
    print("Running Key\nCaesar\nAtbash\nBaconian\nAutokey\nStatic\nTransposition")