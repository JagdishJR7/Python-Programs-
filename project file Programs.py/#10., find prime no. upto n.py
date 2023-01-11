#printt prime no upto n:
count=0
n=int(input("enter no. upto which you want find primt no."))
print("list of prime no. b/w 1 to",n,":")
for i in range(1,n+1):
    a=i
    count=0
    for j in range(1,a+1):
        if a%j==0:
            count+=1

    if count==2:
        print(a)
