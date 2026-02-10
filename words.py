#q8as3python.py: Input any sentence and extract all words from that sentence and display   
#those words on screen.
#(Lord),Jesus+(Christ)&&Son(of))God.
#Here the words are "lord","Jesus","Christ","Son","of","God".
s=input("Enter any sentence=")
n=len(s) # n=length of given sentence
flag=1 # flag=1 means we hit the first alphabet of any word and after that value of flag=0
nw=0 # nw=number of words in s
for i in range(0,n):
    ch=s[i]
    ch1=ch.upper() # converting lowercase alphabet to upper case
    if(ch1>='A' and ch1<='Z'):
        if(flag==1):
            nw=nw+1
            flag=0
        print(ch,end="")
    elif(flag==0):
        flag=1
        print()
if(flag==1):
    print()
    flag=0
print("Number of words found=",nw)
#end
