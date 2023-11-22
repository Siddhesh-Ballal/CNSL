import random

alphabet = "abcdefghijklmnopqrstuvwxyz"

def enc(pt, k=None):
    if k is None:
        l = list(alphabet)
        random.shuffle(l)
        key="".join(l)

    ct = []    
    for i in pt:
        ct.append(key[alphabet.index(i)])
    
    return ["".join(ct), key]

def dec(ct, k):
    if k is not None:
        pt = []
        for i in ct:
            pt.append(alphabet[k.index(i)])
        return "".join(pt)


pt = "hello"
ctk = enc(pt)
ct =ctk[0]
print("ct = ",ct)
key = ctk[1]
print(dec(ct, key))