a=input("enter the number:")
b=[]
for i in a:
  if(int(i)%2==0):
    continue
  else:
    b.append(i)
print(" ".join(str(x) for x in b))
