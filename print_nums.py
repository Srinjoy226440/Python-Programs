def func(n, i):
    if i > n:
        return 
    print(i)
    func(n, i + 1)

def main():
    num = int(input("Enter the number: "))
    func(num, 1) 

main()
