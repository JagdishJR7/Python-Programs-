#rpogram of selection sort:
def selsort(list,n):
    j=n-1
    while j>0:
        large=list[0]
        index=0
        for i in range(1,j+1):
            if list[i]>large:
                large=list[i]
                index=i
        list[index]=list[j]
        list[j]=large
        j-=1
list=[]
n=int(input("enter the no. of values :"))
print("enter the values")
for i in range(0,n):
    a=int(input(":"))
    list.append(a)
selsort(list,n)
print("sortest list\n")
for i in range(0,n):
    print(list[i])
