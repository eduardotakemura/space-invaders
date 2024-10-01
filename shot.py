from turtle import Turtle
import random

class Shot:
    def __init__(self, object):
        self.shots = []
        self.obj = object
        self.shot_speed = 36
        self.last_cycle = 0
        self.ship_shot_freq = 3

    def ship_shot(self,current_cycle):
        if (current_cycle - self.last_cycle) > self.ship_shot_freq:
            ship_x = self.obj.xcor()
            ship_y = self.obj.ycor()
            new_shot = Turtle()
            new_shot.shape("classic")
            new_shot.color('#00FF00')
            new_shot.shapesize(stretch_len=0.8, stretch_wid=0.6)
            new_shot.penup()
            new_shot.teleport(ship_x,ship_y)
            new_shot.setheading(90)
            self.shots.append(new_shot)
            self.last_cycle = current_cycle

    def alien_shot(self,cycles,wave):
        ref_speed = [7,5,3]
        if int(wave) < 4:
            speed = ref_speed[wave]
        else:
            speed = 1
        if cycles % speed == 0:
            # Get all current coordinates of aliens #
            aliens_coord = [(alien.xcor(), alien.ycor()) for alien in self.obj.all_aliens]

            # Select a random x position #
            x_list = [item[0] for item in aliens_coord]
            chosen_x = random.choice(x_list)

            # Select the lower y with the chosen x #
            match_list = [item[1] for item in aliens_coord if item[0] == chosen_x]
            chosen_y = min(match_list)

            # Create shot at the select position #
            new_shot = Turtle()
            new_shot.shape("classic")
            new_shot.color('yellow')
            new_shot.shapesize(stretch_len=0.8, stretch_wid=0.6)
            new_shot.penup()
            new_shot.teleport(chosen_x, chosen_y)
            new_shot.setheading(270)
            self.shots.append(new_shot)

    def move_shots(self):
        if len(self.shots) > 0:
            for shot in self.shots:
                shot.forward(self.shot_speed)

    def reset_shots(self):
        for shot in self.shots:
            shot.goto(1000,1000)
        self.shots = []



