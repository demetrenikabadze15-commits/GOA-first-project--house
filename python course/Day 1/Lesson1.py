from turtle import*


#painting house

#step 1:square
speed(20)
width(5)
color("pink")
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

#door
forward(80)
color("navy blue")
begin_fill()
left(90)
forward(100)
right(90)
forward(40)
right(90)
forward(100)
end_fill()

#roof
penup()
goto(200,200)
pendown()

color("purple")
begin_fill()
right(150)  
forward(200)
left(120)
forward(200)
end_fill()

# left window
width(2)
penup()
goto(30,180)
pendown()

color("light blue")
begin_fill()
left(30)
forward(40)
left(90)
forward(40)

left(90)
forward(40)

left(90)
forward(40)
end_fill()

#right window
penup()
goto(140,180)
pendown()

color("light blue")
begin_fill()
left(90)
forward(40)

left(90)
forward(40)

left(90)
forward(40)

left(90)
forward(40)
end_fill()

exitonclick()