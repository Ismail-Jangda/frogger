from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.set_score()

    
    def next_level(self):
        self.level += 1
        self.set_score()
    
    def set_score(self):
        self.clear()
        self.penup()
        self.goto(-260 , 260)
        self.write(f"Level: {self.level}", font= FONT)
    
    def game_over(self):
        self.goto(0 , 0)
        self.write(f"Game Over", align="center", font= FONT)