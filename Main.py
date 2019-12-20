import turtle

interface = turtle.Screen()
interface.title("Pong v0.1")
interface.bgcolor("black")
interface.setup(800, 600, 0, 0)
interface.tracer(0)


class Paddle(turtle.Turtle):
    def __init__(self, posx, posy):
        super().__init__()
        self._tracer(0)
        self.shape("square")
        self.shapesize(5, 1)
        self.color("white")
        self.penup()
        self.goto(posx, posy)


def move_up():
    y = paddle_1.ycor()
    y += 20
    paddle_1.sety(y)


def move_down():
    y = paddle_1.ycor()
    y -= 20
    paddle_1.sety(y)


paddle_1 = Paddle(-350, 0)
paddle_2 = Paddle(350, 0)

interface.onkeypress(move_up, "Up")
interface.onkeypress(move_down, "Down")

while True:
    interface.update()
    interface.listen()
