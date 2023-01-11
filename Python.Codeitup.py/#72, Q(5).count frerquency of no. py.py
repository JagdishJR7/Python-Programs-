#72 Q5(count frequency of no.):
a=[]
size=int(input("enttre size of the list :"))
for i in range(size):
    x=int(input("Enter number :"))
    a.append(x)
print("original list is :",a)
key=int(input("enter number to find fruquency :"))
count=0
for i in range(size):
    if (a[i]==key):
        count=count+1
print("Frequency =",count)
