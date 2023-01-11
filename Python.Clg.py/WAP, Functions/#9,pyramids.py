#9,star pattern:
def func(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if j>=i:
                print("*",end=' ')
            else:
                print(" ",end=' ')
        print()
    
n=int(input("enter  the number of rows:"))
func(n)
#9,pyramids:
def func():
    for i in range(1,5):
        for j in range(1,8):
            if j>=5-i and j<=3+i :
                print("*",end=' ')
            else:
                print(" ",end=' ')
        print()
func()
