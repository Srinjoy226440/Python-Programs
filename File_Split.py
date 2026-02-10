#q2as4python.py: Write a program to split one file into  two(2) output files. 
file1=input("Enter Input File Name=")
file2=input("Enter Output File-1 Name=")
file3=input("Enter Output File-2 Name=")
 
fp1=open(file1,'rb')
fp2=open(file2,'wb')
fp3=open(file3,'wb')
 
data1=fp1.read() # Reading data from any input File
n=len(data1) # n=size of input File
n1=n//2
n2=n-n1
data2=data1[0:n1]  # data2= 1st half of input file
data3=data1[n1:n]  # data3=2nd half of input file
fp2.write(data2) # transferring data2 to file2
fp3.write(data3) # transferring data3 to file3
 
print("File Split is over...")
print("<size of ",file1,">=",n," Bytes")
print("<size of ",file2,">=",n1," Bytes")
print("<size of ",file3,">=",n2," Bytes")
 
fp1.close()
fp2.close()
fp3.close()
