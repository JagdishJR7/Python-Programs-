# all major list function:
a=[]
x=int(input("Enter max size :"))
for i in range(x):
    val=input("enter values:")
    a.append(val)
print("original list is :",a)
print("Length of list is :",len(a))
print("max value in  list is :",max(a))
print("Min value in list is :",min(a))
b=a
print("Content of list a is :",a)
print("Content of list b is  :",b)
z=input("enter value to be count :")
s=a.count(z)
print(z,"Appear in the list",s,"Times")
z=input("enter value whose index you want  :")
s=a.index(z)
print("index value of  is :",s)
val =input("Enter value to insert :")
ind =int(input("Enter index where you  want to insert :"))
a.insert(ind,val)
print(a)
val= input("Enter value that you want to remove :")
a.remove(val)
print(a)
a.sort()
print("List after shorting :",a)
a.sort(reverse=True)
print("decending order :",a)
a.sort(reverse=False)
print("Accending order :",a)
a.pop()
print(a)
