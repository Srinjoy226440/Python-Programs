#c_g_2.py : Display a circle  on screen
from graphics import *
win = GraphWin('My Graphics Window', 800, 800) # specifies graphics window size 800x800
win.setBackground("#ffff00") # setting back ground color=yellow
P = Point(400,400) # creates a Point object at x=400, y=400
g = Circle(P, 300) # radius=250, Centre at (400,300)
g.draw(win) # To draw a circle
g.setFill("#0000ff") # fill color of circle by red-color
g.setWidth(30) # Set width of line of cicle to 20 pixels
g.setOutline("#00ff00") #Change line color of circle to  green
win.getMouse() # keep window up
win.close()
