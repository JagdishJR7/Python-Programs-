print(" 1 : ")
print(" 2 : ")
print(" 3 : ")
j=1
while j>0:
    choice=input("enter your choice :")
    if choice=='1':
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
       
    elif choice=='2':
        def fib(s):
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
        n=int(input("Enter the number of terns :"))
        fib(n)
    elif choice=='3':
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
                
    else:
        print("invaid choice ")
        print()
