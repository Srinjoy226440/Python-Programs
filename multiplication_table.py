#waf for an integer which prints its multiplication table uptil 10.
def mul_tab(n):
    for i in range(1,11):
        print(n,"*",i," = ",n*i)

def main():
    num=int(input("Enter the number: "))
    mul_tab(num)

main()