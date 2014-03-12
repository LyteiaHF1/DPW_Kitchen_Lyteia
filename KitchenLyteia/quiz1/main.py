'''
Lyteia Kitchen
3/11/14
Quiz1
'''
class CalcArea():
    width = 15
    height = 15


def calcArea(w, h):
    area = h * w
    return area

    area = calcArea(height, width)

    if height == width:
        print "The area of your square is" + str(area)+ "square feet."
    else:
        print "The area of your rectangle is" + str(area)+ "square feet."

        height = 40
        width = 20

        area = calcArea(height,width)

class Beer():
    bottle  = 100
    print str(bottle) + "bottles of beer on the wall"+ str(bottle) + "bottles of beer... you take one down pass it around " + str(bottle -1) + "bottles of beer on the wall"
    while bottle > 1:
        bottle -=1
        