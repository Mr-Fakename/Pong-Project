import turtle
import random

interface = turtle.Screen()
interface.title("Turtle Pong v0.8")
interface.bgcolor("white")
interface.setup(800, 600, 0, 0)
interface.tracer(0)
interface.colormode(255)

score = turtle.Turtle()
score.color("black")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Player 1: 0  Player 2: 0", align="center", font=("Consolas", 24, "normal"))


class Ball(turtle.Turtle):
    def __init__(self, paddle_1, paddle_2):
        super().__init__()
        self.speed(0)
        self.shape("turtle")
        self.color(random.randint(0, 250), random.randint(0, 250), random.randint(0, 250))
        self.penup()
        self.goto(0, 0)
        self.dx = 1
        self.dy = 1
        self.paddle_1 = paddle_1
        self.paddle_2 = paddle_2

    def collision(self):

        # Top and bottom
        global score_2, score_1
        if self.ycor() > 290:
            self.sety(290)
            self.dy *= -1
        elif self.ycor() < -290:
            self.sety(-290)
            self.dy *= -1

        # Left and right
        if self.xcor() > 350:
            self.goto(0, 0)
            self.color(random.randint(0, 250), random.randint(0, 250), random.randint(0, 250))
            self.dx *= -1
            score_1 += 1
            score.clear()
            score.write("Player 1: {}  Player 2: {}".format(score_1, score_2), align="center",
                        font=("Consolas", 24, "normal"))

        elif self.xcor() < -350:
            self.goto(0, 0)
            self.color(random.randint(0, 250), random.randint(0, 250), random.randint(0, 250))
            self.dx *= -1
            score_2 += 1
            score.clear()
            score.write("Player 1: {}  Player 2: {}".format(score_1, score_2), align="center",
                        font=("Consolas", 24, "normal"))

        # Paddle and ball collisions
        if self.xcor() < -340 and self.paddle_1.ycor() + 50 > self.ycor() > self.paddle_1.ycor() - 50:
            self.dx *= -1
        elif self.xcor() > 340 and self.paddle_2.ycor() + 50 > self.ycor() > self.paddle_2.ycor() - 50:
            self.dx *= -1

    def move(self):
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)


class Paddle(turtle.Turtle):
    def __init__(self, posx, posy=0):
        super().__init__()
        self._tracer(0)
        self.shape("square")
        self.shapesize(5, 1)
        self.color("black")
        self.penup()
        self.goto(posx, posy)

    def move_up(self):
        y = self.ycor()
        y += 30
        self.sety(y)

    def move_down(self):
        y = self.ycor()
        y -= 30
        self.sety(y)


score_1 = 0
score_2 = 0

paddle_1 = Paddle(-350)
paddle_2 = Paddle(350)

ball = Ball(paddle_1, paddle_2)

interface.onkeypress(paddle_1.move_up, "z")
interface.onkeypress(paddle_1.move_down, "s")
interface.onkeypress(paddle_2.move_up, "Up")
interface.onkeypress(paddle_2.move_down, "Down")

while True:
    interface.update()
    interface.listen()
    ball.collision()
    ball.move()
