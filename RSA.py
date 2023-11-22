p=int(input("enter p = "))
q=int(input("enter q = "))
n = p*q

phi = (p-1)*(q-1)
e=int(input("enter e = "))

d=0
for i in range(n):
    if (i*e)%phi ==1:
        d=i
        break

print(d)

# enc:

M=int(input("enter M = "))

C = (M**e)%n
print("C = ", C)

# dec

D = (C**d)%n
print("M = ", D)