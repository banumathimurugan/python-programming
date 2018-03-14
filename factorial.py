n=int(input())
f=1
if(n<0):
   print("Enter valid number")
elif(n==0):
   print("factorial of zeo is 1")
else:
   for i in range(1,n+1):
        f=f*i
print(f)
