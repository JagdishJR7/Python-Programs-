#43 find number is odd or even:by  function:
def func():                             #without argument
    a=int(input("Enter the value :"))
    if a%2==0:
        print("even value")
    else:
        print("odd value")
func()

#with srgument
def func(a):
    if a%2==0:
        print("Even value")
    else:
        print("Odd value")
func(4)
func(5)
m=int(input("enter the value:"))
func(m)
