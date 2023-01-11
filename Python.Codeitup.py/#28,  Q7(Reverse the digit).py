#28,Q7 reverse the digit:
i=int(input("Enetr the digit :"))
rev=0
while (i>0):
    rev=(rev*10)+i%10
    i=i//10
print("Reverse digit =",rev)
