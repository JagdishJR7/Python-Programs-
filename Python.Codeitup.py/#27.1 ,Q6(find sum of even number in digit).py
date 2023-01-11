#27.1Q6,sum of even digit and pro of odd digit in digit:
i=int(input("Enetr the digit :"))
sum=0
pro=0
while (i>0):
    d=i%10
    if d%2==0:
        sum=sum+d
    else:
        pro=pro+d
    i=i//10
    
print("sum of even number =",sum,"Product of odd no. =",pro)
