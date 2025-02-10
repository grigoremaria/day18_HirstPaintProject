import turtle
from turtle import Turtle, Screen
#keyword - module name - keyword - thing in Module
import random
#import everything (from ... import *)

# import turtle as t
# #keyword - module name - keyword - alias name
# tommy = t.Turtle()

# import heroes #installing a package is stored local
# print(heroes.gen())


# tim = turtle.Turtle() #module_name.class when we say import turtle
tim = Turtle() #creating object from class when we say from ... import...
#
# tim.shape("turtle")
# tim.color("red")

# draw a square
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

#draw a dashed line
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

#draw a triangle, square, pentagon, etc... decagon random colour
# colours = ["black", "red", "green", "blue", "dark red", "cadet blue"]
# def draw_shape(number_of_sides):
#     angle = 360 / number_of_sides
#     for _ in range (number_of_sides):
#         tim.forward(100)
#         tim.right(angle)
#
# for shape_side_n in range(3,11):
#     tim.color(random.choice(colours))
#     draw_shape(shape_side_n)

#draw a random walk
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# tim.speed("fast")
# tim.pensize(15)
# angle = [0, 90, 180, 270]
#
# for _ in range(200):
#     tim.color(random.choice(colours))
#     tim.forward(30)
#     tim.setheading(random.choice(angle))

#generate a random RGB colours
# #(1, 3, 8) = python tuples (tuples are inmutable, they are constant)
# turtle.colormode(255)
#
# def random_colour():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_colour = (r,g,b)
#     return random_colour
#
# tim.speed("fastest")
# tim.pensize(15)
# angle = [0, 90, 180, 270]
#
# for _ in range(100):
#     tim.color(random_colour())
#     tim.forward(30)
#     tim.setheading(random.choice(angle))

#draw a spirograph
turtle.colormode(255)
def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r, g, b)
    return colour

tim.speed("fastest")

def draw_spirograf(size_of_gap):

    for _ in range(int(360/ size_of_gap)):
        tim.color(random_colour())
        tim.circle(100)
        tim.setheading(tim.heading() + 10)

draw_spirograf(5)

screen = Screen()
screen.exitonclick()