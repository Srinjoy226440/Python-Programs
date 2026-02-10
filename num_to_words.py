#Write a program to input any +ve integer (1-9999999) and convert it 
#into corresponding words.
#[ Example: 3232335 : Thirty Two Lakh Thirty Two Thousand Three Hundred Thirty Five.]
def number_to_words(n):
    a=["Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten",
       "Eleven", "Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen",
       "Nineteen"]
    b=["X","X","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
    m=n
    #To extract digits from Lakh place
    nlkh=n//100000
    if(nlkh>19):
        nlkh1=nlkh//10
        nlkh2=nlkh%10
    else:
        nlkh1=0
        nlkh2=nlkh
    #To extract digits from thousand place
    n=n%100000
    nth=n//1000
    if(nth>19):
        nth1=nth//10
        nth2=nth%10
    else:
        nth1=0
        nth2=nth
    #To extract digit from Hundredth place
    n=n%1000
    nh=n//100
    #To extract digits from tens place and unit place
    n=n%100
    if(n>19):
        nt1=n//10
        nt2=n%10
    else:
        nt1=0
        nt2=n
    #To display number in words
    print(m, ': ',end="")
 
    #To display Lakh order  number
    if(nlkh1!=0 and nlkh2!=0):
        print(b[nlkh1]," ",a[nlkh2]," Lakh ",end='');
    elif(nlkh1!=0 and nlkh2==0):
        print(b[nlkh1]," "," Lakh ",end="")
    elif(nlkh1==0 and nlkh2!=0):
        print(a[nlkh2]," ", " Lakh ", end="")
 
    #To display Thousand  order  number
    if(nth1!=0 and nth2!=0):
        print(b[nth1]," ",a[nth2]," Thousand ",end='')
    elif(nth1!=0 and nth2==0):
        print(b[nth1]," "," Thousand ",end="")
    elif(nth1==0 and nth2!=0):
        print(a[nth2]," ", " Thousand ", end="")
 
    #To display Hundred order number
    if(nh!=0):
        print(a[nh]," Hundred ",end='')
 
    #To display tens place and unit place number
    if(nt1!=0 and nt2!=0):
        print(b[nt1]," ",a[nt2],end='');
    elif(nt1!=0 and nt2==0):
        print(b[nt1],end='')
    elif(nt1==0 and nt2!=0):
        print(a[nt2],end='')
    print()
#End of function
#Main program starts
n1=int(input("Enter Lower limit(1-9999999)="))
n2=int(input("Enter Upper limit(1-9999999)="))
for i in range(n1,(n2+1)):
    number_to_words(i)
#End of main   
