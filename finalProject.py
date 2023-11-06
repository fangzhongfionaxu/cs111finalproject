#author:Fiona Xu fx100
#Final Project
from turtle import *
from turtleBeads import *
# color1,2,3
# number of repeats
# largest pensize
# ratio of pensize decrease
with open('input.txt','r') as fr:
    strippedlines=[]
    for line in fr:
        strippedlines.append(line.strip())
colors=strippedlines[:3]
colors=['AliceBlue','DodgerBlue1','navy']
maxsize=2
repeat=5
decreaseRate=2.5
maxradius=5
speed(0)
teleport(-300,50)
pendown()
fd(10)
bk(10)
rt(90)
penup()

def onewave(repeat,colors,maxsize,maxradius):
    '''a function to draw waves of different colors'''
    if repeat>0:
        pendown()
        pensize(maxsize)
        pencolor(colors[0])
        circle(maxradius,180)
        rt(180)
        circle(maxradius,180)
        rt(180)
        colors.append(colors.pop(0))
        onewave(repeat-1,colors,maxsize,maxradius)
        
def waves(lines,decreaseRate,y,repeat):
    '''use recursion to draw multiple waves'''
    teleport(-300,y)
    seth(-90)
    if lines>=0:
        pendown()
        onewave(repeat,colors,maxsize*decreaseRate,maxradius*decreaseRate)
        penup()
        seth(-90)
        setx(-300)
        sety(y)
        pendown()
        waves(lines-1,decreaseRate*1.5,y-40,repeat-1)

def smallboat(h,v):
    '''draw small boat'''
    seth(0)
    penup()
    pensize(1)
    teleport(h,v)
    pendown()
    color('chocolate4')
    begin_fill()
    fd(18)
    rt(120)
    fd(9)
    rt(60)
    fd(9)
    rt(60)
    fd(9)
    end_fill()
# graphic:Waves
# what 'Waves' is going to do 
# three colors consequitivly in each line
# draw semicircles using pen/draw 2 semicircles and filling the middle part in to form curves
# small medium big 
# fill screen
lines=int(input('how many lines of waves do you want?'))
y=int(input('how high do you want your farest wave be?'))
repeat=int(input('how many waves do you want to see?'))
waves(lines,decreaseRate*1.5,y,repeat)

h=int(input('what x axis do you want your small boat at?'))
v=int(input('what y axis do you want your small boat at?'))
smallboat(h,v)