import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(2)

myturtle = Player()
car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkeypress(key="Up", fun=myturtle.move_up)
screen.onkeypress(key="Down", fun=myturtle.move_down)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car.move()
    car.create_car()
    screen.update()

    for car_obj in car.total_car:
        if myturtle.distance(car_obj) < 20:
            score.game_over()
            game_is_on = False
            screen.onkeypress(None, "Up")
            screen.onkeypress(None, "Down")
            break

    if myturtle.finish():
        score.level_up()
        myturtle.back_to_start()
        car.level_up()


screen.exitonclick()