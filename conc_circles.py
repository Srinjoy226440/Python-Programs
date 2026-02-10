#Display  4 Concentric Circles
from graphics import * #type: ignore
win = GraphWin('My Graphics Window', 800, 800) # specifies graphics window size 800x800
win.setBackground("#ffff00")
C1= Point(400,400) # Defining centre of all 4 circles
R1=300
R2=200
R3=100
R4=50
g1=Circle(C1,R1) # Drawing circle having radius=300
g1.draw(win)
g1.setWidth(10)
g1.setFill("#ff0000")
g1.setOutline("#ff00ff")
 
g2=Circle(C1,R2) # Drawing circle having radius=200
g2.draw(win)
g2.setWidth(10)
g2.setFill("#00ff00")
g2.setOutline("#ffffff")
 
g3=Circle(C1,R3) # Drawing circle having radius=100
g3.draw(win)
g3.setWidth(10)
g3.setFill("#0000ff")
g3.setOutline("#ffffff")
 
 
g4=Circle(C1,R4) # Drawing circle having radius=50
g4.draw(win)
g4.setWidth(10)
g4.setFill("#ff0000")
g4.setOutline("0000ff")
 
win.getMouse() # keep window up
win.close()
