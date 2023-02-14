from turtle import Turtle
START_POSITION = ((0, 0), (-20, 0), (-40, 0))


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in START_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_xcor = self.segments[i - 1].xcor()
            new_ycor = self.segments[i - 1].ycor()
            self.segments[i].goto(x=new_xcor, y=new_ycor)
        self.head.forward(10)

    def refresh(self):
        for segment in self.segments:
            segment.goto(1000, 1000)

        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def up(self):
        if not self.head.heading() == 270:
            self.head.setheading(90)

    def down(self):
        if not self.head.heading() == 90:
            self.head.setheading(270)

    def left(self):
        if not self.head.heading() == 0:
            self.head.setheading(180)

    def right(self):
        if not self.head.heading() == 180:
            self.head.setheading(0)
