#q5as2python.py: Write a program to implement recursive call to calculate n-th member
#of a fibonacci series.
def fib(n):
    if(n<=2):
        return 1
    else:
        return fib(n-1)+fib(n-2)
#end of fib(n) function
#Main starts
n1=int(input("Enter Lower limit of fibonacci series="))
n2=int(input("Enter Upper limit of fibonacci series="))
for i in range(n1,(n2+1)):
    f=fib(i)
    print("fib(",i,")=",f)
#End of main
