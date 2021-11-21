from turtle import Turtle
# STARTING_POSITION = (-350, 0)
MOVE_DISTANCE = 20
PADDLE_LENGTH = 5
MAX_PADDLE_Y_COORD = 260


class Paddle(Turtle):
    def __init__(self, starting_position):
        super().__init__()
        self.create_paddle(starting_position)

    def create_paddle(self, starting_position):
        self.shape("square")
        self.speed(0)
        self.color("white")
        self.penup()
        self.setposition(starting_position)
        self.turtlesize(stretch_wid=PADDLE_LENGTH, stretch_len=1)

    def paddle_up(self):
        coords = self.position()
        if coords[1] < MAX_PADDLE_Y_COORD:
            new_y_coord = coords[1] + MOVE_DISTANCE
            self.goto(coords[0], new_y_coord)

    def paddle_down(self):
        coords = self.position()
        if coords[1] > -MAX_PADDLE_Y_COORD:
            new_y_coord = coords[1] - MOVE_DISTANCE
            self.goto(coords[0], new_y_coord)
