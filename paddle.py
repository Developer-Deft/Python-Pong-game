from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position, color):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.speed("fastest")
        self.color(color)
        self.penup()
        self.setposition(position)

    def up(self):
        new_y = self.ycor() + 30
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 30
        self.goto(self.xcor(), new_y)
