import turtle
turtle.up()
turtle.goto(-300,-200)
turtle.down()
turtle.color("darkgreen","darkgreen")
turtle.speed(3)
turtle.hideturtle()


def board():
    for i in range(4):
        turtle.forward(500)
        turtle.left(90)

def vr():
    turtle.up()
    turtle.forward(167)
    turtle.down()
    turtle.left(90)
    turtle.forward(500)
    turtle.right(90)
    turtle.up()
    turtle.forward(167)
    turtle.down()
    turtle.right(90)
    turtle.forward(500)

def hr():
    turtle.up()
    turtle.goto(-300,-33)
    turtle.down()
    turtle.left(90)
    turtle.forward(500)
    turtle.left(90)
    turtle.up()
    turtle.forward(167)
    turtle.down()
    turtle.left(90)
    turtle.forward(500)

board()
vr()
hr()
