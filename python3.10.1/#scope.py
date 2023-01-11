global b
def scopeTest(a):
    
    b=8
    print("inside function a =",a)
    print("inside function b =",b)
a=1
b=2
scopeTest(7)
print("outside function a =",a)
print("outside function b =",b)
