#71. Linear search:/sequential search:
a=[]
size=int(input("Enter size of the list :"))
for i in range(size):
    x=int(input("enter no.:"))
    a.append(x)
print("original list is :",a)
key=int(input("Enter no. to be search :"))
flag=0
for i in range(size):
    if (a[i]==key):
        flag=1
        pos=i+1
        break
if(flag==1):
    print("element found at",pos," position ")
else:
    print("element not found ")
    
