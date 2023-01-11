#67.0 sort function in list:
a=[1,5,6,3,9,8,5]
a.sort()
print(a)

a=[]
for i in range(5):
    x=input("Enter item to add in list :")
    a.append(x)
print("original list =",a)
a.sort(reverse=False)
print("accending ordedr:",a)
a.sort(reverse=True)
print("decnding order :",a)
