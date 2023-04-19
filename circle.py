import turtle as t
import time
time.sleep(2)
t.bgcolor("black")
t.pensize(2)
t.speed(0)
while True:
    for i in range(6):
        for j in ["#dfff11","#66ff00","#ff08e8","yellow","violet","red"]:
            t.color(j)
            t.circle(60)
            t.left(10)
        
