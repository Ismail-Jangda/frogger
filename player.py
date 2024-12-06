from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10


class Player(Turtle):
    def __init__(self) :
        super().__init__()
        self.shape("turtle")
        self.penup()        
        self.restart()

    def restart(self):
        self.setheading(90)
        self.setpos(STARTING_POSITION)

    def move_up(self):
        self.forward(MOVE_DISTANCE)
 