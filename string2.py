str1=input("Enter a sentence: ")
str1=str1.lower()
s1=str1.split()
s2=[]
seen=set()
flag=0
for word in s1:
    if word in seen:
        flag=1
    else:
        seen.add(word)
        s2.append(word)

print(s2)