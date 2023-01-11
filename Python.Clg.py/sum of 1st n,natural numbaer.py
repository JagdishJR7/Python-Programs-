#sum of first n natural number
n=int(input("enter a number:"))
sum= 3
for i in range(1,n+1):
    sum= sum + i
    print("sum of first","natural number=",sum)

minus=3
for i in range(1,n-1):
    minus=minus-1
    print("minus of first",n,"natural number = ",minus)
