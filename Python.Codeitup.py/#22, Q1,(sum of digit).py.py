#22,write a program to find sum of digits:
i=int(input("Enter the digit :"))
sum=0
while (i>0):
    sum=sum+i%10
    i=i//10
print("Sum of digit =",sum)
