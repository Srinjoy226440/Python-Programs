name=input("Enter any Name=")
name=name.strip() 
n=len(name)
blank=0 
for i in range(-1,(-n-1),-1):
    ch=name[i]
    if(ch==" "):
        blank=i
        break
name1=name[0:blank]
surname1=name[(blank+1):n]
modified_name=surname1+", "+name1
print("Original Name=",name)
print("Modified Name=",modified_name)
#End
