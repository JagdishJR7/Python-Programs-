#roots of quadratic equation:
import math
a=int(input("enter the cofficient a "))
b=int(input("enter the cofficient b "))
c=int(input("enter the cofficient c "))
d=b*b-4*a*c;
if d>0:
   s1=(-b+math.sqrt(d))/2*a
   s2=(-b-math.sqrt(d))/2*a
   print("roots are real and unequal" ,s1,"and",s2)         #4/8/2
elif d==0:
    s1=b/2*a
    print("roots are real and same ",s1)
else:
    print("no real roots are there")
