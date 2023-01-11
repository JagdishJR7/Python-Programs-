#,MENU program of def(factorial and fibonacci series )
print("1 : to find factorial number ")
print("2 : to print  fibonacci series ")
j=1
while j>0:
    choice=input("enter  your choice :")
    if choice=='1':
        def factorial(s1):
            s1=1
            if n<0:
                print("the factorial is not defined ")
            else:
                for i in range(1,n+1):
                   s1=s1*i
                return(s1)
        n=int(input("enter the number"))
        res=factorial(n)
        print("factorial of ",n,"is",res)
    elif choice=='2':
        def fibonacci(n):
           s1=0
           s2=1
           print(s1)
           print(s2)
           for i in range(n-2):
               s3=s1+s2
               s1=s2
               s2=s3
               print(s3)
           return(s3)
        n=int(input("enter the no. upto which you to print series :"))
        s=fibonacci(n)
        print(n,"th no. of fibonacci series :",s)
    
