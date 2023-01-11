print(" 1 : ")
print(" 2 : ")
j=1
while j>0:
    choice=input("enter your choice ")
    if choice=='1':
        def func(n):
            for i in range(1,n+1):
                for j in range(1,n+1):
                    if j<=i:
                        print("*",end=' ')
                    else:
                        print(" ",end=' ')
                print()
        n=int(input("enter  the number of rows:"))
        func(n)
    elif choice=='2':
        def func():
            for i in range(1,5):
                for j in range(1,8):
                    if j>=5-i and j<=3+i:
                        print("*",end=' ')
                    else:
                        print(" ",end=' ')
                print()
        func()
    else:
        print("invalid choice")
        print()
        
