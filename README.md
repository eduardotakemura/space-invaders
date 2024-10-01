# Space Invaders - Python Turtle Recreation

This project is a recreation of the classic arcade game **Space Invaders** using Python's Turtle graphics library. The game is broken down into several components to handle different aspects of the game such as alien movement, player controls, and collision detection.

## Demo
You can play the game [here](https://replit.com/@eduardotakemura/space-invaders).

## Game Components

### 1. **Spaceship**
- The player controls a spaceship at the bottom of the screen.
- The spaceship can move left and right using the arrow keys and shoot projectiles using the spacebar.

### 2. **Aliens**
- The aliens move horizontally across the screen, dropping down a level each time they reach the edge.
- They shoot projectiles at the spaceship and try to reach the bottom of the screen.

### 3. **Blocks (Barriers)**
- The game includes blocks that serve as barriers between the spaceship and the aliens.
- These blocks can be destroyed by both the player's and aliens' shots.

### 4. **Shots**
- Both the player and the aliens can shoot projectiles.
- Collision detection checks for hits between shots and targets, such as the spaceship, aliens, or blocks.

### 5. **Board (Score and Lives)**
- The game keeps track of the player's score and remaining lives.
- If the player loses all lives, the game ends.

## Main Game Logic

The main game loop is handled in the `game()` function, which includes:
- Alien movement and shooting
- Spaceship controls and shooting
- Collision detection for shots hitting aliens, blocks, and the spaceship
- Wave progression when all aliens are destroyed
- Ending the game when the aliens reach the bottom of the screen or the player loses all lives.

### Key Functions:
- **check_shots_hit()**: Checks for collisions between the player's shots and alien shots.
- **check_alien_hit()**: Checks if the player's shots hit any aliens.
- **check_ship_hit()**: Checks if alien shots hit the player's spaceship.
- **check_barrier_hit()**: Checks for hits on the blocks (barriers) by any shots.
- **check_out_limits()**: Removes shots that go out of bounds.
- **check_alien_position()**: Ends the game if an alien reaches the bottom of the screen.

## Controls

- **Left Arrow Key**: Move the spaceship left.
- **Right Arrow Key**: Move the spaceship right.
- **Spacebar**: Shoot a projectile from the spaceship.

## Setup and Running the Game

1. Clone the repository or download the source files.
2. Ensure you have Python installed on your machine.
3. Run the main game file using:

    ```bash
    python main.py
    ```

4. Press **Space** to start the game.

## File Structure

- **main.py**: The main game loop and setup.
- **spaceship.py**: Controls the spaceship movements and actions.
- **aliens.py**: Handles the aliens' behavior and shooting.
- **blocks.py**: Defines the blocks (barriers) between the player and aliens.
- **shot.py**: Manages the shooting mechanics for both the spaceship and aliens.
- **board.py**: Manages the score, lives, and display.

## Future Improvements

- Adding more levels or increasing difficulty.
- Improving the graphical representation of the aliens and spaceship.
- Adding sound effects for shooting and explosions.

---

Enjoy playing the game!
