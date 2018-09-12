x=int(input("Enter the number:"))
if x>1:
  for i in range(2,x):
    if x%i==0:
      print("yes")
      break
  else:
    print("No")
else:
  print("yes")
