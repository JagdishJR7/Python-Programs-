#27,prodouct of digit;
i=int(input("Enter the digit :"))
pro=1
while(i>0):
    pro=pro*(i%10)
    i=i//10
print("product of digit =",pro)
