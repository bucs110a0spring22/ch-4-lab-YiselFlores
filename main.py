import turtle
import math
import time
import datetime 
from datetime import date

def setupWindow(wn=None):
 wn.setworldcoordinates(-360, -2, 360, 2)
  
def setupAxis(myTurtle=None):
 "Sets up 2 line axis "
 "args: Takes a turtle object as a paremeter"
  
 myTurtle.down()
 myTurtle.goto(-360,0)
 myTurtle.goto(360,0)
 myTurtle.up()
 myTurtle.goto(0,-1)
 myTurtle.down()
 myTurtle.goto(0,1)
 myTurtle.up()
 
 



def drawSineCurve(myTurtle = None):
  "Draws a sine curve on the axis"
  "Args: Takes turtle object as parameter"
  myTurtle.color("green")
  myTurtle.up()
  myTurtle.goto(-360,0)
  myTurtle.down()
  for angle in range (-360,360):
   myTurtle.goto(angle,math.sin(math.radians(angle)))
 


def drawCosineCurve(myTurtle=None):
  "Draws a cosine curve on the axis"
  "Args: Takes turtle object as parameter"
  myTurtle.color("red")
  myTurtle.up()
  myTurtle.goto(-360,0)
  myTurtle.down()
  for angle in range (-360,360):
   myTurtle.goto(angle,math.cos(math.radians(angle)))
 


def drawTangentCurve(myTurtle=None):
  "Draws a tangent graph on the axis"
  "Args: Takes turtle object as parameter"
  myTurtle.color("blue")
  myTurtle.up()
  myTurtle.goto(-360,0)
  myTurtle.down()
  for angle in range (-360,360):
   myTurtle.goto(angle,math.tan(math.radians(angle)))

def graphtime(myturtle):
 "Function gives you the date in which the graph was drawn"
 "Args: Takes turtle object as parameter"
 "returns current date"
 today = date.today()
 current_date = today.strftime("%B %d, %Y")
 myturtle.up()
 myturtle.goto(-360,1.5)
 myturtle.down()
 myturtle.write("Drawn on "+ 
 current_date)
 return today

def birthday_count(current_date):
  "Function gives you the months and days passed since the date of the graph drwan and user's bday"
  "Args: a time/or date graph was drawn"
  user_birthday = input("Please enter your birthday in Month m/d/yyyy ")
  birth_date = datetime.datetime.strptime(user_birthday,"%m/%d/%Y").date()
  print("Your birthday day is : "+birth_date.strftime('%B/%d/%Y'))
  delta = abs(birth_date - current_date)
  months =abs(int(delta.days/30))
  print(str(delta.days) + " days and "+str(months)+" months have passed since the date of your birthday to the date this graph was drawn!!" )
 
  

##########  Do Not Alter Any Code Past Here ########
def main():
    #Part A
    
    wn = turtle.Screen()
    wn.tracer(5)
    dart = turtle.Turtle()
    dart.speed(10)
    drawSineCurve(dart)
    today = date.today() 
    #Part B
    setupWindow(wn)
    setupAxis(dart)
    dart.speed(10)
    drawSineCurve(dart)
    drawCosineCurve(dart)
    drawTangentCurve(dart)
    graphtime(dart)
    answer = input("Do you want to how many days and months has passed since your birthdate and the illustration of this graph? ")
    if (answer == "yes"or answer=="yes"):
       birthday_count(today)
  
    wn.exitonclick()
    
main()
