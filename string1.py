def main():
    word=input("Enter the word: ")
    n=len(word)
    c=0
    for i in range(n):
        sub=word[i:n]
        if(rev_check(sub)==sub):
            print(sub)

def rev_check(s):
    r_s=s[::-1]
    return r_s

main()