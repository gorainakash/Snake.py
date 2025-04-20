from turtle import Turtle
import random
colors = ["red", "blue", "purple", "orange", "yellow", "green"]


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color(random.choice(colors))
        self.shapesize(stretch_len=0.6, stretch_wid=0.6)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.color(random.choice(colors))
        r_x = random.randint(-270, 270)
        r_y = random.randint(-270, 270)
        self.goto(r_x, r_y)


