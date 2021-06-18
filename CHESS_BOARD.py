import turtle

turtle.speed(0)
# turtle.hideturtle()
x=150
for i in range (1,9):
    turtle.up()
    turtle.goto(-200,-x)
    turtle.down()
    if(i%2==0):
        for j in range(1,9):
            if(j%2==0):
                turtle.begin_fill()
                turtle.fillcolor("black")
                for k in range(1,5):
                    turtle.forward(50)
                    turtle.left(90)
                turtle.end_fill()
            else:
                for k in range(1,5):
                    turtle.forward(50)
                    turtle.left(90)
            turtle.forward(50)
    else:
        for j in range(1,9):
            if(j%2!=0):
                turtle.begin_fill()
                turtle.fillcolor("black")
                for k in range(1,5):
                    turtle.forward(50)  
                    turtle.left(90)
                turtle.end_fill()
            else:
                for k in range(1,5):
                    turtle.forward(50)
                    turtle.left(90)
            turtle.forward(50)
    x=x-50