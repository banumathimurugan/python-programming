x=int(input("Enter first number:")
y=int(input("Enter secomd number:")
def gcd(x,y):
  if x==0 or y==0:
    return 0
  if x==y:
    return x
  if x>y:
    return gcd(x-y,y)
  return gcd(x,y-x)
def lcm(x,y):
  return x*y/gcd(x,y)
print("LCM of",a,"and",b,"is:",int(lcm(x,y)))
