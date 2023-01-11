print(" 1 : ")
print(" 2 : ")
print(" 3 : ")
j=1
while j>0:
    choice=input("enter your choice :")
    if choice=='1':
        def func(n):
            for i in range(1,11):
                print(n,"x",i,"=",n*i)
            return(n)
        n=int(input("enter the number :"))
        func(n)

    elif choice=='2':
        def func(x):
            if x%400==0:
                print("Leap year")
            elif x%4==0 and x%100!=0:
                print("Leap year")
            else:
                print("None leap year")
        x=int(input("Enter a year :"))
        func(x)
        
    elif choice=='3':
        def func():
            c='y'
            while c=='y':
                s=input("Enetr a string:")
                if s==s[::-1]:
                    print("palindrome")
                else:
                    print("Not a palindrome")
        func()
    else:
        print("invalid choice")
        

        

            
