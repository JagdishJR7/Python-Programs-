#2,change fahrenheit to celcius and vice versa:
def fahernheit(c):
    return (c*9/5)+32
def celcius(f):
    return (f-32)*5/9
c=int(input("Enter celcius temp :"));
print("the fahernheit temp =",fahernheit(c))

f=int(input("Enter fahernheit temp :"));
print("the celcius temp =",celcius(f))
