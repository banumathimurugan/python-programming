x=int(input("Enter the number:"))
y=0
while x>0:
  b=x%10
  y=(y*10)+b
  x//=10
print(y)
