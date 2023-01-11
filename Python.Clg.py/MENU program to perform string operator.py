# MENU:program by using string charactors:
print(" 1 : return the position of substring in the string ")
print(" 2 : replace the substring 'good' with 'best' in the given string")
print(" 3 : find all substring seprated by delimeter")
print(" 4 : convert a line into title form")
print(" 5 : convert the lower case charactere to uppercase and vice versa")
print(" 6 : check if a given string is a palindrome")
j=1
while j>0:
     choice= input("enter your choice")
     if choice=='1':
         s=input("Enter the string :")
         s1=input("pick a substring :")
         print("position of chosen substring = ",end="")
         print(s.find(s1))
         print()
     elif choice=='2':
         s=input("Enter a string :")
         s1=s.replace("good","best")
         print("the mutated string is : ",end="")
         print(s1)
         print()

     elif choice=='3' :
         s=input("Enter a string :")
         print("the substtring seprated by ';' are :",end="")
         print(s.split(";"))
         print()
     elif choice=='4' :
         s=input("Enter a string :")
         print("The title form of string is :",end="")
         print(s.title())
         print()
     elif choice=='5' :
         s=input("Enter the string :")
         for i in range(0,1):
             if s[i].isupper():
                 s1=s[i].lower()
                 print(s1,end="")
             else:
                 s1=s[i].upper()
                 print(s1,end="")

             print()
     elif choice=='6' :
         s=input("Enter a string :")
         print()
         if s==s[::-1]:
             print("string is palindrome")
         else:
             print("not palindrome")
             print()

     else:
         print("invalid choice")
         print()
         
