#,Mathmatical table:
def func(n):
   for i in range(1,11):
       print(n,"x","-",n*i)
   return(n)
n=int(input("enter the number :"))
func(n)

#
def func(n):
   for i in range(1,5):
       print(n,"x","-",n*i)
       print(n,"x","=",n/i)
       print(n,"x","-",n+i)
       print(n,"x","=",n-i)
   return(n)
n=int(input("enter the number :"))
func(n)
