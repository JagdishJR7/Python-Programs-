#pro to print reverse order:and sum of digit
n=int(input("enter the number :"))
rev=0
sum=0
while n>0:
    rev=(rev*10)+n%10
    sum=sum+n%10
    n=n//10
print("reverse of number =",rev)
print("sum of a digit =",sum)
