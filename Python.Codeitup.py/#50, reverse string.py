#50,reverse the string:
a=input("Enter string :")
print(a[-1::-1])

a=input("Enter string :")
for i in range((len(a)-1),-1,-1):
    print(a[i],end="")
