# reverse and add the program:
i=int(input("Enter number :"))
rev=0
sum=0
while (i>0):
    rev=(rev*10)+i%10
    sum=sum+i%10
    i=i//10
print("Reverse=",rev)
print("sum of digits=",sum)
