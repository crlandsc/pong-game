from turtle import Turtle
# STARTING_POSITION = (-350, 0)
# MOVE_DISTANCE = 10
BOUNDARY = 280

class Ball(Turtle):
    def __init__(self, starting_position):
        super().__init__()
        self.create_ball(starting_position)
        self.y_move = 10
        self.x_move = 10

    def create_ball(self, starting_position):
        self.shape("circle")
        self.speed(0)
        self.color("white")
        self.penup()
        self.setposition(starting_position)

    def move(self):
        # self.wall_bounce()
        new_y_coord = self.ycor() + self.y_move
        new_x_coord = self.xcor() + self.x_move
        self.goto(new_x_coord, new_y_coord)

    def y_bounce(self):
        # if self.ycor() > BOUNDARY or self.ycor() < -BOUNDARY:
        self.y_move *= -1

    def x_bounce(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.x_move *= -1
        # self.y_move *= -1


