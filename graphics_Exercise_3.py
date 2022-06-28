from ezgraphics import GraphicsImage, GraphicsWindow
from math import trunc

#Use the image (IMG_1065_Scoobert.gif)
image = GraphicsImage("IMG_1065_Scoobert.gif")

#Establish the width and height of the image
width = image.width()
height = image.height()

#Get the pixel colors of the picture
for row in range(height):
    for col in range(width):
        red = image.getRed(row, col)
        green = image.getGreen(row, col)
        blue = image.getBlue(row, col)
        
        #Turn each pixel of the picture gray
        gray = trunc(0.2126 * red) + trunc(0.7152 * green) + trunc(0.0722 * blue)

        #Set each pixel in the picture to its new gray color        
        image.setPixel(row, col, gray, gray, gray)

#Display the image
win = GraphicsWindow()
canvas = win.canvas()
canvas.drawImage(image)
win.wait()
