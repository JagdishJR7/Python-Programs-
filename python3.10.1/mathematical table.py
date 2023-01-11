#program of mathemaatical table:
n=int(input("enter the number :"))
for i in range(1,13):
    print(n,"x","-",n*i)
    print(n/i)
    print(n,"=",n/i)
    print(n,"x","=",n/i)
    print(n,"x","-",n+i)
    print(n,"x","=",n-i)
