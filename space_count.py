a=input("Enter file name:")
k=0
 with open(a,'r') as f:
     for line in f:
         b=line.split()
         for i in b:
            for c in i:
                 if(c.isspace):
                     k=k+1
print(k)
