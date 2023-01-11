#34,star pyramid star :
n=int(input("Enter the number of rows:"))
i=1
while(i<=n):
    j=1
    while(j<=i):
        print('$',end=' ')
        j=j+1
    print()
    i=i+1
    
#35,star pattern:
n=int(input("Enter the no. of rows :"))
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
