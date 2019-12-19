import turtle


# class Interface:
#
#     def __init__(self):
#         interface = turtle.Screen()
#         interface.title("Pong v0.1")
#         interface.bgcolor("black")
#         interface.setup(800, 600, 0, 0)
#         interface.tracer(0)

# Main screen
interface = turtle.Screen()
interface.title("Pong v0.1")
interface.bgcolor("black")
interface.setup(800, 600, 0, 0)
interface.tracer(0)


# Paddle
class Paddle:

    def __init__(self, x, y):
        self = turtle.Turtle()
        self._tracer(0)
        self.shape("square")
        self.shapesize(5, 1)
        self.color("white")
        self.penup()
        self.setx({}) = x
        self.sety({}) = y


paddle_1 = Paddle(350, 0)


while True:
    interface.update()

