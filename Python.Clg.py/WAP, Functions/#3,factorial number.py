#3,factorial number:
def factorial(s):
    s1=1
    if n<0:
        print("The factorial is not exit")
    else:
        for i in range(1,n+1):
            s1=s1*i
        return s1
n=int(input("Enter the number :"))
res=factorial(n)
print("factorial of ",n,"=",res)

