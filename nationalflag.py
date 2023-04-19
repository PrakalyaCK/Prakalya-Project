import turtle as t
t.speed(0)
t.pensize(5)
t.color("#054187")
def draw(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    
for i in range(24):
    t.forward(80)
    t.backward(80)
    t.left(15)
draw(0,-80)
t.circle(80,360)
t.color("green")
t.begin_fill()
t.forward(350)
t.right(90)
t.forward(200)
t.right(90)
t.forward(700)
t.right(90)
t.forward(200)
t.end_fill()
t.color("orange")
t.begin_fill()
draw(-350,80)
t.right(90)
t.forward(700)
t.left(90)
t.forward(200)
t.left(90)
t.forward(700)
t.left(90)
t.forward(200)
t.end_fill()

     


