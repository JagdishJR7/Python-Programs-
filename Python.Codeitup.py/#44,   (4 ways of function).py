#44,FUNCTION:
#1,NO ARGUMENT NO RETURN:
def func():
    a=int(input("Enter 1st number :"))
    b=int(input("Enter 2nd number :"))
    c=a+b
    print("Sum =",c)
func()

#2,WITH ARGUMENT NO RETUERN:
def func(a,b):
    c=a+b
    print("sum=",c)
A=int(input("Enter 1st number ;"))
B=int(input("Enter 2nd number :"))
func(A,B)

#3,NO ARGUMENT WITH RETURN:
def func():
    a=int(input("Enter 1st number :"))
    b=int(input("Enter 2nd number :"))
    c=a+b
    return c
z=func()
print("sum=",z)

#WITH ARGUMENT WITH RETURN:
def func(a,b):
    c=a+b
    return c
a=int(input("Enter 1st number ;"))
b=int(input("Enter 2nd number :"))
z=func(a,b)
print("sum=",c)
