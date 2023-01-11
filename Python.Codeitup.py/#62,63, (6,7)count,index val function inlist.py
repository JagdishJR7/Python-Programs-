#62 ,(6) count function():
a=["ram","shyam","ram","gita","Ram","jagdish","gita"]
x=a.count("ram")
print("Frequency=",x)

a=[]
for i in range(5):
    x=input("enter number :")
    a.append(x)
print(a)
x=input("Enter the value whose frequency you want :")
s=a.count(x)
print("frequency of",x,"is =",s)

#63 ,(7)/index function():
a=["ram","shyam","gita","bita","chita"]
x=a.index("bita")
print("index value =",x)

a=[]
for i in range(5):
    x=input("Enter number :")
    a.append(x)
print(a)
x=input("enter no. whose you want index value :")
s=a.index(x)
print("Index value =",s)

