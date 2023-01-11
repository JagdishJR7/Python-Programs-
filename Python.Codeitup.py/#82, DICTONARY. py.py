#82, DICTONARY topic:
dic1={"brand":"suzuki","model":"Dzire","Year":2020}
print(dic1)
x=dic1["model"]
print(x)
y=dic1.get("brand")
print(y)
#loop through a dicyonary:
dict1={"brand":"suzuki","model":"Dzire","Year":2020}
for i in dict1:
    print(i)         #keys:

for x in dict1:
    print(dict1[x])       #values:

for y in dict1.values():   #values:
    print(y)

for i,j in dict1.items():  #both keys and values:
    print(i,j)

#change values :
dict2={'brand':'suzuki','model':'Dzire','Year':2020}
dict2['Year']=2019
print(dict2)
dict2['model']='Dzir'
print(dict2)
