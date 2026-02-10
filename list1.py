l1 = [1,2,4,3,2,2,1]
n=len(l1)
flag=0
for i in range(0,n,1):
    num=l1[i]
    for j in range(i+1,n,1):
        if(num==l1[j]):
            print("TRUE")
            flag=1
            break
    if(flag==1):
        break
    else: 
        continue

if(flag==0):
    print("FALSE")
