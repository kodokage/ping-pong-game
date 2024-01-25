from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_pos = 10
        self.y_pos = 10

    def move_ball(self):
        x_dir = self.xcor() - self.x_pos
        y_dir = self.ycor() + self.y_pos
        self.goto(x_dir, y_dir)

    def bounce_x(self):
        self.x_pos *= -1
        # self.move_ball()

    def bounce_y(self):
        self.y_pos *= -1
        # self.move_ball()

    def reset_ball(self):
        self.goto(0,0)