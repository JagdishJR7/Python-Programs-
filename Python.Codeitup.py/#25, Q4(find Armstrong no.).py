#25,find number is Armstrong or not:
i=int(input("Enter the digit :"))
orig=i
sum=0
while (i>0):
    sum=sum+(i%10)*(i%10)*(i%10)
    i=i//10
print("sum of cubes of digit=",sum)

if orig==sum :
  print("Number is Armstrong")              #153,1634
else:
    print("Number is not Aremstrong")
