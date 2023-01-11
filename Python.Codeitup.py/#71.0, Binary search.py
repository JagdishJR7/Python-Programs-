#,71 binary search,  (it must be in accending or decending orderr:
def binary_search(a,size,key):
    found=0
    i=0
    j=size-1
    while i<=j and found==0:
        mid=(i+j)//2
        if a[mid]==key:
           found=1
           pos=mid+1
        elif a[mid]>key:
           j=mid-1
        elif a[mid]<key:
           i=mid+1
    if found==1:
        print("Number found at",pos,"position")
    else:
        print("number not found")
a=[]
size=int(input("Enter size of the list :"))
for i in range(size):
    x=int(input("enter no.:"))
    a.append(x)
print("original list is :",a)
key=int(input("Enter no. to be search :"))
binary_search(a,size,key)
