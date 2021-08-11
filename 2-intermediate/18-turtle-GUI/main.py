from turtle import Turtle, Screen

tim = Turtle()
# timmy_the_turtle.shape('turtle')
# timmy_the_turtle.color('red')
# timmy_the_turtle.forward(180)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(50)

# Drawing square
for _ in range(4):
    tim.forward(180)
    tim.right(90)

screen = Screen()
screen.exitonclick()
