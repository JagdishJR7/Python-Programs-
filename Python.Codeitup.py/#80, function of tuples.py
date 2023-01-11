#80, function of tuples:
#1, len()
employes =('ram', 'shyam',100,12.3)
print(len(employes))
#2, max and min value :
a=(6,5,8,5,7,9.5)
print(min(a))
print(max(a))
#3, index function :
a=(10,20,30,40,50,60,40,60,30)
s=a.index(40)
print(s)
#4,count function:
z=a.count(30)
print(z)
#5, tuple function:
#"empty" tuple:
s=tuple()
print(s)
#creating from a "list"
t=tuple([1,2,3])
print(t)
#creating tuple from "string":
j=tuple("Jagdish")
print(j)
#creating tuple frome "dictonary":
A=tuple({1:"m",2:"n",3:"k"})
print(A)
