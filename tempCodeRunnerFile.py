l1=[1,2,2,4,3,3,5,4]
s1=set(l1)
for i in s1:
    print (i)

s1.add(6)
print(s1)
s1.update([7,8,9,10])
print(s1)
s1.discard(10)
print(s1)