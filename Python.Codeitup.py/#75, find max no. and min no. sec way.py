#75 Q(9).find max no. and min no. in the list
a=[]
size=int(input("enter size of the list that you want :"))
for i in range(size):
    x=int(input("enter number"))
    a.append(x)
print("original list :",a)
maxval=max(a)
minval=min(a)
print("maximum value :",maxval)
print("minimum value :",minval)
                
