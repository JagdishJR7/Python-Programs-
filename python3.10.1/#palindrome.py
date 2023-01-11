# palindrome checking:

#case sensitive camparision
c='y'
while c=='y':
    s=input("Enetr a string:")
    if s==s[::-1]:
        print("palindrome")
    else:
        print("Not a palindrome")

# case insensitive camparision:

c='y'
while c=='y':
    s=input("Enetr a string:")
if s.upper()==s[::-1].upper():
    print("yes")
else:
    print("no")

c=input("continue (y/n)?")

#
def func(n):
    rev=0
    while (n>0):
        rev=rev*10 + n%10
        n=n//10
    if (rev==n):
        print("palindrome")
    else:
        print("not palindrome")

n=int(input("Enter the number :"))
func(n)
