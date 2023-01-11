#81, change tuple values:
x=('apple','bannana','cherry')
y=list(x)
y[1]='kiwi'
x=tuple(y)
print(x)

#check items exit in the tuple:in or not in :
tuple1=("ram","shyam","ravi","kawwi")
if "ram" in tuple1:
    print("Yess ram present in tuple1")
else:
    print("no ram is not present in tuple1")
    
#add the tuple
tuple1=("ram","ravi","kawi","jag","dag","True",)
tuple2=list(tuple1)
tuple2.insert(5,"fualse")
x=tuple(tuple2)
print("new tuple",x)

#del tuples element:(all)
tup1e1=(1,2,3,"ram',shyam",5,",jagdish","kawi")
print(tuple1)
del(tuple1)
print("After deleting:")
print(tuple1)
