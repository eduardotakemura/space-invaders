from turtle import Turtle
import random

ALIEN_START_POS = (-162, 216)
COLOR_ORDER = ['red','orange','orange','yellow','yellow']
class Aliens:
    def __init__(self):
        self.pace = 3
        self.mysterious_pace = 12
        self.start()

    def start(self):
        self.all_aliens = []
        self.generate_aliens(ALIEN_START_POS[0], ALIEN_START_POS[1])
        self.create_mysterious()

    def refresh(self):
        for alien in self.all_aliens:
            alien.goto(1000,1000)
        self.all_aliens = []
        self.mysterious.reset()

    def generate_aliens(self,x,y):
        for col in range(5):
            for row in range(11):
                alien = Turtle(shape="turtle")
                alien.color(COLOR_ORDER[col])
                alien.shapesize(stretch_len=0.9, stretch_wid=1.35)
                alien.penup()
                alien.teleport(x, y)
                alien.setheading(270)
                x += 27
                self.all_aliens.append(alien)
            x = ALIEN_START_POS[0]
            y -= 36

    def move(self):
        for alien in self.all_aliens[::-1]:
            if alien.xcor() >= 216 or alien.xcor() <= -216:
                self.pace *= -1
                self.drop_row()
                break

        for alien in self.all_aliens[::-1]:
            alien.teleport(alien.xcor() + self.pace)

    def drop_row(self):
        for alien in self.all_aliens:
            alien.teleport(y=alien.ycor()-18)

    def create_mysterious(self):
        self.mysterious = Turtle(shape="turtle")
        self.mysterious.color("blue")
        self.mysterious.shapesize(stretch_len=0.9, stretch_wid=1.35)
        self.mysterious.penup()
        self.reset_mysterious()

    def move_mysterious(self):
        if self.mysterious_active:
            self.mysterious.forward(self.mysterious_pace)
            self.mysterious_out_screen()

    def reset_mysterious(self):
        self.init_x = random.choice([320, -320])
        self.init_y = 234
        self.mysterious.teleport(self.init_x, self.init_y)
        if self.init_x > 0:
            self.mysterious.setheading(180)
        else:
            self.mysterious.setheading(0)
        self.mysterious_active = False

    def mysterious_out_screen(self):
        if self.mysterious.xcor() > 320 or self.mysterious.xcor() < -320:
            self.reset_mysterious()



