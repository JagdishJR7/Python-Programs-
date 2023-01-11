#76, Q().find min value and second min value :
a=[]
size=int(input("enter the size of the of the list :"))
for i in range(size):
    x=int(input("enter number :"))
    a.append(x)
print("original list :",a)
minval=min(a)
print("minimum value: ",minval)
a.remove(minval)
smin=min(a)
print("second min value :",smin)

#second way to write program:
a=[]
size=int(input("enter the size of the of the list :"))
for i in range(size):
    x=int(input("enter number :"))
    a.append(x)
print("original list :",a)
a.sort()
print("Min value :",a[0])
print("second min value :",a[1])
print("max value :",a[size-1])
print("Second max value :",a[size-2])
