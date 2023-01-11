# program of fibonacci series:1 1 2 3 5 8 11 ...
a=int(input("enter no. upto which you want printt fibonacci series:"))
s1=0
s2=1
print(s1)
print(s2)
for i in range(a-2):
    s3=s1+s2
    s1=s2
    s2=s3
    print(s3)
