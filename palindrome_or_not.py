a=int(input("enter number:")
temp=a
rev=0
while(a>0):
  dig=n%10
  rev=rev*10+dig
  a=a//10
if(temp==rev):
  print("yes")
else:
  print("no")
