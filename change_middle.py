a=input("Enter any string")
b=len(a)
c=list(a)
a=''
if b%2!=0:
    for i in range(b//2):
      a+=c[i]
    a+='*'
    d=b//2+1
else:
  for i in range(b//2):
    a+=c[i]
   a+='*"
   d=b//2+1
for i in range(d,b):
        a+=c[i]
print(a)
  
