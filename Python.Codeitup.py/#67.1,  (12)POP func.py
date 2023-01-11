# 67.1 (12).pop func in list:
a=[5,6,3,2,1,48,5,5]
a.pop()
print(a)

a=[]
for i in range(5):
    x=input("enter item to be in list :")
    a.append(x)
print("original list :",a)
a.pop()
print("after poping :",a)
