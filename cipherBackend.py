def capshandling(char):
    return 0 if 'A' <= char <= 'Z' else 32 if 'a' <= char <= 'z' else -1

def overflow(finalnum, caps, plaintext):
    while ((finalnum < (65+caps)) and ('A' <= plaintext <= 'Z' or 'a' <= plaintext <= 'z')): finalnum += 26
    while ((finalnum > (90+caps)) and ('A' <= plaintext <= 'Z' or 'a' <= plaintext <= 'z')): finalnum -= 26
    return finalnum

def preset(greekEncoding, cipherdict):
    reversedict, cipherlist = {v: k for k, v in cipherdict.items()}, []
    print(', '.join(cipherlist := [reversedict[ord(i)-(945 + (1 if ord(i)-945 >= 17 else 0))] for i in greekEncoding]))
    return cipherlist