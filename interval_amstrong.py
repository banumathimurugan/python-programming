l=int(input())
u=int(input())
for num in range(l,u+1):
   order=len(str(num))
   temp=num
   sum=0
   while(temp>0):
       rem=temp%10
       sum=sum+rem**order
       temp//=10
   if(num==sum):
       print(num)    
