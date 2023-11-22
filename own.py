import random

# Caesar Cipher


def caesarCipherEncryption(plainText, key):
    encryptedText = ""


    for i in range(len(plainText)):
        character = plainText[i]
        if character.isupper():
            encryptedText += chr((ord(character) + key -65) % 26 + 65)
        elif character.islower():
            encryptedText += chr((ord(character) + key -97) % 26 + 97)
        elif character.isdigit():
            encryptedText += str(int(character) + key)
        else:
            encryptedText += character
       
    return encryptedText


def caesarCipherDecryption(encryptedText, key):
    plainText = ""


    for i in range(len(encryptedText)):
        character = encryptedText[i]
        if character.isupper():
            plainText += chr((ord(character) - key -65) % 26 + 65)
        elif character.islower():
            plainText += chr((ord(character) - key -97) % 26 + 97)
        elif character.isdigit():
            plainText += str(int(character) - key)
        else:
            plainText += character
       
    return plainText


# Monoalphabetic Cipher


import random


alpha = "abcdefghijklmnopqrstuvwxyz"


def monoalphabeticEncrypt(original, key=None):


    if key is None:
        l = list(alpha)
        random.shuffle(l)
        key = "".join(l)


    new = []


    for letter in original:
        new.append(key[alpha.index(letter)])


    return ["".join(new), key]


def monoalphabeticDecrypt(cipher, key=None):
    if key is not None:
        new = []
        for letter in cipher:
            new.append(alpha[key.index(letter)])


        return "".join(new)


# Vignere Cipher




import math




def generateKey(plainText, keyword):
    key = keyword * math.ceil(len(plainText)/len(keyword))
    key = key[:len(plainText)]
    return key




def vignereCipherEncryption(plainText, key):
    encryptedText = []
    for i in range(len(plainText)):
        x = (ord(plainText[i]) +
             ord(key[i])) % 26
        x += ord('A')
        encryptedText.append(chr(x))
    return("" . join(encryptedText))




def vignereCipherDecryption(encryptedText, key):
    orig_text = []
    for i in range(len(encryptedText)):
        x = (ord(encryptedText[i]) -
             ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return("" . join(orig_text))


# Vernam Cipher


def vernamCipherEncryption(plainText, key):
    cipherText = ""
    cipher = []
    for i in range(len(key)):
        cipher.append(ord(plainText[i]) - ord('A') + ord(key[i])-ord('A'))
 
    for i in range(len(key)):
        if cipher[i] > 25:
            cipher[i] = cipher[i] - 26
 
    for i in range(len(key)):
        x = cipher[i] + ord('A')
        cipherText += chr(x)
 
    return cipherText
 
def vernamCipherDecryption(encryptedText, key):
    plainText = ""
    plain = []


    for i in range(len(key)):
        plain.append(ord(encryptedText[i]) - ord('A') - (ord(key[i]) - ord('A')))


    for i in range(len(key)):
        if (plain[i] < 0):
            plain[i] = plain[i] + 26


    for i in range(len(key)):
        x = plain[i] + ord('A')
        plainText += chr(x)


    return plainText


# Rail Fence Cipher


def encryptRailFence(text, key):
 
    rail = [['\n' for i in range(len(text))] for j in range(key)]
    dir_down = False
    row, col = 0, 0
     
    for i in range(len(text)):
        if (row == 0) or (row == key - 1):
            dir_down = not dir_down
        rail[row][col] = text[i]
        col += 1
       
        if dir_down:
            row += 1
        else:
            row -= 1
    result = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    return("" . join(result))
     
def decryptRailFence(cipher, key):
 
    rail = [['\n' for i in range(len(cipher))]
                for j in range(key)]
     
    dir_down = None
    row, col = 0, 0
     
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
           
        rail[row][col] = '*'
        col += 1
        if dir_down:
            row += 1
        else:
            row -= 1
             
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if ((rail[i][j] == '*') and
            (index < len(cipher))):
                rail[i][j] = cipher[index]
                index += 1
         
    result = []
    row, col = 0, 0
    for i in range(len(cipher)):
         
        if row == 0:
            dir_down = True
        if row == key-1:
            dir_down = False
             
        if (rail[row][col] != '*'):
            result.append(rail[row][col])
            col += 1
             
        if dir_down:
            row += 1
        else:
            row -= 1
    return("".join(result))
    
    
    
    
    
    
    
text = input("Enter the text: ")
key = input("Enter the key: ")
rs = random.randint(1,27)
ct = vignereCipherEncryption(caesarCipherEncryption(text, rs), key)

print("ct = ", ct)
dt = (caesarCipherDecryption(vignereCipherDecryption(ct, key),rs))

pt= []
for i in dt:
    pt.append(chr(ord(i)-6))
pt = ''.join(pt)
print("dt = ", pt)