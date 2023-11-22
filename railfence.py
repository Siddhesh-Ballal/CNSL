s = input("Enter the string: ")
k = int(input("Enter the key: "))
enc=[[" " for i in range(len(s))] for j in range(k)]
print(enc)
flag=0
row=0
for i in range(len(s)):
  enc[row][i]=s[i]
  if row==0:
    flag=0
  elif row==k-1:
    flag=1
  if flag==0:
    row+=1
  else:
    row-=1
print(enc[row][i])

for i in range(k):
  print("  ".join(enc[i]))

ct=[]
for i in range(k):
    for j in range(len(s)):
      if enc[i][j]!=' ':
        ct.append(enc[i][j])
print("Ciphertext: ", ct)

# def decoder(ct, k):
#   ct = ct.replace(" ","")
#   print(ct)
  
# decoder(ct, k)
ct = ' '.join(ct)
print(ct)
j=0
flag=0
for i in range(len(ct)):
   print(enc[j][i])
   if(j==k-1):
     flag=1
   elif j==0:
     flag=0
   if(flag==0):
     j+=1 
   else:
     j-=1
