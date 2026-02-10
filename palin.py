#q2s3python.py : Write a program in python to test whether word/sentence is
#plaindrome or not a palindrome.
# example: suppose s="Madam", Here s is a Palindrome
def palindrome(x):
    n=len(x)
    xcap=x.upper() # To convert all alphabets to capital letters
    flag=1 # flag=1 means the string palindrome and if flag=0 then x is not a palindrome
    left=0
    right=n-1
    while (left < right):
        ch1=xcap[left]
        ch2=xcap[right]
        if (ch1 !=ch2):
            flag=0
            break
        else:
            left=left+1
            right=right-1
    return flag
######################################
 
#Main progrm starts
s=input("Enter any sentence=")
flag=palindrome(s)
 
if(flag==0):
       print(s," is not a Palindrome")
else:
      print(s,"is a Palindrome")
#End
