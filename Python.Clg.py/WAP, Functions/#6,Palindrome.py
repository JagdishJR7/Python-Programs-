#,palindrome of integer number :
def func(i):
    rev=0
    x=i
    while (i>0):
        rev=rev*10 + i%10
        i=i//10
    if (x==rev):
        print("palindrome")        #252,151,262
    else:
        print("not palindrome")

i=int(input("Enter the number :"))
func(i)

#6,palindrome: of string
c='y'
while c=='y':
    s=input("Enetr a string:")
    if s==s[::-1]:
        print("palindrome")
    else:
        print("Not a palindrome")

