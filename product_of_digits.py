x=int(input("Enter the number:"))
y=1
while x>0:
  z=x%10
  y*=z
  x//=10
print(y)
