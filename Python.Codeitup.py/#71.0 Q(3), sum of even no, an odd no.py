#70.0 sum of evn no. an odd no.in list
a=[]
size=int(input("How many Element you want to Enter in list :"))
for i in range(size):
    x=int(input("Enter number :"))
    a.append(x)
print("original list :",a)
even=0
odd=0
sum=0
total=0
for i in range(size):
    if (a[i]%2==0):
       even=even+1
       sum=sum+(a[i])
    else:
        odd=odd+1
        total=total+(a[i])
print("Total even no. =",even,"and sum is :",sum)
print("Total odd no. =",odd,"and sum is :",total)
