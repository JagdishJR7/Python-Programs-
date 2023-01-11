print(" 1 : Enter the number of rows")
print(" 2 : Enter the no. of rows ")
print(" 3 : Enetr the  no. of rows ")
print(" 4 : eenter  the no. of rows ")
j=1
while j>0:
    choice = input("enter your choice :")
    if choice=='1':
        i=1
        while(i<=n):
              j=1
              while(j<=i):
                    print('$',end=' ')
                    j=j+1
        print()
        i=i+1
    elif choice=='2':
        i=1
        while(i<=n):                      #to count number of rows
              b=1
              while(b<=n-i):
                   print(' ',end=" ")          #for blank space:
                   b=b+1
              j=1
              while(j<=i):
                   print("$",end=" ")        #for print star
                   j=j+1
              print()
              i=i+1
