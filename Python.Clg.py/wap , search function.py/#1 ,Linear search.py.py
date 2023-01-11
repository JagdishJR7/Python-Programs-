# Linear search
def lsearch(l,n,val):              #formal parameter :
    found=0
    i=0
    while i<n and not(found):
        if val==l[i]:
            found=1
            pos=i+1
        i+=1
    if found :
        return pos
    else :
        return -1
l=[]
n=int(input("Enter the no. of value "))
print("Enter the values ")
for i in range(0,n):
    a=int(input(":"))
    l.append(a)

c='y'                               
while c== 'y' or c=='Y':
    val=int(input("enter the values to be searched "))
    p=lsearch(l,n,val)              #actual parameter:

    if p==-1:
        print("values not present ")
    else:
        print("values present at ",p,"possition")

    c=input("\nDo you want to continue ? Y/N")
