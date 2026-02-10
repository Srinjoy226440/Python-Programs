#q1as4python.py:Write a program in python to copy content of one input file to one output  file.  
filein=input("Enter Input File Name=")
fileout=input("Enter Output File Name=")
fp1=open(filein,'rb')
fp2=open(fileout,'wb')
data1=fp1.read() # Reading data from any input File
n=len(data1) # n=size of input File
fp2.write(data1) # Transferring data from memomy to output file
print("File Copy is over...")
print("<size of ",filein,">=",n," Bytes")
fp1.close()
fp2.close()
