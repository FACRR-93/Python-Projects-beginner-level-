from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.write(arg = f"Score: {self.score}", align = "center", font =("Arial", 10, "normal"))

    def gameover(self):
        self.color("white")
        self.goto(0,0)
        self.write("GAME OVER",align = "center", font =("Arial", 10, "normal"))

    def count(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Score: {self.score}", align="center", font=("Arial", 10, "normal"))