#freq.py: Write a program to store ‘n’ arbitrary integers in a list a[].
#Calculate the frequency of all number and display all distinct numbers and
#its corresponding  frequency.
def frequency(a,f):
    n=len(a)
    for i in range(0,n):
        for j in range(0,n):
            if(a[i]==a[j]):
                f[i]=f[i]+1
    display(a,f) # To display all distinct frequencies
#End of freqency() function
def display(a,f):
    n=len(a)
    print("Number\t Frequency")
    print(a[0],'\t ',f[0])
    for i in range(1,n):
        flag=1
        for j in range(0,i):
            if(a[i]==a[j]):
                flag=0
                break
        if(flag==1):
            print(a[i],'\t',f[i])
# End of display Function
a=[]
f=[0]*20
n=int(input("Enter size of your list(1-10)="))
print("Enter ",n," elements one by one--->")
for i in range(0,n):
    print("a[",i,"]=",end="")
    x=int(input(""))
    a+=[x]
frequency(a,f)
#End of main
