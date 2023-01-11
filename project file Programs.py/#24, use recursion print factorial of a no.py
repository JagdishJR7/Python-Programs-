# use recursion print factorial of number :
def rec_fact(n):
    if n==1:
        return 1
    else:
        return n*rec_fact(n-1)
n=int(input("enter a no."))
if n==0:
    print("factorial=1")
elif n<0:
    print("factorial is not defined")
else:
    print("factorial=",rec_fact(n))
