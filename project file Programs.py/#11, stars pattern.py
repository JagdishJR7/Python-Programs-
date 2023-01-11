#stars pattern:
n=int(input("enter the no. of rows:"))
i=1
while i<=n:
    j=1
    while j<=i:
        print(j,end="")
        j+=1
    print()
    i=i+1

n=int(input("enter the no. of rows ::"))
i=1
while i<=n:
    b=1
    while b<=n-i:
        print(" ",end="")
        b=b+1
    j=1
    while j<=i:
        print(j,end="")
        j+=1
    print()
    i+=1
