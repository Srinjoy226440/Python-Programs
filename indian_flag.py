from graphics import *
win=GraphWin("Indian National Flag", 1200,800)
win.setBackground("#ff00ff") # Changing Background color of main canvas 
label=Text(Point(600,20),"Indian National Tri color Flag") # To display a label in canvas
label.setSize(30) # setting fontsize=30
label.setTextColor("#0000ff") # setting font color=blue
label.draw(win) # Drawing label in canvas
#To draw a rectangle
p1=Point(200,50)
p2=Point(1000,50)
p11=Point(200,250)
p22=Point(1000,250)
p111=Point(200,450)
p222=Point(1000,450)
p4=Point(200,650)
p3=Point(1000,650)
rect1=Rectangle(p1,p22) # Drawing rectangle
rect1.setWidth(10)
rect1.setOutline("#000000")
rect1.setFill("#FF6820")  # or color code="FF671F"
rect1.draw(win) # To draw 1st rectangle
 
rect2=Rectangle(p11,p222)
rect2.setWidth(10)
rect2.setOutline("#000000")
rect2.setFill("#ffffff")
rect2.draw(win) # Drawing 2nd rectangle
 
rect3=Rectangle(p111,p3)
rect3.setWidth(10)
rect3.setOutline("#000000")
rect3.setFill("#138808") # Color code of green is #046A38 or #138808
rect3.draw(win) # Drawing 3rd rectangle
 
#To draw a circle inside the flag
circle1=Circle(Point(600,350),90)
circle1.setWidth(10)
circle1.setOutline("#000000")
circle1.draw(win) # Drawing circle inside the Flag
 
# To draw 2 lines inside circle
line1=Line(Point(510,350),Point(690,350))
line1.setWidth(10)
line1.setOutline("#000000")
line1.draw(win) # Drawing horizontal line in the circle
 
# To draw 2 lines inside circle
line1=Line(Point(600,250),Point(600,450))
line1.setWidth(10)
line1.setOutline("#000000")
line1.draw(win) # Drawing horizontal line in the circle
input("Press Enter to exit...")
