#64, (8).list.insert(index,obj):
a=["ram","shyam","gita","bita","chita"]
a.insert(1,"jagdish")
print(a)

a=[]
for i in range(5):
    x=input("Enter number :")
    a.append(x)
print("list=",a)
a.insert(2,"9")
print("New List =",a)


a=[]
for i in range(5):
    x=input("Enter number :")
    a.append(x)
print("Original list =",a)
index=int(input("Enter index where you want to insert value :"))
value=input("enter value that you want to insert :")
a.insert(index,value)
print("NEW LIST =",a)
