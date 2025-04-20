from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.up()

    def up(self):
        self.write(f"Score : {self.score}", align="center", font=("courier", 18, "normal"))

    def inc(self):
        self.score += 1
        self.clear()
        self.up()

    def game_o(self):
        self.goto(0, 0)
        self.write("☠ GAME OVER ☠", align="center", font=("courier", 18, "normal"))






