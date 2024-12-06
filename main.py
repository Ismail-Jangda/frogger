import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from detect_collision import detect_collision_with_car

NUMBER_OF_CARS_NEEDED =  20
FINISH_LINE_Y = 280
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

#set up the turtles
my_player = Player()
car_1 = []
myScoreboard = Scoreboard()
for num_of_cars in range(NUMBER_OF_CARS_NEEDED):
    car_1.append(CarManager())

screen.onkeypress(fun= my_player.move_up, key= "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    if my_player.ycor() > FINISH_LINE_Y:
        my_player.restart()
        myScoreboard.next_level()
        for num_of_cars in car_1:
            num_of_cars.level += 1 
    for num_of_cars in car_1:
        num_of_cars.move_car()
        if detect_collision_with_car(num_of_cars, my_player):
            game_is_on = False
    screen.update()

myScoreboard.game_over()
screen.update()

screen.exitonclick()
