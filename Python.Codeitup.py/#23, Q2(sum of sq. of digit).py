#23,sum of square of digit:
i=int(input("Enter the digit :"))
sum=0
while (i>0):
    sum=sum+(i%10)*(i%10)
    i=i//10
print("sum of square of digit =",sum)
