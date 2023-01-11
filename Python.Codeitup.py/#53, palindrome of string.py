#53,rpogram to check string is palindrome or not:
c='y'
while c=='y':
    a=input("enter string:")
    b=a[-1::-1]
    if(a==b):
       print("Palindrome string")               #madam
    else:
         print("Not Palindrome string")
