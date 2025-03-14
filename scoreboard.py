from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(x=-200, y=250)
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(arg=f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def level_up(self):
        self.level += 1
        self.update_level()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg=f"GAME OVER.", align=ALIGNMENT, font=FONT)
