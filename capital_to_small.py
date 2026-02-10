#q7bas4python.py:  Write a program to convert all capital letters to small letters in
#any program. / Any  text file.
file1=input("Enter Input File Name=")
file2=input("Enter Output File Name=")
fp1=open(file1,'r')
fp2=open(file2,'w')
data1=fp1.read()
data2=data1.lower()
fp2.write(data2)
fp1.close()
fp2.close()
print("File conversion is over")
#End
