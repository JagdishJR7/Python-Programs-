#table to find value of sin(x),cos(x),tan(x):
from math import*
n=int(input("enter the no.:"))
for i in range(0,n+1):
    x=i*(pi/4)
    print("sin","(",x,")","n",sin(x))
    print("cos","(",x,")","n",cos(x))
    print("tan","(",x,")","n",tan(x))
