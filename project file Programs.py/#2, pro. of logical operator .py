# program of logical operator .py
a=int(input('enter the 1st number :'))
b=int(input("enter the 2nd number :"))
c=int(input("enter the 3rd number :"))

#Logical operator :(and)
print((a>b) and (a>c))
print((c>b) and (c>a))
print((b>c) and (b>a))

#Logical operator :(or)
print((a>b) or (a<b))
print((c>b) or (c<b))

#Logicall operator :(not)
print(a>b)
print(not(a>b))
