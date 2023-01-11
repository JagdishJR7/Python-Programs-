#program to search no. by binary search:
def bsearch(l,n,val):
    found=0
    low=0
    high=n-1
    while low<=high and not(found):
        mid=int((low+high)/2)
        if val==l[mid]:
            found=1
        elif val<l[mid]:
            high=mid-1
        else:
            low=mid+1

    if found:
        return mid
    else:
        return -1
l=[]
n=int(input("ENter the no. of values :"))
print("Enter the values ")
for i in range(0,n):
    a=int(input(":"))
    l.append(a)

c="y"
while c=='y' or c=="Y":
    val=int(input("Enter the no. to be searched "))
    p=bsearch(l,n,val)
    if p==-1:
        print("value not present ")
    else:
        print("value present at",p+1,"position")
    
