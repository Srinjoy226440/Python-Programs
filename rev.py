def rev(n):
    r=0
    while(n!=0):
        d=n%10
        r=r*10+d
        n//=10
    return r

def main():
    num=int(input("Enter the number: "))
    reverse=rev(num)
    print(reverse)

main()