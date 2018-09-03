a=int(input("Enter the number"))
factor=0
for i in range(1,a):
  if a%i==0:
    fact=i
if fact>1:
  print("It is composite")
else:
  print("Not composite")
