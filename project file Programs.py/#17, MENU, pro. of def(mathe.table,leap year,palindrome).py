#MENU, pro. of def(mathematical table,leap year palindrome)
print("1 : to printt matheematicaal table ")
print("2 : to find leap year ")
print("3 : to check palindrome no.")
j=1
while j>0:
    choice=input("enter your choice :")
    if choice=='1':
        def func(n):
            for i in range(1,11):
                s=n*i
                print(n,"x",i,"=",s)
            return(n)
        n=int(input("enter a number "))
        func(n)
    elif choice=='2':
        def func(x):
            if x%4==0:
                print("Leap year")
            elif x%4==0 and x%100!=0:
                print("Leeap year")
            else:
                print("year is not a leap year")
        x=int(input("enter a year"))
        func(x)
    elif choice=='3':
        def func(n):
            c='y'
            while c=='y':
                s=input("enter a string :")
                if s==s[::-1]:
                    print("palindrome")
                else:
                    print("not a palindrome")
        n=int(input("enter a string"))
        func(n)
    else:
        print("invalid choice ")
        print()
                
            
