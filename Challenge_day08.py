import turtle

def draw_flower():
    screen = turtle.Screen()
    screen.bgcolor("white")

    toto = turtle.Turtle()
    toto.speed(0)
    toto.color("purple")
    for i in range(60):

        toto.circle(80, 70)
        toto.left(130)
        toto.circle(80, 70)
        toto.dot(15)
        toto.left(7.5)

    toto.penup()
    toto.goto(0, -20)
    toto.color("white")
    toto.begin_fill()
    toto.circle(20)

    toto.end_fill()
    screen.exitonclick()


draw_flower()