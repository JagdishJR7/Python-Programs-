#74, Q(8).reverse th eprogram :
a=[]
size=int(input("Enter size of the list :"))
for i in range(size):
     x=int(input("Entre numbre :"))
     a.append(x)
print("original list :",a)
i=0
j=size-1
while (i<j):
    t=a[i]
    a[i]=a[j]
    a[j]=t
    i=i+1
    j=j-1
print("List after reverse =")
for i in range(size):
    print(a[i])
    
    
