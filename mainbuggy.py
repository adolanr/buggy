#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
painter = trtl.Turtle()
painter.pensize(40)
painter.circle(20)
legamount = 10
leglength = 200
legdistanceapart = 5000 / legamount
painter.pensize(5)
n = 0
while (n < legamount):
  painter.goto(0,0)
  painter.setheading(legdistanceapart*n)
  painter.forward(leglength)
  n = n + 1

painter.penup()

painter.goto(-10,50)

painter.color("white")

painter.pendown()

painter.circle(5)

painter.penup()

painter.goto(10,50)

painter.pendown()

painter.circle(5)

painter.hideturtle()
wn = trtl.Screen()
wn.mainloop()