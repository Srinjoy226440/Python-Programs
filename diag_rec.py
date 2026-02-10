#c_g_5.py : Display Rectangle   and connect two diagonals
from graphics import *
win = GraphWin('My Graphics Window', 1000, 600) # specifies graphics window size 300x300
win.setBackground("#ffff00")
P1= Point(50,50) # Defining top leftmost point object P1 at (50,50)
P2=Point(950,50) # Defining right bottom most object P2 at (950,50)
P3=Point(950,550)
P4=Point(50,550)
#C1=Point(120,70)
g = Rectangle(P1,P3)# Drawing Rectangle
g.draw(win) # To draw a Line from P1 to P3
g.setWidth(15)
g.setFill("#ff0000")
#Connecting 1st diagonal
 
g1=Line(P1,P3)
g1.draw(win)
g1.setWidth(15)
g1.setFill("#00ff00")
 
#Connecting 2nd diagonal
g2=Line(P2,P4)
g2.draw(win)
g2.setWidth(15)
g2.setFill("#0000ff")
 
win.getMouse() # keep window up
win.close()
