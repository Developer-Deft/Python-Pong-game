from turtle import Turtle


class Dashed(Turtle):
    def __init__(self):
        super().__init__()
        self.color("Brown")
        self.setheading(90)
        for _ in range(15):
            self.forward(12)
            self.penup()
            self.forward(12)
            self.pendown()


class Dashed_2(Turtle):
    def __init__(self):
        super().__init__()
        self.color("Brown")
        self.setheading(270)
        for _ in range(15):
            self.forward(12)
            self.penup()
            self.forward(12)
            self.pendown()

