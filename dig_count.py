def count(n):
    c=0
    while(n>0):
        n//=10
        c+=1
    return c
def main():
    num=int(input("Enter the number: "))
    ans=count(num)
    print("Length: ",ans)

main()
