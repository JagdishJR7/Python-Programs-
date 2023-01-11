print('genreal equation of a qudratic equation is Ax**2+bx+c')
a=int(input("enter cofficient of x**2 :"))
b=int(input("enter cofficient of x :"))
c=int(input("enter cofficient of C :"))
d=b**2-4*a*c
if d>0:
    print("equation have two real and distint root")
elif d==0:
    print("equation have two real and equal root")
else:
    print("roots are imaginary")
if d>0 or d==0:
    s1=(-b + d**0.5)/2*a
    s2=(-b - d**0.5)/2*a
    print("roots of equation are ===>>",s1,s2)
