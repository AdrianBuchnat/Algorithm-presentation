import pygame
import heapq


def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()


def dikstra(draw, grid, start, end):
    count = 0
    open_set = []
    heapq.heappush(open_set, (0, count, start))

    came_from = {}

    g_score = {tile: float("inf") for row in grid for tile in row}
    g_score[start] = 0

    open_set_hash = {start}


    while open_set:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


        current = heapq.heappop(open_set)[2]
        open_set_hash.remove(current)

        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            start.make_start()
            return True

        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1
            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                if neighbor not in open_set_hash:
                    count += 1
                    heapq.heappush(open_set, (g_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()
 
        if current != start:
            current.make_closed()

        draw()

    return False

