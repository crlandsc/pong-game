from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball((0, 0))
l_scoreboard = Scoreboard((-100, 200))
r_scoreboard = Scoreboard((100, 200))
screen.listen()
screen.onkeypress(fun=r_paddle.paddle_up, key="Up")
screen.onkeypress(fun=r_paddle.paddle_down, key="Down")
screen.onkeypress(fun=l_paddle.paddle_up, key="w")
screen.onkeypress(fun=l_paddle.paddle_down, key="s")

game_is_on = True
l_score = 0
r_score = 0
while game_is_on:
    playing_round = True
    speed = 0.08
    while playing_round:
        screen.update()
        time.sleep(speed)
        ball.move()

        # Detect wall collision
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.y_bounce()

        # Detect paddle collision
        if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
            ball.x_bounce()
            speed *= .9

        # Detect R paddle miss
        if ball.xcor() > 380:
            l_scoreboard.increase_score()
            ball.reset_position()
            playing_round = False

        # Detect L paddle miss
        if ball.xcor() < -380:
            r_scoreboard.increase_score()
            r_score += 1
            ball.reset_position()
            playing_round = False


screen.exitonclick()