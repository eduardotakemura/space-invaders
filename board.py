from turtle import Turtle
from spaceship import Spaceship
import random

class Board(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.highscore = 0
        self.mysterious = [25,50,75,100]
        self.reset()

    def reset(self):
        self.score = 0
        self.lives = 3
        self.lives_ship = []
        self.aliens_start = []

    def base_board(self):
        # Score column #
        self.goto(-135, 280)
        self.write(arg="SCORE", align='center', font=('Calibri', 20, 'normal'))
        self.goto(-135, 252)
        self.write(arg=self.format_score(self.score), align='center', font=('Calibri', 20, 'normal'))

        # Highscore column #
        self.goto(135, 280)
        self.write(arg="HIGHSCORE", align='center', font=('Calibri', 20, 'normal'))
        self.goto(135, 252)
        self.write(arg=self.format_score(self.highscore), align='center', font=('Calibri', 20, 'normal'))

        # Bottom line #
        self.goto(-270, -216)
        self.pendown()
        self.pensize(3)
        self.color('#00FF00')
        self.setheading(0)
        self.forward(550)
        self.penup()

        # Lives Row #
        self.goto(-81, -252)
        self.color('white')
        self.write(arg=self.lives, align='center', font=('Calibri', 20, 'normal'))
        if self.lives > 1:
            x = self.xcor()
            y = self.ycor()
            for live in range(self.lives-1):
                ship = Spaceship()
                ship.goto(x + 27 , y + 14)
                x += 36
                self.lives_ship.append(ship)

    def increase_score(self, alien):
        if alien.color()[0] == "yellow":
            self.score += 10
        elif alien.color()[0] == "orange":
            self.score += 20
        elif alien.color()[0] == "red":
            self.score += 30
        elif alien.color()[0] == "blue":
            random_score = random.choice(self.mysterious)
            self.score += random_score
            print(random_score)
        self.refresh()

    def refresh(self):
        self.clear()
        if len(self.aliens_start) > 0:
            for alien in self.aliens_start:
                alien.goto(1000,1000)
                self.aliens_start = []
        for ship in self.lives_ship:
            ship.goto(1000,1000)
        self.base_board()

    def format_score(self, score):
        score = int(score)
        if score < 10:
            formated_score = f"000{score}"
        elif score < 100:
            formated_score = f"00{score}"
        elif score < 1000:
            formated_score = f"0{score}"
        else:
            formated_score = f"{score}"
        return formated_score

    def start_board(self):
        self.clear()
        self.base_board()

        # First Row #
        self.color('white')
        self.goto(0, 126)
        self.write(arg="PLAY", align='center', font=('Calibri', 20, 'normal'))

        # Second Row #
        self.goto(0, 90)
        self.write(arg="SPACE INVADERS", align='center', font=('Calibri', 20, 'normal'))

        # Third Row #
        self.goto(0, 36)
        self.write(arg="PRESS SPACE TO START", align='center', font=('Calibri', 20, 'normal'))

        # Forth Row #
        self.goto(0, -18)
        self.write(arg="*SCORE ADVANCE TABLE*", align='center', font=('Calibri', 20, 'normal'))

        # Pontuation Table #
        color_order = ['blue','red','orange','yellow']
        text = ["= ? MYSTERY","= 30 POINTS","= 20 POINTS","= 10 POINTS"]
        y = -54
        for color,text in zip(color_order,text):
            alien = Turtle(shape="turtle")
            alien.setheading(270)
            alien.color(color)
            alien.penup()
            alien.shapesize(stretch_len=0.9, stretch_wid=1.35)
            alien.goto(-81, y+18)
            self.aliens_start.append(alien)
            self.goto(12, y)
            self.write(arg=text, align='center', font=('Calibri', 20, 'normal'))
            y -= 36

    def end_board(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.refresh()
        self.goto(0, 224)
        self.write(arg="GAME OVER", align='center', font=('Calibri', 20, 'normal'))

    def restart_board(self):
        self.reset()
        self.refresh()
        self.goto(0,-54)
        self.write(arg="PRESS R TO RESTART", align='center', font=('Calibri', 20, 'normal'))






