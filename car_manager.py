from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 10
MOVE_INCREMENT = 5


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid = None, stretch_len = 3)
        self.setheading(180)
        self.color(random.choice(COLORS))
        self.level = 0
        self.reset()
    
    def move_car(self):
        if self.xcor() < -330:
            self.reset()
        self.forward(STARTING_MOVE_DISTANCE + self.level * MOVE_INCREMENT)
    
    def reset(self):
        #Technically i should've defined the numbers in a separate constant file, but ill just do this
        self.goto(x = random.randint(330, 930), y = random.randint(-240,240))

    

