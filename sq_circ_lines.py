#c_g_7.py : Draw a Square having length of one side=500. Connect two diagonals.
#Draw 4 concentric circles at 4 corners of the square
from graphics import *
win = GraphWin('My Graphics Window', 700, 700) # specifies graphics window size 800x800
win.setBackground("#ffff00")
#Defining 2 end points of square
P1=Point(100,100)
P2=Point(600,600)
P3=Point(600,100)
P4=Point(100,600)
C1=Point(350,350)
g1=Rectangle(P1,P2) # Defining object for Drawing Square of side length=500
g1.draw(win)
g1.setWidth(15)
g1.setOutline("#000000")
 
#To Draw Diagonal from P1 to P2
g2=Line(P1,P2)
g2.draw(win)
g2.setWidth(15)
g2.setFill("#000000")
 
#To Draw Diagonal from P3 to P4
g3=Line(P3,P4)
g3.draw(win)
g3.setWidth(15)
g3.setFill("#000000")
 
#To Draw circles at different corners
radius=40
g4=Circle(P1,radius)
g4.draw(win)
g4.setWidth(15)
g4.setFill("#ff0000")
g4.setOutline("#000000")
 
g5=Circle(P2,radius)
g5.draw(win)
g5.setWidth(15)
g5.setFill("#ff0000")
g5.setOutline("#000000")
 
g6=Circle(P3,radius)
g6.draw(win)
g6.setWidth(15)
g6.setFill("#ff00ff")
g6.setOutline("#000000")
 
g7=Circle(P4,radius)
g7.draw(win)
g7.setWidth(15)
g7.setFill("#ff00ff")
g7.setOutline("#000000")
 
g8=Circle(C1,radius)
g8.draw(win)
g8.setWidth(15)
g8.setFill("#00ffff")
g8.setOutline("#000000")
 
win.getMouse() # keep window up
win.close()
