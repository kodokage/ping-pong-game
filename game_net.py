from turtle import  Turtle

class GameNet(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.dot(20, 'white')
        self.shapesize(30,1)
        self.color("white")