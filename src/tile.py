import pygame
from config import WHITE, BLACK, CELL_SIZE, GREEN, RED, ROWS, COLS, \
    PURPLE, TURQUISE, YELLOW

class Tile:
    def __init__(self, row, col) -> None:
        self.row = row
        self.col = col

        self.x = col * CELL_SIZE
        self.y = row * CELL_SIZE
        self.color = WHITE
        self.is_wall = False


#    def __eq__(self, other):
#        return isinstance(other, Tile) and self.row == other.row and self.col == other.col
#
#
#    def __hash__(self):
#        return hash((self.row, self.col))


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
    

    def get_pos(self):
        return self.row, self.col


    def make_open(self):
        self.color = TURQUISE


    def make_closed(self):
        self.color = PURPLE


    def make_path(self):
        self.color = YELLOW


    def update_neighbors(self, grid):
        self.neighbors = []
        if self. row < ROWS - 1 and not grid[self.row + 1][self.col].is_wall: #Bottom tile
            self.neighbors.append(grid[self.row + 1][self.col])
        if self.row > 0 and not grid[self.row - 1][self.col].is_wall: #Up tile
            self.neighbors.append(grid[self.row - 1][self.col])
        if self.col < COLS - 1 and not grid[self.row][self.col + 1].is_wall:
            self.neighbors.append(grid[self.row][self.col + 1])
        if self.col > 0 and not grid[self.row][self.col - 1].is_wall:
            self.neighbors.append(grid[self.row][self.col - 1])

