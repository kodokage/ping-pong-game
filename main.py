from turtle import Screen
from paddle import Paddle
from game_net import GameNet
from ball import Ball
from score_board import ScoreBoard
import time

## Set Up Screen
screen = Screen()
screen.setup(width=800, height=600)
screen.listen()
screen.bgcolor("green")
screen.title("Ping Pong Game")
screen.tracer(0)

r_paddle = Paddle((370, 0))
l_paddle = Paddle((-370, 0))
# game_net = GameNet()
ball = Ball()
score = ScoreBoard()

screen.onkeypress(key="Up", fun=r_paddle.go_up)
screen.onkeypress(key="Down", fun=r_paddle.go_down)
screen.onkeypress(key="w", fun=l_paddle.go_up)
screen.onkeypress(key="s", fun=l_paddle.go_down)

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move_ball()

    ##Detect Wall Collision
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce_y()
       
    
    ## Detect left Paddle Collision
    if ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()

     ## Detect right Paddle Collision
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340:
        ball.bounce_x()

    ## Detect right score (out of bounds left)
    if ball.xcor() < -400:
        ball.reset_ball()
        score.score_right()

     ## Detect left score (out of bounds right)
    if ball.xcor() > 400:
        ball.reset_ball()
        score.score_left()

screen.exitonclick()