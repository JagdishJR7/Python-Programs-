#MENU pro. of string operator :
print("1 : return  the position of subdtring in string ")
print("2 : replace the substring 'good' with 'best' in the given string ")
print("3 : find all substring seprated by delimiter ")
print("4 : convert a line into title form ")
print("5 : check  if a given string is palindrome ")
j=1
while j>0:
    choice=input("enter your choice :")
    if choice=='1':
        s=input("enter the string :")
        s1=input("pick a substring :")
        print("position os chosem substring =",end="")
        print(s.find(s1))
        print()
    elif choice=='2':
        s=input("enter the  string ")
        s1=s.replace("good","best")
        print("the mutated string is ",s1)
        print()
    elif choice=='3':
        s=input("enter the string :")
        print("the substring seprated by ';'",end="")
        print(s.split(";"))
        print()
    elif choice=='4':
        s=input("enter the string :")
        print("the title form oof string is :",s.title())
        print()
    elif choice=='5':
        s=input("enter  a string ")
        print()
        if s==s[::-1]:
            print("string is palindrome ")
        else:
            print("not palindrome ")
    else:
        print("invalid choice")
        print()
    
