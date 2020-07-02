from turtle import *
 
bgcolor("black")
pensize(6) #Set the thickness of the pen to 6
firstRowColors = ["blue", "white", "red"] #firstRowColors is a list of colors that are present in the first row of logo
for i in range(3):
  penup()
  pencolor(firstRowColors[i])
  goto(i*110, 0)
  pendown()
  circle(50)
 
secondRowColors = ["", "yellow", "", "green"]
for i in range(1, 4, 2):
  penup()
  pencolor(secondRowColors[i])
  goto(i*55, -50)
  pendown()
  circle(50)
  
mainloop()
