from re import A
import turtle
import time

from cv2 import circle

time.sleep(1)
t = turtle.Turtle()
t.hideturtle()
t.screen.bgcolor("light blue")

t.speed(0)

t.hideturtle()
t.setheading(-60)
t.fd(100)
t.home()
t.setheading(-120)
t.fd(100)
t.home()
t.left(90)
t.fd(100)


t.setheading(-60)
t.fd(50)
t.setheading(220)
t.fd(57)
t.setheading(-360)
t.circle(4,360)
t.penup()
t.home()
t.setheading(90)
t.fd(100)
t.pendown()

t.setheading(220)
t.fd(50)
t.setheading(290)
t.fd(50)
t.penup()
t.home()
t.setheading(90)
t.fd(100)
t.pendown()

t.setheading(360)
t.circle(40)

t.setheading(90)
t.penup()
t.fd(35)
t.pendown()
t.fd(5)

t.penup()
t.fd(10)
t.setheading(360)
t.fd(12)
t.pendown()
t.circle(5)

t.penup()
t.backward(24)
t.pendown()
t.circle(5)

t.penup()
t.home()
t.setheading(90)
t.fd(118)
t.pendown()
t.setheading(360)
t.fd(10)
t.backward(20)



t.penup()
t.home()
t.setheading(90)
t.fd(5)
t.pendown()

t.setheading(135)
t.fd(40)
t.circle(2,190)

t.penup()
t.home()
t.setheading(90)
t.fd(5)
t.pendown()

t.setheading(135)
t.fd(40)
t.circle(4,540)
t.fd(35)
t.setheading(160)
t.circle(5,240)
t.setheading(290)
t.circle(5,230)



turtle.done()
t.done()