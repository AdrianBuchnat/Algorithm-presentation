

import pygame
import sys

WIDTH, HEIGHT = 600, 600
ROWS, COLS = 30, 30
CELL_SIZE = WIDTH // COLS

WHITE = (255, 255, 255)
BLACK = (0, 0 ,0)
GREY = (200, 200, 200)

def draw_grid(win):
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(win, GREY, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(win, GREY, (0, y), (WIDTH, y))


def main():
    pygame.init()


win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pathfinding Visualizer")

clock = pygame.time.Clock()

run = True
while run:
    clock.tick(60)

    win.fill(WHITE)
    draw_grid(win)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
sys.exit()
