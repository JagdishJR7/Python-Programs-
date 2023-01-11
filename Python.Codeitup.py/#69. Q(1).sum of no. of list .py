#69 Q(1)find sum of list (using list):
a=[]
size=int(input("How many Element you want to Enter in list :"))
for i in range(size):
    x=int(input("Enter number :"))
    a.append(x)
print("original list :",a)
sum=0
for i in range(size):
    sum=sum+a[i]
print("Sum of list element is :",sum)
