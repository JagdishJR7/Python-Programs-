#21Q10,sum of first n number :
n=int(input("How many number you want to add :"))
i=1
sum=0
count=0
while (count<n):
    if i%2==0:
        sum=sum+i
        count=count+1
    i=i+1
print("sum of Even number =",sum)
