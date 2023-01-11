# 10.reverse fuunction in list.
a=[5,"ram",5,"shyam"]
a.reverse()
print(a)

a=[]
for i in range(5):
    x=input("enter item to add in list :")
    a.append(x)
print("original list =",a)
a.reverse()
print("reveres list =",a)
