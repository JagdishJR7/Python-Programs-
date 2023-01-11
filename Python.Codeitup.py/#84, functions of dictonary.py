#84, function of dictonary:
dict1={'brand':'maruti','model':'dzire','year':2016}
#1, len(():
x=len(dict1)
print("Length of dictonary:",x)

#2,remove function: pop(()
print(dict1)
dict1.pop('model')
print(dict1)

#3, pop items:
dict1={'brand':'maruti','model':'dzire','year':2016}
print(dict1)
dict1.popitem()
print(dict1)

#4,del(keys) func():
dict1={'brand':'maruti','model':'dzire','year':2016}
del dict1['year']
print(dict1)

#5, clear key words:
dict1={'brand':'maruti','model':'dzire','year':2016}
print(dict1)
dict1.clear()
print(dict1)
