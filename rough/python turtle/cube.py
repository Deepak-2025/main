import turtle
import time

time.sleep(1)
t = turtle.Turtle()
t.hideturtle()
t.screen.bgcolor("light blue")
t.pensize(4)

t.penup()
t.setheading(180)
t.fd(100)
t.pendown()

t.setheading(90)
t.fd(100)

t.setheading(360)
t.fd(200)

t.setheading(270)
t.fd(200)

t.setheading(360)
t.backward(200)

t.setheading(90)
t.fd(200)

t.home()

t.setheading(360)
t.fd(200)

t.setheading(270)
t.fd(200)

t.setheading(360)
t.backward(200)

t.setheading(90)
t.fd(200)
t.setheading(90)
t.backward(200)

t.setheading(135)
t.fd(141)
t.setheading(360)
t.fd(200)
t.setheading(315)
t.fd(141)
t.setheading(90)
t.fd(200)
t.setheading(135)
t.fd(141)


turtle.done()
t.done()