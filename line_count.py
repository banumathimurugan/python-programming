a=input("Enter file name:")
b=0
with open(a,'r') as f:
    for c in f:
         b +=1
print(b)
