year=int(input(" "))
if(year%4==0 and year!=100) or (year%400==0):
 print ("Leap year")
else:
 print("Not leap year")
