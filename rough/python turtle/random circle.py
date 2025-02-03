from multiprocessing import Condition
import turtle
import time
import random


time.sleep(1)

test = turtle.Turtle()

turtle.colormode(255) #color mode

#test.speed(1) #for speed
test.screen.bgcolor("yellow")
test.color("grey")
# test.hideturtle()
test.shape("classic")
test.shapesize(2)
# test.screen.bgpic("1.pnj")
# test.setheading(90) #values in degree,for change the direction

# test.left(200)  #value in degree
# test.right(200) #value in degree

# test.write("hello")

# test.pensize(10)
# test.backward(20)
# test.pencolor('green')
# test.penup()
# test.pendown()

# test.home()  #for goto the default location
# test.goto(100,200)  #for custom location

#clr = ['green','red','white','black','yellow','grey','purple','blue']
#l = random.choice(string.ascii_letters) #for random a-z
i = 0
while i < 3:
    test.penup()
    i = i+1
    x = random.randint(-300, 250)
    y = random.randint(-300, 250)
    test.goto(x, y)
    test.pendown()
   # c = random.choice(clr)
   # print(c)
    #test.color(c)
    #or
    r = (random.randint(0,255),random.randint(0,255),random.randint(0,255)) #for random color
    test.color(r)
    test.begin_fill()
    test.circle(10)
    test.end_fill()


# test.goto(90,90)
#r = random.randint(0,255)  
#g = random.randint(0,255)  
#b = random.randint(0,255)  



turtle.done()
test.done()
