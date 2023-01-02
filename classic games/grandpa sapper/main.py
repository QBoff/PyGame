import copy

import pygame
from random import randint


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, surface):
        wcolor = pygame.Color("white")
        for i in range(self.height):
            for j in range(self.width):
                pygame.draw.rect(surface, wcolor, (self.left + self.cell_size * j, self.top + self.cell_size * i,
                                                   self.cell_size, self.cell_size), 1 if self.board[i][j] == 0 else 0)

    def get_click(self, mouse_pos):
        cell_coords = self.get_cell(mouse_pos)
        if cell_coords is None:
            return

        self.on_click(cell_coords)

    def get_cell(self, mouse_pos):
        board_width = self.width * self.cell_size
        board_height = self.height * self.cell_size
        if self.left < mouse_pos[0] < self.left + board_width:
            if self.top < mouse_pos[1] < self.top + board_height:
                cell_coords = (mouse_pos[1] - self.left) // self.cell_size,\
                              (mouse_pos[0] - self.top) // self.cell_size
                return cell_coords
        return None

    def on_click(self, cell_coords):
        i = cell_coords[0] // self.cell_size - self.left // self.cell_size
        j = cell_coords[1] // self.cell_size - self.top // self.cell_size
        if (i >= 0 and j >= 0) and (i < self.width and j < self.height):
            i = cell_coords[0] // self.cell_size - self.left // self.cell_size
            j = cell_coords[1] // self.cell_size - self.top // self.cell_size
            # print((i, j))
            self.board[j][i] = int(not bool(self.board[j][i]))
        else:
            print(None)






class Life(Board):
    
    def paint_block(self, field, pos):
        x, y = pos
        neighbors = 0
        for yS in range(y-1, y+2):
            for xS in range(x-1, x+2):
                if field[yS][xS] == 1:
                    neighbors += 1

        if field[y][x]:
            neighbors -= 1
            if neighbors == 2 or neighbors == 3:
                return 1
            else:
                return 0
        else:
            if neighbors == 3:
                return 1
            else:
                return 0




width_count, height_count = 120, 75
size = 10
resolution = width, height = width_count * size + 1, height_count * size + 1
FPS = 100
start = False

screen = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()

next_blocks_stage = [[0 for l in range(width_count)] for j in range(height_count)]
blocks = [[randint(0, 1) for l in range(width_count)] for j in range(height_count)]

def paint_block(field, pos):
    x, y = pos
    neighbors = 0
    for yS in range(y-1, y+2):
        for xS in range(x-1, x+2):
            if field[yS][xS] == 1:
                neighbors += 1

    if field[y][x]:
        neighbors -= 1
        if neighbors == 2 or neighbors == 3:
            return 1
        else:
            return 0
    else:
        if neighbors == 3:
            return 1
        else:
            return 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.key == pygame.K_SPACE:
            start = not start

    screen.fill(pygame.Color('black'))

    [pygame.draw.line(screen, (78,78,78), (x,0), (x, height)) for x in range(0, width, size)]
    [pygame.draw.line(screen, (78,78,78), (0,y), (width, y)) for y in range(0, height, size)]

    for x_block in range(1, width_count-1):
        for y_block in range(1, height_count-1):
            if blocks[y_block][x_block] == 1:
                pygame.draw.rect(screen, (255,255,255), (x_block * size + 2, y_block * size + 2, size-2, size-2))
            next_blocks_stage[y_block][x_block] = paint_block(blocks, (x_block, y_block))

    blocks = copy.deepcopy(next_blocks_stage)

    pygame.display.set_caption("FPS: " + str(int(clock.get_fps())))
    clock.tick(FPS)
    pygame.display.flip()