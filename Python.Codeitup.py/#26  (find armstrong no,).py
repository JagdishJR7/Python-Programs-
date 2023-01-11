#26,for any number find Armstrong number:
n=int(input("Enetr Number to check :"))
i=n
count=0
while (i>0):
    count=count+1
    i=i//10
sum=0
i=n
while (i>0):
    digit=i%10
    x=1
    pro=1
    while (x<=count):
        pro=pro*digit
        x=x+1
    sum=sum+pro
    i=i//10
if (sum==n):
     print("Armstrong number ")
else:
    print("Not Armstrong number")
