from ezgraphics import GraphicsWindow

win = GraphicsWindow(600, 600)
win.setTitle("Spiral")

#Declare and initialize coordinate variables
x1 = 500
y1 = 50
y2 = 400
y3 = 100
x2 = 450

#Declare and initialize the spiralFactor variable
#spiralFactor will be used to decrement the original draw coordinates to create the spiral effect
sprialFactor = 0

canvas = win.canvas()

#Original starting coordinates for the outer layer of the spiral
# canvas.drawLine(500, 50, 500, 400)
# canvas.drawLine(500, 400, 50, 400)
# canvas.drawLine(50, 400, 50, 100)
# canvas.drawLine(50, 100, 450, 100)

#The spiralFactor is either subtracted from or added to each coordinate
#The spiral will be drawn while the spiralFactor is less than 200
while sprialFactor < 200:
    #Form the right line of the shape
    canvas.setColor("green")
    canvas.drawLine(x1 - sprialFactor, y1 + sprialFactor, x1 - sprialFactor, y2 - sprialFactor)
    #Form the bottom line of the shape
    canvas.setColor("red")
    canvas.drawLine(x1 - sprialFactor, y2 - sprialFactor, y1 + sprialFactor, y2 - sprialFactor)
    #Form the left line of the shape
    canvas.setColor("blue")
    canvas.drawLine(y1 + sprialFactor, y2 - sprialFactor, y1 + sprialFactor, y3 + sprialFactor)
    #Form the top line of the shape
    canvas.setColor("orange")
    canvas.drawLine(y1 + sprialFactor, y3 + sprialFactor, x2 - sprialFactor, y3 + sprialFactor)
    
    #Update the spiralFactor variable
    sprialFactor = sprialFactor + 50

win.wait()