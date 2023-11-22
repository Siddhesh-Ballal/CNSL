import random

p = int(input("enter p="))
d = int(input("enter d="))
e1 = int(input("enter e1="))
e2 = (e1**d)%p

print(e2)
print("pub key = (",e1,",",e2,",",p,")")


# enc
r = random.randint(100,1000)
print("r=",r)
c1 = (e1**r) % p
pt = int(input("enter pt="))
c2 = (pt * (e2**r))%p

print("ct = (",c1,",",c2,")")

# dec
for i in range(p):
    if i*(c1**d)%p == 1:
        x=i
        break

print("pt = ", (c2*x)%p)