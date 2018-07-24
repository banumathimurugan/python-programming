a=input("Enter the number");
while(a!=0):
      re=re*10;
      re=re+a%10;
      a=a/10;
print("the reverse of the number",re);
return 0
