print(" 1 : ")
print(" 2 : ")
j=1
while j>0:
    choice=input("enter your choice ")
    if choice=='1':
        def cube():
            a=int(input("Enter the no.:"))
            s=a**3
            print("Cube =",s)
        cube()
        cube()
    elif choice=='2':
        def fahernheit(c):
            return (c*9/5)+32
        c=int(input("Enter celcius temp :"));
        print("the fahernheit temp =",fahernheit(c))

        def celcius(f):
            return (f-32)*5/9
        f=int(input("Enter fahernheit temp :"));
        print("the celcius temp =",celcius(f))

    else:
        print("invalid choice ")
        print()
