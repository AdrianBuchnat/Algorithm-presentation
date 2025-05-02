import pygame
import sys
from config import BLACK, PURPLE, ROWS, TURQUISE, WIDTH, HEIGHT, COLS, CELL_SIZE, \
     WHITE, GREY, YELLOW, RED, GREEN
from tile import Tile
from astar import astar


def draw_grid(win):
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(win, GREY, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(win, GREY, (0, y), (WIDTH, y))


def draw_legend(win):
    font = pygame.font.Font(None, 18)

    legend_items = [
        ("Start", GREEN),
        ("End", RED),
        ("Wall", BLACK),
        ("Open", TURQUISE),
        ("Closed", PURPLE),
        ("Path", YELLOW)
    ]

    for i, (label, color) in enumerate(legend_items):
        pygame.draw.rect(win, color, (10, 10 + i * 30, 20, 20))
        text = font.render(label, True, (0, 0, 0))
        win.blit(text, (40, 10 + i * 30))

        
def draw(win, grid):
    win.fill(WHITE)
    for row in grid:
        for tile in row:
            tile.draw(win)

    draw_grid(win)
    draw_legend(win)
    pygame.display.update()


def get_clicked_pos(pos):
    x, y = pos
    col = x // CELL_SIZE
    row = y // CELL_SIZE
    return row, col


def make_grid():
    return[[Tile(row,col) for col in range(COLS)] for row in range(ROWS)]



def main():
    pygame.init()
    pygame.font.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pathfinding Visualizer")
    
    grid = make_grid()
    clock = pygame.time.Clock()
    run = True
    changed = True

    start = None
    end = None

    while run:
        clock.tick(10)

        if changed == True:
            draw(win, grid)
            changed = False
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and start and end:
                    for row in grid:
                        for tile in row:
                            tile.update_neighbors(grid)

                    astar(lambda: draw(win, grid), grid, start, end)

                elif event.key == pygame.K_r:
                    start = None
                    end = None
                    grid = make_grid()
                    changed = True
                

        #left click - set start, end or wall
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            row, col = get_clicked_pos(pos)
            if 0 <= row < ROWS and 0 <= col < COLS:
                tile = grid[row][col]
                if not start and tile != end:
                    start = tile
                    tile.make_start()
                elif not end and tile != start:
                    end = tile;
                    tile.make_end()
                elif tile != start and tile != end:
                    tile.make_wall()
            changed = True
        
        #right clik - dalate wall / start / end
        if pygame.mouse.get_pressed()[2]:
            pos = pygame.mouse.get_pos()
            row, col = get_clicked_pos(pos)
            if 0 <= row < ROWS and 0 <= col < COLS:
                tile = grid[row][col]
                tile.reset()
                if tile == start:
                    start = None
                elif tile == end:
                    end = None
            changed = True
    
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()

