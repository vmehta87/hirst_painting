import colorgram
import turtle as turtle_module
import random

t1 = turtle_module.Turtle()
t1.shape('turtle')
turtle_module.colormode(255)
t1.penup()
t1.speed('fastest')

colors = colorgram.extract('image.jpg', 30)
rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)
print(rgb_colors)
kept_colors = [(229, 249, 73), (229, 237, 253), (67, 252, 194), (17, 184, 82), (19, 15, 96), (218, 153, 94),
               (74, 37, 23), (94, 1, 56), (59, 4, 180), (247, 102, 203), (28, 245, 41), (248, 21, 135), (168, 3, 123),
               (6, 99, 40), (100, 179, 5), (50, 15, 253), (106, 172, 243), (172, 92, 13), (11, 92, 180), (64, 114, 247),
               (183, 183, 250), (183, 2, 1), (249, 21, 18), (53, 98, 1), (76, 248, 252), (4, 181, 187), (19, 151, 58)]


def cycle():
    for num in range(10):
        t1.dot(20, random.choice(kept_colors))
        t1.forward(50)
    t1.left(90)
    t1.forward(50)
    t1.left(90)
    t1.forward(50)
    for num in range(10):
        t1.dot(20, random.choice(kept_colors))
        t1.forward(50)
    t1.right(90)
    t1.forward(50)
    t1.right(90)
    t1.forward(50)


t1.setposition(-230, -230)
for i in range(5):
    cycle()

screen = turtle_module.Screen()
screen.exitonclick()
