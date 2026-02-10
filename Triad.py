#q4as2python.py : Write a program in python to display all 3 digits Triad numbers (n1,n2,n3)
#where n2=2*n1 and n3=3*n1 and n1,n2,n3 contain all digits(1,2,3,4,5,6,7,8,9). (
#Example: (192,384,576) is Triad number.
for i in range(123,330):
    n1=i
    n2=2*i
    n3=3*i
    n=1
    #Extract all digits from n1,n2,n3
    a=[0]*10 # defining a list a[] which contains 10 0-s.
    #Extracting digits from n1
    while(n1 !=0):
        d=n1%10
        a[n]=d
        n=n+1
        n1=n1//10
    #Extracting digits from n2
    while(n2 !=0):
        d=n2%10
        a[n]=d
        n=n+1
        n2=n2//10
#Extracting digits from n3
    while(n3 !=0):
        d=n3%10
        a[n]=d
        n=n+1
        n3=n3//10
#Testing for '0' digit in a[]
    flag=1
    for j in range(1,10):
        if(a[j]==0):
            flag=0
            break
    if(flag==1):
        #To test duplicate digits in a[]
        for j in range(1,10):
            for k in range(1,10):
                if(a[j]==a[k] and j!=k):
                    flag=0
                    break
            if(flag==0):
                break
        if(flag==1):
            print("Triad number =(",i,",",2*i,",",3*i,")")
