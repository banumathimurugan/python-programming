a=int(input("Enter the number:"))
l=[]
for i in range(a):
  l.append(int(input()))
for i in range(1,n):
  if l[i-1]>l[i]:
    print(l[i-1])
    break
