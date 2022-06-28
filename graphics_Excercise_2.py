from ezgraphics import GraphicsImage, GraphicsWindow
from math import trunc

#Use the image (IMG_1065_Scoobert.gif)
image = GraphicsImage("IMG_1065_Scoobert.gif")

#Establish width and height
width = image.width()
height = image.height()

#Get the values of each color in the picture
for row in range(height):
    for col in range(width):
        red = image.getRed(row, col)
        green = image.getGreen(row, col)
        blue = image.getBlue(row, col)
        
        #Alter the red value of the image by adding 30% more red
        if red + (red * 0.3) <= 255:
            newRed = trunc(red + (red * 0.3))
        
        #If the red value of the picture plus 30% more is greater than 255 than set the red at the accepted maximum of 255
        else:
            newRed = 255

        #Set the modified colors        
        image.setPixel(row, col, newRed, green, blue)

#Draw the image
win = GraphicsWindow()
canvas = win.canvas()
canvas.drawImage(image)
win.wait()
