from turtle import *
import colorsys

speed(0)
bgcolor("black")
pensize(2)
hideturtle()

h = 0


def rose():
    global h
    for i in range(16):
        for j in range(18):
            c = colorsys.hsv_to_rgb(h, 1, 1)
            pencolor(c)
            h += 0.005

            right(90)
            circle(150 - j * 6, 90)
            left(90)
            circle(150 - j * 6, 90)
            right(180)
            circle(40, 22.5)


def draw_rose(x, y):
    penup()
    goto(x, y)
    setheading(0)
    pendown()
    rose()
draw_rose(0, 0)
draw_rose(-300, 250)
draw_rose(300, 250)
draw_rose(-300, -250)
draw_rose(300, -250)
done()
