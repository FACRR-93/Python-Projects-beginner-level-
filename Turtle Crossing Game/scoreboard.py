FONT = ("Courier", 14, "normal")
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.goto(-260, 260)
        self.hideturtle()
        self.write(arg=f"Level: {self.score}", align="left", font=FONT)

    def gameover(self):
        self.color("black")
        self.goto(0,0)
        self.write("GAME OVER",align = "center", font =FONT)

    def count(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Level: {self.score}", align="left", font=FONT)