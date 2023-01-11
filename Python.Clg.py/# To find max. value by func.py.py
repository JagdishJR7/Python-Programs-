def findmax(lst,n):
    large = lst[0]
    for i in range(1,n):
        if lst[i]>large :
            large=lst[i]
    return large

lst=[]
n=int(input("Enter the number of values :"))
print("enter the values ")
for i in range(0,n):
    a= int(input(":"))
    lst.append(a)

p=findmax(lst,n)
print("\nMaximum value is :",p)

lst=[]
n=int(input("Enter the number of values :"))
print("enter the values ")
for i in range(0,n):
    a= int(input(":"))
    lst.append(a)
p=max(lst)
print("Maximun value :",p)
