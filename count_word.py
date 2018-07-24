a=input(Enter file name:")
b=0
with open(a,'r') as f:
    for line in f:
    c=line.split()
    b += len(c)
print(b)
