#4fibonacci series :1 1 2 3 5 8 12 ...
def fib(s):
    s1=1
    s2=1
    print(s1)
    print(s2)
    for i in range(2,10):
        s3=s1+s2
        s1=s2
        s2=s3
        print(s3)
    return(s3)
n=int(input("Enter the number of terns :"))
fib(n)
