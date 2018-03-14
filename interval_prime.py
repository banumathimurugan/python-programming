a=int(input())
b=int(input())
for n in range(a+1,b):
    m=0
    if n==0:
      m=1
    else:
       for i in range(2,n):
             if m==0:
               if n%i==0:
                  m=1
    if m==0:
       print(n)
