#32,program of fibonacci series: 1,1,2,3,5,8,12.....
n=int(input("Enter Number upto which you want print series :"))
x=1
y=0
z=1
while(z<=n):
    print(z)
    x=y
    y=z
    z=x+y
