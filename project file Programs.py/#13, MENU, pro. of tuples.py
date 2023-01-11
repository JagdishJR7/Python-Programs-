#MENU pro. of tuples:
print("1 : half of the value of tuple in one line and half in another line :")
print("2 : find all even values in tuples :")
print("3 : concatenate a tuple t2=(11,12,13) in a given tuple t1 :")
print("4 : return maximum and minimum value from tuple :")
t1=(1,2,3,4,5,6,7,8,9,10)
j=1
while j>0:
    choice=input("enter your choice :")
    if choice=='1':
        print("the first half :",t1[0:5])
        print("second half :",t1[5:10])
        print()
    elif choice=='2':
        for i in t1:
            if t1[i-1]%2==0:
                li.append(t1[i-1])
        t2=tuple(li)
        print(t2,",",end="")
    elif choice=='3':
        t2=(11,12,13)
        t1+=t2
        print(t1)
    elif choice=='4':
        print("max value ",max(t1))
        print("min value ",min(t1))
    else:
        print("invalid choice")
        print()
