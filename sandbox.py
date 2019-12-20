import turtle


class Interface(turtle._Screen):
    def __init__(self):
        super().__init__()
        turtle.TurtleScreen.__init__(self, Interface._canvas)
        self.setup(800, 600)
        # self.screensize(1000, 1000)
        self.title("Pong v0.2")
        self.bgcolor("black")


def MyScreenFunction():
    if turtle.Turtle._screen is None:
        turtle.Turtle._screen = Interface()
    return turtle.Turtle._screen


turtle.Screen = MyScreenFunction


class Paddle(turtle.Turtle):
    def __init__(self, posx, posy):
        super().__init__()
        self._tracer(0)
        self.shape("square")
        self.shapesize(5, 1)
        self.color("white")
        self.penup()
        self.goto(posx, posy)

    def move_up(self):
        y = self.ycor()
        y += 20
        self.sety(y)

    def move_down(self):
        y = self.ycor()
        y -= 20
        self.sety(y)


paddle_1 = Paddle(-350, 0)
paddle_2 = Paddle(350, 0)
# interface = Interface()
interface = turtle.Screen()

interface.onkeypress(paddle_1.move_up, "z")
interface.onkeypress(paddle_1.move_down, "s")
interface.onkeypress(paddle_2.move_up, "Up")
interface.onkeypress(paddle_2.move_down, "Down")

while True:
    interface.update()
    interface.listen()
