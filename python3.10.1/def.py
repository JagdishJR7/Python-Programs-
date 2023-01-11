#
def javaprogram():
    print("function")
javaprogram()
print("done")

def  fnDemo2(str):
    print("Hello",str)
fnDemo2("jack")
str=input("Enter name :")
fnDemo2(str)

def add(a,b,c):
    s = a+b+c
    return s
a=0
b=0
c=0
a,b,c = input("Enter three number :").split()
print("Sum =",add(a,b,c))

a=int(a)
b=int(b)
c=int(c)
print("Sum ",add(a,b,c))
