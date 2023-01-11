#20,find a sum of even number b/w 1 to n:
n=int(input("Enter Number :"))
i=1
sum=0
while (i<=n):
    if i%2==0:
        sum=sum+i
        
    i=i+1
print("Sum of even no.=",sum)
    
#20,second way:
n=int(input("Enter number :"))
i=2
sum=0
while (i<=n):
    sum=sum+i
    i=i+2
print("Sum of Even number =",sum)
    
