#q8as4python.py: Write a program to extract words from any text file and store in another
#file. Display all words on screen and finally print number of words in that file.
file1=input("Enter Input File Name=")
file2=input("Enter Output File Name=")
fp1=open(file1,'r')
fp2=open(file2,'w')
data1=fp1.read()
n=len(data1)
flag=1 # flag=1 when we hit 1st alphabet of a valid word
nw=0 # nw=number of words in input file
for i in range(0,n):
    ch=data1[i]
    ch1=ch.upper()
    if(ch1>='A' and ch1<='Z'):
        if(flag==1):
            nw=nw+1
            flag=0
        print(ch,end="")
        fp2.write(ch)
    elif(flag==0):
        flag=1
        print()
        fp2.write("\n")
print("Total number of words extracted=",nw)
fp1.close()
fp2.close()
#End
