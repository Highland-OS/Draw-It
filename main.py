from turtle import *
from random import *
import turtle
import time

turtle.pensize(5)
 
def drawUp():
    turtle.seth(90)
    turtle.fd(20)

def drawDown():
    turtle.seth(270)
    turtle.fd(20)

def drawLeft():
    turtle.seth(180)
    turtle.fd(20)

def drawRight():
    turtle.seth(0)
    turtle.fd(20)

def colourRed():
    turtle.color('red')

def colourGreen():
    turtle.color('green')

def colourBlue():
    turtle.color('navy')

def colourWhite():
    turtle.color('white')

listen()
turtle.onkey(drawUp,'Up')
turtle.onkey(drawDown,'Down')
turtle.onkey(drawLeft,'Left')
turtle.onkey(drawRight,'Right')

turtle.onkey(colourRed,'r')
turtle.onkey(colourGreen,'g')
turtle.onkey(colourBlue,'b')
turtle.onkey(colourWhite,'w')
