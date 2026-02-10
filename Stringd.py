#q67as3python.py : Write a program in Python to input any sentence. Calculate and
#print (i) number of vowels, (ii) no of consonants, (iii) no of alphabets in that sentence.
def nvowel(s):
    s1=s.upper() # To convert all alphabets to capital letters
    nov=0 # nov=number of vowels
    n=len(s)
    for i in range(0,n):
        ch=s1[i]
        if(ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U'):
            nov=nov+1
    return nov
#End nvowel(s) function
def nalphabet(s):
    s1=s.upper()
    noa=0
    n=len(s)
    for i in range(0,n):
        ch=s1[i]
        if(ch>='A' and ch<='Z'):
            noa=noa+1
    return noa
#End of nalphabet(s) function
def nconsonant(s):
    noc=nalphabet(s)-nvowel(s)
    return noc
#End of nconsonant(s) function
#Main program starts
s=input("Enter any sentence=")
nv=nvowel(s)
nc=nconsonant(s)
na=nalphabet(s)
print("Your sentence=",s)
print("No of Vowels=",nv)
print("No of Consonants=",nc)
print("No of  Alphabets=",na)
#End of main
