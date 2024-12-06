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
        with open("data.txt", "r") as high_score:
            contents = int(high_score.read())
            if contents < self.level:
                print(f"you beat the highscore!! The last high score was {contents}")
                with open("data.txt", "w") as set_high_score:
                    set_high_score.write(str(self.level))

        self.write(f"Game Over", align="center", font= FONT)