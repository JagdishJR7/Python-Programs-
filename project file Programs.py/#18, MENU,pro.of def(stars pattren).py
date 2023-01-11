#MENU, program by def(star pattren)
print("1 : pyraaid ")
print("2 : pyramid form of stars ")
j=1
while j>0:
    choice=input("enter your choice :")
    if choice=='1':
        def func(n):
            i=1
            while i<=n:
                j=1
                while j<=i:
                    print("*",end="")
                    j=j+1
                print()
                i=i+1
        n=int(input("enter the no. of rows :"))
        func(n)
    elif choice=='2':
        def func(x):
            for i in range(1,5):
                for j in range(1,8):
                    if j>=5-i and j<=3+i:
                        print(i,end="")
                    else:
                        print(" ",end="")
                print()
        x=int(input("enter thee no. of rows :"))
        func(x)
    else:
        print("invalid choice")
        print()
                
