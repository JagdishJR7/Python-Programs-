#85, functions of dictonary:
#5, copy()
dict1={'barnd':'suzuki','model':'dzire','year':2020}
x=dict1.copy()
print(x)

#6, fromkeys method:
x=('firstkey','secondkey','thirdkey')
y=('first',2,3)
dict1=dict.fromkeys(x,y)
print(dict1)

#7, setdefault fucn():
dict1={'barnd':'suzuki','model':'dzire','year':2020}
print("original dict is :",dict1)
x=dict1.setdefault('brand','toyota')
print(x)
print(dict1)
y=dict1.setdefault('place','delhi')
print(dict1)
print(y)

#8.,update func ()
dict2={'barnd':'suzuki','model':'dzire','year':2020}
dict2.update({'color':'white'})
print(dict2)
