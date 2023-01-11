#pro. use recursion print fibonacci series:
def rec_fib(n):
    if n==1:
        return 0
    elif n<=2:
        return 1
    else:
        return (rec_fib(n-1) + rec_fib(n-2))

n=int(input("enter the no. upto which you want print series :"))
if n<=0:
    print("invalid input")
else:
    print("fibonacci series ")
for i in range(1,n+1):
    print(rec_fib(i))
