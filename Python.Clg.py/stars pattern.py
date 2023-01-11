# program of stars pattern:
n=int(input("enter the number of rows "))
for i in range(1,n+1):
    print("*"*i)
#
n=int(input("enter  the number of rows:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if j<=i:
          print("*",end=' ')
        else:
            print(" ",end=' ')
    print()
#
n=int(input("enter  the number of rows:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if j>=i:
          print("*",end='')
        else:
            print(" ",end='')
    print()
#
n=int(input("enter  the number of rows:"))
for i in range(1,5):
    for j in range(1,5):
        if j>=5-i:
          print("*",end='')
        else:
            print(" ",end='')             # J>=i
    print()
#
for i in range(1,5):                  #****   J<=4
    for j in range(1,5):              #***    J<=3
        if j<=5-i:                    #**     J<=2
          print("*",end='')           #*      J<=1    
        else:                               # J<=i
            print(" ",end='')
    print()
#
n=int(input("enter  the number of rows:"))
for i in range(1,5):                    #      *
     for j in range(1,8):               #     ***
        if j>=5-i and j<=3+i :          
           print("*",end='')
        else:                            
            print(" ",end='')             
     print()
