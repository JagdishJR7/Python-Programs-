#5 factorial series:
def func(n):
    s=0
    for i in range(0,n+1):
        f=1
        for j in range(1,i+1):
            f=f*j
            if (i%2==0):
                s=s+(1/f)
            else:
                s=s-(1/f)
n=int(input("enter the limit upto which you want to print"))
print("the sum of the series is =",s)
