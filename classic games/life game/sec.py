import pygame
import copy


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.next_blocks_stage = [
            [0 for l in range(width)] for j in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render_life(self, surface):
        life = Life(self.width, self.height)
        wcolor = pygame.Color("green")
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j]:
                    pygame.draw.rect(surface, "green", (self.left + self.cell_size * j, self.top + self.cell_size * i,
                                                        self.cell_size, self.cell_size), 1 if self.board[i][j] == 0 else 0)
                else:
                    pygame.draw.rect(surface, "white", (self.left + self.cell_size * j, self.top + self.cell_size * i,
                                                        self.cell_size, self.cell_size), 1 if self.board[i][j] == 0 else 0)

                self.next_blocks_stage[i][j] = life.paint_block(
                    self.board, (j - 1, i - 1))

        self.board = copy.deepcopy(self.next_blocks_stage)

    def render(self, surface):
        wcolor = pygame.Color("white")
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j]:
                    pygame.draw.rect(surface, "green", (self.left + self.cell_size * j, self.top + self.cell_size * i,
                                                        self.cell_size, self.cell_size), 1 if self.board[i][j] == 0 else 0)
                else:
                    pygame.draw.rect(surface, "white", (self.left + self.cell_size * j, self.top + self.cell_size * i,
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


pygame.init()
size = 500, 500
screen = pygame.display.set_mode(size)
board = Board(10, 12)
board.set_view(100, 100, 30)
running = True
start = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                start = not start

        if event.type == pygame.MOUSEBUTTONDOWN:
            if not start:
                board.on_click(event.pos)
                # board.board = board.next_blocks_stage

        screen.fill((0, 0, 0))
        if start:
            board.render_life(screen)
        else:
            board.render(screen)
        pygame.display.flip()
pygame.quit()
