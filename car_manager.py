from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.total_car = []
        self.create_car()
        self.move_distance = STARTING_MOVE_DISTANCE
        self.total_distance_travelled = 0

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.hideturtle()
            new_car.shape("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(300, random.randrange(start=-240, stop=240, step=10))
            new_car.showturtle()
            self.total_car.append(new_car)

    def move(self):
        for car in self.total_car:
            new_x = car.xcor() - self.move_distance
            car.goto(new_x, car.ycor())
        self.check_distance()

    def check_distance(self):
        for car in self.total_car[:]:
            if car.xcor() < -300:
                car.hideturtle()
                self.total_car.remove(car)

    def level_up(self):
        for car in self.total_car[:]:
            car.hideturtle()
        self.total_car.clear()
        self.move_distance += MOVE_INCREMENT