'''
Lyteia Kitchen
3/4/2014
Lab 1
'''
#Dictionary Set Up
data = dict()

data['name'] = input("Whats your name?:" )
data['school'] = input("What School You Go To?:" )
data['grade_level'] = input("What Grade Are You In?:" )
data['time'] = input("How Many Years You Been Here?:" )
data['grades'] = []

#Get The Grades
for i in range(0,1000000):
    if i == 0:
        grade = input("Grades need to be between 0-4 add # after grades ")
    else:
        grade = input(''' ''')

    if grade == '#':
       break
    else: data['grades'].append(grade) #else add grade to grades
data['type'] = 0
 #for number in data dictionary grades
for number in ['grades']:
 #if number is greater than data['type']
     if number > data['type']:
     #data['type'] equals number
        data['type'] = number
#if data type is equal to  4 data equals A
if data['type']==4:
    data['let']='A'
#if data type is equal to  3 data equals B
elif data['type']==3:
    data['let']='B'
#if data type is equal to  2 data equals C
elif data['type']==2:
    data['let']='C'
#if data type is equal to  1 data equals D
elif data['type']==1:
    data['let']='D'
else:
#Else data equals F
    data['let']='F'
def calcGPA(t,a):
    gpa = t / a
    return gpa

data['gpa'] = 0
amount = 0
total = 0
#for every grade in grades
for g in data['grades']:
#add the g added to the total
    total = total + g
    amount = amount + 1
#gpa = total grades divided by amount
data['gpa'] = total/amount

message = '''
Hey My Name Is {data[name]}, I Am A {data[grade_level]} at {data[school]}, Ive been going here for {data[time]} years.
My GPA Is A {data[gpa]} School i'snt the hardest thing in the world but its not the easiest either !
'''
message = message.format(**locals())
print message