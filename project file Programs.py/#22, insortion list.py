#insertion sort list:
def insort(list,n):
    for i in range(1,n):
        currentval=list[i]
        pos=i
        while pos>0 and currentval<list[pos-1]:
            list[pos]=list[pos-1]
            pos=pos-1
        list[pos]=currentval
list=[]
n=int(input("enter the no. of values :"))
print("enter the values")
for i in range(0,n):
    a=int(input(":"))
    list.append(a)
insort(list,n)
print("sortest list:\n")
for i in range(0,n):
    print(list[i])
























    
