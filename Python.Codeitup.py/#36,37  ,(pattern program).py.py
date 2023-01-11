#36,pattern program:
n=int(input("Enter the number of rows :"))
k=1
i=1
while (i<=n):
    b=1
    while b<=n-i:                   #space pattern 
         print(" ",end=' ')
         b=b+1
    j=1
    while j<=k:                    #star pattern
        print("j",end=' ')
        j=j+1
    k=k+2
    print()
    i=i+1
#37,pattern program:
n=int(input("Enter the no. of rows :"))
i=1
while n>0:
    b=1
    while b<i:
        print(" ",end=' ')
        b=b+1
    j=1
    while (j<=(n*2)-1):
         print("$",end=' ')
         j=j+1
    print()
    n=n-1
    i=i+1
    
