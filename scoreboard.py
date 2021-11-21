from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 60, "normal")

class Scoreboard(Turtle):

    def __init__(self, coordinates):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.setposition(coordinates)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)