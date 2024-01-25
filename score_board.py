from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.r_score = 0
        self.l_score = 0
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.goto(100, 260)
        self.write(self.r_score, align="center", font=("Helvetica", 25, "normal"))
        self.goto(-100, 260)
        self.write(self.l_score, align="center", font=("Helvetica", 25 , "normal"))


    def score_right(self):
        self.r_score += 1
        self.update_score()

    def score_left(self):
        self.l_score += 1
        self.update_score()
       
