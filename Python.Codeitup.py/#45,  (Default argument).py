#45,Default argument;
def add(a,b,c=5):
    d=a+b+c
    print("Addition=",d)
add(5,6)
add(5,6,7)
add(10,10,10)
add(5,56,5,)
x=int(input("Enter 1st value"))
y=int(input("Enter 2nd number"))
add(x,y)
