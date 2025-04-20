from turtle import Turtle
import random


class SpecialFood(Turtle):
    def __init__(self):
        super().__init__()
        self.types = {
            "bonus": {"color": "gold", "effect": "score"},
            "slow": {"color": "cyan", "effect": "slow"},
            "poison": {"color": "red", "effect": "poison"}
        }
        self.type = None
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=1.2, stretch_wid=1.2)
        self.speed("fastest")
        self.hideturtle()
        self.active = False

    def spawn(self):
        if not self.active:
            self.type = random.choice(list(self.types.keys()))
            self.color(self.types[self.type]["color"])
            x = random.randint(-270, 270)
            y = random.randint(-270, 270)
            self.goto(x, y)
            self.showturtle()
            self.active = True

    def despawn(self):
        self.hideturtle()
        self.active = False
