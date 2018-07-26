n=int(input("Enter an number"))
s=0
while(n>0):
   r=n%10
   s=s+r
   n=n//10
if n==0:
   print("the sum of integer is%d" %s)
