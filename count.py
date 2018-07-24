a=input("Enter the value")
b=len(a)
while True:
    if " " in a:
        b=b-1
        if(" " not in a):
           break
        print(b)
    else:
        print(b)
