from turtle import Screen
from spaceship import Spaceship
from blocks import Blocks
from aliens import Aliens
from shot import Shot
from board import Board
import time
import random

# Games Methods #
def check_shots_hit():
    for ship_shot in ship_shooter.shots:
        for alien_shot in alien_shooter.shots:
            if ship_shot.distance(alien_shot) < 10:
                alien_shooter.shots.remove(alien_shot)
                ship_shooter.shots.remove(ship_shot)
                alien_shot.goto(1000, 1000)
                ship_shot.goto(1000, 1000)
                break

def check_alien_hit():
    global wave
    for ship_shot in ship_shooter.shots:
        for alien in aliens.all_aliens:
            if ship_shot.distance(alien) < 20:
                aliens.all_aliens.remove(alien)
                ship_shooter.shots.remove(ship_shot)
                alien.goto(1000,1000)
                ship_shot.goto(1000, 1000)
                board.increase_score(alien)
                break

        # Check if all aliens destroyed #
        if len(aliens.all_aliens) == 0:
            time.sleep(2)
            wave += 1
            aliens.pace += 3
            ship_shooter.reset_shots()
            alien_shooter.reset_shots()
            aliens.start()
            ship.refresh()

        # Check mysterious hit #
        if ship_shot.distance(aliens.mysterious) < 25:
            ship_shooter.shots.remove(ship_shot)
            ship_shot.goto(1000, 1000)
            board.increase_score(aliens.mysterious)
            aliens.reset_mysterious()
            break

def check_ship_hit():
    for shot in alien_shooter.shots:
        x_dist = shot.xcor() - ship.xcor()
        y_dist = shot.ycor() - ship.ycor()
        if (-21.5 < x_dist < 21.5) and (-19 < y_dist < 19):
            ship.hideturtle()
            screen.update()
            time.sleep(2)
            ship_shooter.reset_shots()
            alien_shooter.reset_shots()
            ship.showturtle()
            ship.refresh()
            aliens.reset_mysterious()
            board.lives -= 1
            if board.lives == 0:
                end_screen()
            else:
                board.refresh()

def check_out_limits(shots):
    for shot in shots:
        if shot.ycor() > 280 or shot.ycor() < -216:
            shots.remove(shot)
            shot.goto(1000, 1000)
            break

def check_barrier_hit(shots):
    block_hit = False
    for shot in shots:
        for block in blocks.all_blocks:
            for brick in block:
                if shot.distance(brick) < 5:
                    brick_x = brick.xcor()
                    brick_to_remove = brick
                    for current_brick in block:
                        if current_brick.xcor() == brick_x:
                            if shot.heading() == 90:
                                if current_brick.ycor() < brick_to_remove.ycor():
                                    brick_to_remove = current_brick
                            elif shot.heading() == 270:
                                if current_brick.ycor() > brick_to_remove.ycor():
                                    brick_to_remove = current_brick

                    shots.remove(shot)
                    brick_to_remove.goto(1000, 1000)
                    shot.goto(1000, 1000)
                    block_hit = True
                    break
            if block_hit:
                break

def check_alien_position():
    # Check reach bottom #
    for alien in aliens.all_aliens:
        if alien.ycor() < -126:
            end_screen()
        elif alien.ycor() < -72:
            blocks.refresh()

# Game #
def start_screen():
    board.start_board()
    screen.onkey(fun=game,key='space')
    screen.update()

def end_screen():
    global game_on
    # End Game Board #
    board.end_board()
    screen.update()
    time.sleep(3)

    # Restart Screen #
    game_on = False
    blocks.refresh()
    aliens.refresh()
    ship_shooter.reset_shots()
    alien_shooter.reset_shots()
    board.restart_board()
    ship.hideturtle()
    screen.update()
    screen.onkey(fun=game, key='r')

def game():
    global game_on, aliens, blocks, ship, ship_shooter, alien_shooter
    board.refresh()
    aliens = Aliens()
    blocks = Blocks()
    ship = Spaceship()
    ship_shooter = Shot(ship)
    alien_shooter = Shot(aliens)

    screen.onkey(fun=ship.move_right,key='Right')
    screen.onkey(fun=ship.move_left,key='Left')
    screen.onkey(fun=lambda: ship_shooter.ship_shot(cycles),key='space')

    # Main loop #
    cycles = 0
    wave = 1
    game_on = True
    while game_on:
        time.sleep(0.1)
        screen.update()
        check_shots_hit()
        check_alien_hit()
        check_ship_hit()
        check_barrier_hit(alien_shooter.shots)
        check_barrier_hit(ship_shooter.shots)
        check_alien_position()

        aliens.move()
        ship_shooter.move_shots()
        alien_shooter.move_shots()
        aliens.move_mysterious()
        check_out_limits(alien_shooter.shots)
        check_out_limits(ship_shooter.shots)
        alien_shooter.alien_shot(cycles,wave)

        # Generate a mysterious alien #
        if random.random() < 0.01 and not aliens.mysterious_active:
            aliens.mysterious_active = True
        cycles += 1

# Screen Setup #
screen = Screen()
screen.title("Space Invaders")
screen.setup(height=648,width=540)
screen.bgcolor('black')
screen.tracer(0)
screen.listen()
board = Board()

start_screen()

screen.exitonclick()