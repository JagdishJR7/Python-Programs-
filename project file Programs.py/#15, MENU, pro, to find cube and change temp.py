#MENU, program of def(cube, tempp converter)
print("1 : find cube of a number ")
print("2 : temp converter from celcius to fahrenheit and vice versa ")
j=1
while j>0:
    choice=input("enter your choice :")
    if choice=='1':
        def cube():
            a=int(input("enter a number "))
            s=a**3
            print(s)
        cube()
        cube()
    elif choice=='2':
        def fahrenheit(c):
            return (c*9/5)+32
        c=int(input("enter celcius temp."))
        s=fahrenheit(c)
        print("fahrenheit temp =",s)

        def celcius(f):
            return (f-32)*5/9
        f=int(input("enter temp. in fahrenheit"))
        s=celcius(f)
        print("temp in celcius :",s)
    else:
        print("invalid choice")
        print()
