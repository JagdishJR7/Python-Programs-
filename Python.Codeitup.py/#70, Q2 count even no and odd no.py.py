#70, Q2 count even no. and odd no. in list:
a=[]
size=int(input("How many Element you want to Enter in list :"))
for i in range(size):
    x=int(input("Enter number :"))
    a.append(x)
print("original list :",a)
even=0
odd=0
for i in range(size):
    if (a[i]%2==0):
       even=even+1
    else:
        odd=odd+1
print("Total even no. =",even)
print("Total odd no. =",odd)
