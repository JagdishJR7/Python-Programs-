# Area of square, circle, reactangle, triangle.
import math
print("Area Calculation\n")
cont='y'
while cont == 'y' or cont == 'Y':
    print("Area of Circle    : 1")
    print("Area of square    : 2")
    print("Area of Reactangle: 3")
    print("Area of Triangle  : 4")
    choice=int(input("\nEnter your choice : "))

    if choice == 1:
        r=int(input("Enter radius :"))
        print("Area of Circle = ", math.pi*r*r)
    elif choice == 2:
        s=int(input("Enter the side of square :"))
        print("Area of square =",s*s)
    elif choice == 3:
        a=int(input("Enter Length : "))
        b=int(input("Enter Breadth : "))
        print("Area of Reactangle =",a*b)
    elif choice == 4:
        p=int(input("Enter side 1 :"))
        q=int(input("Enter side 2 :"))
        n=int(input("Enter side 3 :"))
        s=(p+q+n)/2
        t=s*(s-p)*(s-q)*(s-n)
        print("Area of triangle =",math.sqrt(t))
    else :
        print("invalid choice")

    cont=input("\nDo you want to continue ? (y/n) : ")

print("\nThankyou")
