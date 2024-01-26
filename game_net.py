from turtle import  Turtle

y_location = [-300, -200, -100, 0, 100,  200,  300]

class GameNet(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.net =  []
        

        for item in range(7):
            item_index = item
            item = Turtle("square")
            item.penup()
            item.shapesize(2,1)
            item.color("white")
            item.goto(0, y_location[item_index])
            self.net.append(item)

