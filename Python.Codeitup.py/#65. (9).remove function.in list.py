#65, (9)remove(oabject),function
a=["ram",5,"shyam",6,"ravi"]
print("list=",a)
a.remove("shyam")
print("new list=",a)

a=[]
for i in range(5):
    x=input("enter number:")
    a.append(x)
print("original List =",a)
val=input("enter value to  remove :")
a.remove(val)
print(a)
