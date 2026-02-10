#linear.py : Write a program to seacr a number in a list using Linear Search
#algorithm
def linear_search(a,num):
    n=len(a) # n=size of list a[]
    ncount=0 # ncount=number of times 'num' found in a[]
    for i in range(0,n):
        if(num==a[i]):
            ncount=ncount+1
            print(num, " found at position= ",i)
    return ncount
#End of linear_search() function
a=[]
n=int(input("Enter size of your list(1-10)="))
print("Enter ",n," elements one by one--->")
for i in range(0,n):
      print("a[",i,"]=",end="")
      x=int(input(""))
      a+=[x]
num=int(input("Enter Number to be searched="))
nc=linear_search(a,num)
if(nc!=0):
    print("Number of times ",num," found=",nc)
else:
    print("Sorry! ",num," not found..")
#end
