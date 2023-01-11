#8 Identity operator:(is or not is):
x=5
y=10
print(x is y)
print(x is not y)
#(is)
x=5;
if (type(x) is int ):
    print("correct")
else:
    print("incorrect")
#(is not)
x=5.2;
if (type(x) is not int):
    print("corrrect")
else:
    print("incorrect")

#8 Membership operator:(in or not in):
a=15;
list=[1,2,3,4,5,6,7,89,10,11]
if (a in list):
    print("Yes a is present in the list")
else:
    print("No a is not in list")
b=4;
list=[1,2,3,4,5]
if (b not in list):
    print("Yes a is not present in the list")
else:
    print(" a is present in the list")
