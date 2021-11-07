import os
import turtle
import tkinter as TK

text= open("text.txt")

lines=input ("Number of lines (from 100 to 1000): ")
if lines.isdigit()==False:
    lines=750
    linesnumber=lines
else:
    linesnumber=int(lines)
    if linesnumber<100:
        linesnumber=100
    if linesnumber>1000:
        linesnumber=1000

direction=input("Direction (left=1, right=2): ")
if direction.isdigit()==False:
    direction=1
    directioncode=direction
else:
    directioncode=int(direction)
    if directioncode<1:
        directioncode=1
    if directioncode>2:
        directioncode=2
        
turtle.setup (width=640, height=480, startx=0, starty=0)
turtle.speed(0)
        
for pixels in range (1,linesnumber):
    char=text.read(1)
    if char=='':
        text.seek(0,0)
    else:
        asciicode=ord(char)
        if directioncode==1:
            turtle.forward(asciicode)
            turtle.left(asciicode)
        else:
            turtle.forward(asciicode)
            turtle.right(asciicode)
    if turtle.xcor()>320 or turtle.xcor()<-320:
        turtle.setx(0)
    if turtle.ycor()>240 or turtle.ycor()<-240:
        turtle.sety(0)

text.close
TK.mainloop()
    
    
