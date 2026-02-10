#q6as2python.py : Write a program to implement Towers of Hanoi algorithm to move
#‘nd’ disks from peg-1 to peg-2 using Peg-3.

def hanoi(p1,p2,p3,nd) :
    global n # n=total number of operations needed to transfer 'nd' disks from Peg-1
    #to Peg-2 using peg-3
    if(nd==1):
        n=n+1
        print("Step#:",n," : Move  Disk-",nd," from Peg-",p1,"  to Peg-",p2)
        return
    hanoi( p1,p3,p2,(nd-1))
    n=n+1
    print("Step#:",n," : Move  Disk-",nd," from Peg-",p1," to Peg-"  ,p2)
    hanoi( p3,p2,p1,(nd-1))
#End of Hanoi() function
#Start main
global n
n=0
nd=int(input("Enter Number of disks to be shiftd from Peg-1 to Peg-2="))
 
p1=1
p2=2
p3=3
hanoi(p1,p2,p3,nd)
print("Total number of operations performed =",n)
