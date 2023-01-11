# half of the values in different different line:tuple(a)
t1=(1,2,5,7,9,2,4,6,8,10)
print("the first half :",end="")
print(t1[0:5])
print("the second half :",end="")
print(t1[5:10])

#different line for odd tuples and even tuples:tuple(b)
t2=("Even values :")
for i in range(0,len(t1)):
    if t1[i]%2==0:
        t2 += str(t1[i])
print(t2)

#concatenate:tuple(c)
t2=(11,13,15)
t1 += t2
print(t1)

#maximum and minimum value of tuples:tuple(d)
print(min(t1))
print(max(t1))


