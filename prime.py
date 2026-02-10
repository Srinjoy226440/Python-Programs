def prime(n):
    c=0
    for i in range(1,n+1):
        if(n%i==0):
            c+=1
    if(c==2):
        return True
    else:
        return False

def main():
    n=int(input("Enter the number: "))
    a=prime(n)
    if(a==True):
        print(n,"is Prime")
    else:
        print(n,"is Composite")

main()