#79, tuples:
#Traversing Tuple
tuple1=(1,2,3,4)
for i in tuple1:
    print(i)
for i in range(len(tuple1)):
    print(tuple1[i])
#joining tuple:
tuple1=(1,2,3)
tuple2=(6,5,4)
tuple3=tuple1+tuple2
print(tuple3)
#Repeating and replicate tuples :
tuple1=(1,2,3)
tuple2=tuple1*3
print(tuple2)
#slicing the tuples:
tuple1=(10,12,15,14,15,14)
tuple2=tuple1[3:5]
print(tuple2)
tuple3=tuple1[0:5:2]
print(tuple3)
tuple4=tuple1[5:0:-2]
print(tuple4)
