import pygame
from math import floor
import random


class Board:
    def __init__(self, width, height):
        self.width = abs(width)
        self.height = abs(height)
        self.board = [[-1] * width for _ in range(height)]
        self.left = 7
        self.top = 7
        self.cell_size = 30

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, surface):
        wcolor = [pygame.Color("white"), pygame.Color("red")]
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j] == -1:
                    pygame.draw.rect(surface, wcolor[0], (self.left + self.cell_size * j, self.top + self.cell_size * i,
                                                          self.cell_size, self.cell_size), 1 if self.board[i][j] == -1 else 0)
                elif self.board[i][j] == 10:
                    pygame.draw.rect(surface, wcolor[1], (self.left + self.cell_size * j, self.top + self.cell_size * i,
                                                          self.cell_size, self.cell_size), 1 if self.board[i][j] == -1 else 0)
                else:
                    font = pygame.font.SysFont("Arial", 20)
                    label = font.render(str(self.board[i][j]), 1, "green")
                    surface.blit(label, (self.left + self.cell_size *
                                 j + 5, self.top + self.cell_size * i + 5))
                    pygame.draw.rect(surface, wcolor[0], (self.left + self.cell_size * j, self.top + self.cell_size * i,
                                                          self.cell_size, self.cell_size), 1)

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
        i = floor((cell_coords[0] - 7) / self.cell_size) - \
            floor((self.left - 7) / self.cell_size)
        j = floor((cell_coords[1] - 7) / self.cell_size) - \
            floor((self.top - 7) / self.cell_size)
        if (i >= 0 and j >= 0) and (i < self.width and j < self.height):
            i = floor((cell_coords[0] - 7) / self.cell_size) - \
                floor((self.left - 7) / self.cell_size)
            j = floor((cell_coords[1] - 7) / self.cell_size) - \
                floor((self.top - 7) / self.cell_size)
            print((i, j))
            neighbors = self.count_neighbors(j, i)
            print(neighbors)
            self.board[j][i] = neighbors
            if self.board[j][i] == 0:
                self.open_cell()
        else:
            print(None)

    def count_neighbors(self, y, x):
        count = []
        if self.board[y][x] == 10:
            return None

        for i in range(self.height):  # equal y
            for j in range(self.width):  # equal x
                if self.board[i][j] == 10 and i == y - 1 and j == x:
                    count.append((i, j))
                elif self.board[i][j] == 10 and i == y + 1 and j == x:
                    count.append((i, j))
                elif self.board[i][j] == 10 and i == y and j == x - 1:
                    count.append((i, j))
                elif self.board[i][j] == 10 and i == y and j == x + 1:
                    count.append((i, j))
                elif self.board[i][j] == 10 and i == y - 1 and j == x - 1:
                    count.append((i, j))
                elif self.board[i][j] == 10 and i == y - 1 and j == x + 1:
                    count.append((i, j))
                elif self.board[i][j] == 10 and i == y + 1 and j == x - 1:
                    count.append((i, j))
                elif self.board[i][j] == 10 and i == y + 1 and j == x + 1:
                    count.append((i, j))

        return len(list(set(count)))

    def open_cell(self):
        for x in range(self.width):
            for y in range(self.height):
                if self.board[y][x] != 10:
                    nb = self.count_neighbors(y, x)
                    self.board[y][x] = nb
                


class Minesweeper(Board):
    def __init__(self, width, height, mine_count):
        super().__init__(abs(width), abs(height))
        self.mine_count = mine_count
        self.board = [[-1] * self.width for _ in range(self.height)]
        for _ in range(mine_count):
            i, j = random.randrange(
                0, self.height - 1), random.randrange(0, self.width - 1)
            self.board[i][j] = 10


pygame.init()
size = 500, 500
screen = pygame.display.set_mode(size)
board = Minesweeper(8, 8, 9)
board.set_view(7, 7, 50)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.on_click(event.pos)
    screen.fill((0, 0, 0))
    board.render(screen)
    pygame.display.flip()
pygame.quit()
