from turtle import *


#we want to paint a house

#step  1: drwa a square

width(8)
color("purple")
begin_fill()

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square

#start of door


forward(70)
left(90)
color("yellow")
begin_fill()
forward(120)   #height of door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

#end of door

penup()
goto(200, 200)
pendown()

color("orange")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
left(25)
forward(100)
left(95)
forward(60)
left(90)
pendown()
color("blue")
begin_fill()
forward(50)
left(90)
forward(40)
left(90)
forward(50)
left(90)
forward(40)
end_fill()

exitonclick()