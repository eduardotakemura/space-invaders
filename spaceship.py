from turtle import Turtle

STARTING_POSITION = (-216,-180)

class Spaceship(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("triangle")
        self.color('#00FF00')
        self.shapesize(stretch_len=0.9, stretch_wid=1.35)
        self.penup()
        self.setheading(90)
        self.ship_speed = 18
        self.refresh()

    def refresh(self):
        self.teleport(STARTING_POSITION[0], STARTING_POSITION[1])

    def move_right(self):
        if self.xcor() < 216:
            self.teleport(x = self.xcor()+self.ship_speed)

    def move_left(self):
        if self.xcor() > -216:
            self.teleport(x = self.xcor()-self.ship_speed)