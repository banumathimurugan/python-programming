n=int(input())
tem=n
s=0
while(tem>0):
  r=tem%10
  s=s+r**3
  tem//=10
if(n==s):
  print(n,"is amstrong number")
else:
  print(n,"is not amstrong number")
