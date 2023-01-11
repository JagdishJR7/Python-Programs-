#program to print fibonacci series :
n=int(input("enter the no. of terms :"))
s1=0
s2=1
print(s1)
print(s2)
for i in range(n-2):
    s3=s1+s2
    s1=s2
    s2=s3
    print(s3)

#fibonacci series:
m=int(input("enter the number :"))
a=0
b=1
c=0
while (c<=m):
     print(c)
     c=a+b 
     a=b
     b=c

