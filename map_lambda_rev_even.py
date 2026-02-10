nums=list(map(int,input("Enter the numbers: ").split()))
res=list(map(lambda x: int(str(x)[::-1])if x % 2 ==0 else x,nums))
print(res)
