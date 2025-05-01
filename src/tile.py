import pygame
from config import WHITE, BLACK, CELL_SIZE, GREEN, RED

class Tile:
    def __init__(self, row, col) -> None:
        self.row = row
        self.col = col

        self.x = col * CELL_SIZE
        self.y = row * CELL_SIZE
        self.color = WHITE
        self.if_wall = False


    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, CELL_SIZE, CELL_SIZE))


    def make_wall(self):
        self.color = BLACK
        self.is_wall = True


    def reset(self):
        self.color = WHITE
        self.is_wall = False


    def make_start(self):
        self.color = GREEN


    def make_end(self):
        self.color = RED
