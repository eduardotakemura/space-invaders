from turtle import Turtle

BLOCK_START_POS = (-189, -90)

class Blocks:
    def __init__(self):
        self.start()

    def create_block(self,init_x, init_y):
        x = init_x
        y = init_y
        new_block = []
        for col in range(6):
            for row in range(6):
                brick = Turtle(shape="square")
                brick.color('#00FF00')
                brick.shapesize(stretch_len=0.45, stretch_wid=0.3)
                brick.penup()
                brick.teleport(x, y)
                x += 9
                new_block.append(brick)
            x = init_x
            y += -6
        return new_block

    def refresh(self):
        for block in self.all_blocks:
            for brick in block:
                brick.goto(1000,1000)
        self.all_blocks = []

    def start(self):
        self.x, self.y = BLOCK_START_POS
        self.all_blocks = []
        for _ in range(4):
            current_block = self.create_block(self.x, self.y)
            self.all_blocks.append(current_block)
            self.x += 108