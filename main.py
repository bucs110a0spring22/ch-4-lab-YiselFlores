import turtle
import math

def setupWindow(window=None):
 window.setworldcoordinates(-360, -2, 360, 2)
  
def setupAxis(myTurtle=None):
 myTurtle.down()
 myTurtle.goto(-360,0)
 myTurtle.goto(360,0)
 myTurtle.up()
 myTurtle.goto(0,-1)
 myTurtle.down()
 myTurtle.goto(0,1)
 myTurtle.up()
 



def drawSineCurve(myTurtle = None):
  myTurtle.color("green")
  myTurtle.up()
  myTurtle.goto(-360,0)
  myTurtle.down()
  for angle in range (-360,360):
   myTurtle.goto(angle,math.sin(math.radians(angle)))
 


def drawCosineCurve(myTurtle=None):
  myTurtle.color("red")
  myTurtle.up()
  myTurtle.goto(-360,0)
  myTurtle.down()
  for angle in range (-360,360):
   myTurtle.goto(angle,math.cos(math.radians(angle)))
 


def drawTangentCurve(myTurtle=None):
  myTurtle.color("blue")
  myTurtle.up()
  myTurtle.goto(-360,0)
  myTurtle.down()
  for angle in range (-360,360):
   myTurtle.goto(angle,math.tan(math.radians(angle)))



##########  Do Not Alter Any Code Past Here ########
def main():
    #Part A
    wn = turtle.Screen()
    wn.tracer(5)
    dart = turtle.Turtle()
    dart.speed(10)
    drawSineCurve(dart)

    #Part B
    setupWindow(wn)
    setupAxis(dart)
    dart.speed(10)
    drawSineCurve(dart)
    drawCosineCurve(dart)
    drawTangentCurve(dart)
    wn.exitonclick()
main()
