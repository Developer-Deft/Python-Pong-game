from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from middle_ball import Dashed, Dashed_2
import time
# create a screen using Screen class.
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("Gray")

screen.title("Welcome to the pong game.")
screen.tracer(0)

r_paddle = Paddle((375, 0), "blue")
l_paddle = Paddle((-375, 0), "red")
ball = Ball()
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
# w key for left
# s key for left
screen.onkey(l_paddle.up, "u")
screen.onkey(l_paddle.down, "d")

scoreboards = Scoreboard()
middle_wall = Dashed()
middle_wall_back = Dashed_2()

# create and move a paddle.

is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.track()
    if ball.ycor() > 280 or ball.ycor() < -280:
        # need to bounce the ball
        ball.bounce_y()

    # detect the collision with the ball
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 60 and ball.xcor() < -340:
        ball.bounce_x()

    # detect the paddle misses
    if ball.xcor() > 400:
        ball.reset_ball()
        scoreboards.l_point()

    if ball.xcor() < -400:
        ball.reset_ball()
        scoreboards.r_point()

screen.exitonclick()
