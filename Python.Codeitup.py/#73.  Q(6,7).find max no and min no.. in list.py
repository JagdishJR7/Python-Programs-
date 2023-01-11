#73,Q(6,7) find max no. and min no. of list:
a=[]
size=int(input("Enter size of the list :"))
for i in range(size):
    x=int(input("Enter Number :"))
    a.append(x)
print("original number :",a)
max=a[0]
min=a[0]
for i in range(size):
    if (a[i]>max):
        max=a[i]
    elif (a[i]<min):
        min=a[i]
print("Max numbher ::",max)
print("Min number :",min)
