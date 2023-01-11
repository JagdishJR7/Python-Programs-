#2,change fahrenheit to celcius and vice versa:


def func(c):
    x=(c*9/5)+32
    c=int(input("Enter celcius temp :"));
    return x
x=func(c)
print("the fahernheit temp =",x)

def celcius(f):
    y=(f-32)*5/9
    f=int(input("Enter fahernheit temp :"));
    return y
y=celcius(f)
print("the celcius temp =",y)

#2,change fahrenheit to celcius and vice versa:
def fahernheit(c):
    return (c*9/5)+32
c=int(input("Enter celcius temp :"));
print("the fahernheit temp =",fahernheit(c))

def celcius(f):
    return (f-32)*5/9
f=int(input("Enter fahernheit temp :"));
print("the celcius temp =",celcius(f))



