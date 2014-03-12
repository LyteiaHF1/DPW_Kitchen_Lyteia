'''
Lyteia Kitchen
3/11/14
Quiz1
'''
def calcArea(w, h):
    #area = h times width
    area = h * w
    #this returns the area
    return area
height = 40
width = 20
area = calcArea(height, width)
    #if height is the same a width
if height == width:
        print "The area of your square is " + str(area)+ " square feet."
else:
        print "The area of your rectangle is " + str(area)+ " square feet."


area = calcArea(height,width)

class Beer():
    bottle  = 100
    print str(bottle) + " bottles of beer on the wall "+ str(bottle) + " bottles of beer... you take one down pass it around " + str(bottle -1) + " bottles of beer on the wall"
    #bottle greater than 1
    while bottle > 1:
        #bottle = -1 (take one away each time)
        bottle -=1
        print str(bottle) + " bottles of beer on the wall "+ str(bottle) + " bottles of beer... you take one down pass it around " + str(bottle -1) + "bottles of beer on the wall"