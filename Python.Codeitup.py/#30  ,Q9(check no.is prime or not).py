#30,check whether a number is prime or not;
n=int(input("Enter a nouber :"))
count=0
i=1
while (i<=n):
     if (n%i==0):
        count=count+1
     i=i+1
if (count==2):
    print("Prime number")
else:
    print("Not a prime number")
    
