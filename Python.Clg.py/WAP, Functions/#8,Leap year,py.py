#8,Leap year:
def func(x):
    if x%400==0:
       print("Leap year")
    elif x%4==0 and x%100!=0:
        print("Leap year")
    else:
        print("None leap year")
x=int(input("Enter an year :"))
func(x)
