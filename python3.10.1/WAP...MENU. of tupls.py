#menu of tuples:
import math
print(" a : print half the value of tuples in one one line and other half in next line")
print(" b : print another tuple whose values are even values of the given tuple")
print(" c : concatenate a tuples t2=(11,13,15) with given tuple t1 ")
print(" d : return maximum and minimum values from this  tuple ")
t1=(1,2,5,7,9,2,4,6,8,10)
li=list()
j=1
while j>0:
    choice=input("Enter your choice :")
    if choice=='a':
        print()
        print("the first half :",end="")
        print(t1[0:5])
        print("the second half :",end="")
        print(t1[5:10])
        print()
    elif choice=='b':
        print()
        print("the even values of t1 are :",end="")
        for i in t1:
            if t1[i-1]%2==0:
                li.append(t1[i-1])
        t2=tuple(li)
        print(t2,",",end="")
        print()
    elif choice=='c':
        t2=(11,13,15)
        print("the concatenate result of t1 with t2 is : ",end="")
        print(t1+t2)
        print()
    elif choice=='d':
        print(min(t1))
        print(max(t1))
        print()
    else:
        print(" Wrong choice !!")
        print()
              
        
