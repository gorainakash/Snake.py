from turtle import Turtle,Screen
STARTING_P=[(0, 0), (-20, 0), (-40, 0)]
MOVE=20


class Snake:

    def __init__(self):
        self.segment=[]
        self.create_snake()
        self.head = self.segment[0]
        self.head.shape("triangle")

    def create_snake(self):
        for p in STARTING_P:
            self.add_s(p)

    def add_s(self, p):
        tim = Turtle(shape="circle")
        tim.color("white")
        tim.penup()
        tim.goto(p)
        self.segment.append(tim)

    def extend_s(self):
        self.add_s(self.segment[-1].position())

    def move(self):
        for seg_n in range(len(self.segment) - 1, 0, -1):
            nx = self.segment[seg_n - 1].xcor()
            ny = self.segment[seg_n - 1].ycor()
            self.segment[seg_n].goto(nx, ny)
        self.head.fd(MOVE)

    def up(self):
        if self.head.heading() == 270:
            pass
        else:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() == 90:
            pass
        else:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() == 180:
            pass
        else:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() == 0:
            pass
        else:
            self.head.setheading(180)

