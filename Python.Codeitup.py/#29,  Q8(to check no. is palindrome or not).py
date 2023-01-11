#29,check number  is palindrome or not:
i=int(input("Enter digit :"))
rev=0
x=i
while (i>0):
    rev=(rev*10)+i%10
    i=i//10
if (x==rev):
    print("Palindrome number")     #535,252,
else:
     print("Not a palindrome")
