import math
a=int(input("Enter the number"))
b=int(input("Enter the number"))
z=b*a
print(z)
z_sqrt=z**0.5
if(z_sqrt==int(math.sqrt(z))):
  print("yes")
else:
  print("no")
