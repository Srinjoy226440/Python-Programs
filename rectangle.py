#c_g_4.py : Display Rectangle   on screen
from graphics import *
 
win = GraphWin('My Graphics Window', 1000, 800) # specifies graphics window size1000x800
win.setBackground("#ffff00")
P1= Point(50,50) # Defining top leftmost point object P1 at (50,50)
P2=Point(950,550) # Defining right nottom most object P2 at (950,550)
g = Rectangle(P1,P2)
g.draw(win) # To draw a Rectangle 
g.setWidth(10)
g.setFill("#ff0000")
g.setOutline("#00ff00") # To change color of line drawing rectangle
 
P3=Point(100,100)
P4=Point(900,500)
g1=Rectangle(P3,P4)
g1.draw(win) # Drawing 2nd rectangle
g1.setWidth(10)
g1.setFill("#00ff00")
g1.setOutline("#ff00ff") # To change color of line drawing rectangle
 
P5=Point(150,150)
P6=Point(850,450)
#g2=Rectangle(P5,P6)
#g2.draw(win) # Drawing 2nd rectangle
#g2.setWidth(10)
#g2.setFill("#0000ff")
#g2.setOutline("#ff0000") # To change color of line drawing rectangle
 
P7=Point(200,200)
P8=Point(800,400)
g3=Rectangle(P7,P8)
g3.draw(win) # Drawing 3rd rectangle
g3.setWidth(10)
g3.setFill("#ff00ff")
g3.setOutline("#ffffff") # To change color of line drawing rectangle
 
P9=Point(250,250)
P10=Point(750,350)
g4=Rectangle(P9,P10)
g4.draw(win) # Drawing 4th rectangle
g4.setWidth(10)
g4.setFill("#00ff00")
g4.setOutline("#000000") # To change color of line drawing rectangle
win.getMouse() # keep window up
win.close()
