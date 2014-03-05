'''
Lyteia Kitchen
3/4/14
Day One
'''
'''
name = raw_input("Enter Your Name")
print name + " Very nice to meet you"
'''
# for single line comment
#Expressions
'''
yearBorn = 1990
currentYear= 2014
age = currentYear - yearBorn
print age
'''
#Conditionals
#budget = 300
#if budget > 200 :
    #stuff would wanna do if true
    #if no line of code in here use pass(if you have an empty conditiona and need ti ignore it)
    #print "you can buy a pair of Jordans"
#else:

#elif budget > 30:
    #print "you can buy shoes from payless"

#Functions
'''
 def calcArea(h,w):
     a = h * w
     return a

height = 40
width = 30

area = calcArea(height, width)
print "Your area is:" + str(area)
'''

#ARRAYS
students = ["Jario", "Austin", "Bryan", "Samantha"]

#Dictionaries - associative arrays

villains = dict()
villains = {"Star Wars": "Darth Vader", "Lion King": "Scar", "Silence of The Lambs": "Hannibal"}

#print villains["Star Wars"]
#print students[1:3]

#LOOPS
x = 100
for i in range(1,100):#Sets a range of 1 up to, not to include 100
    x-=1
    #print "There are " + str(x) + " number of beer on the wall"
    pass

for s in students:
    #print s
    pass

#FORMAT METHOD FOR BIG STRINGS
your_name = "Lyte"
real_age = 23
message = '''
{your_name}, thanks for joining us you are great! You are awesome! Thumbs Up !
You are {real_age} years old. That's great.
Sincerely ,
    People who cant spell
'''

message = message.format(**locals())
print message
import random
for y in range (0,100):
    print random.randrange(2,9)










