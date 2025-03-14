from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
UP_DIRECTION = 90
DOWN_DIRECTION = -90


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(to_angle=90.0)
        self.goto(STARTING_POSITION)

    def move_up(self):
        if self.ycor() < FINISH_LINE_Y:
            if self.heading() != UP_DIRECTION:
                self.setheading(to_angle=UP_DIRECTION)
            new_y = self.ycor() + MOVE_DISTANCE
            self.goto(self.xcor(), new_y)

    def move_down(self):
        if self.ycor() > -FINISH_LINE_Y:
            if self.heading() != DOWN_DIRECTION:
                self.setheading(to_angle=DOWN_DIRECTION)
            new_y = self.ycor() - MOVE_DISTANCE
            self.goto(self.xcor(), new_y)

    def back_to_start(self):
        self.goto(STARTING_POSITION)

    def finish(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
        else:
            return False
