n=input()
list=[]
for i in range(0,n):
    int_input=int(raw_input())
    list.append(int_input)
for a in list:
    a=min(list)
print (a)
