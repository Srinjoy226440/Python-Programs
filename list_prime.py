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
    nums1 = list(map(int, input().split()))
    nums2=list(filter(prime,nums1))
    print(nums2)

main()