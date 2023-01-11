#program of factorial series:
n=int(input("enter the number"))
s1=1
for i in range(2,n+1):
     s1=s1*i
print("factorial of ",n," = ",s1)
