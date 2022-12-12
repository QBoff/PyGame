import pygame


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.player = 1

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, surface):
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j] == 1:
                    pygame.draw.line(surface,
                                     "blue",
                                     (self.left + self.cell_size * j + 10,
                                      self.top + self.cell_size * i + 10),
                                     (self.left + self.cell_size * (j + 1) - 10,
                                      self.top + self.cell_size * (i + 1) - 10)
                                     )
                    pygame.draw.line(surface,
                                     "blue",
                                     (self.left + self.cell_size * j + 10,
                                      self.top + self.cell_size * (i + 1) - 10),
                                     (self.left + self.cell_size * (j + 1) - 10,
                                      self.top + self.cell_size * i + 10),
                                     )
                elif self.board[i][j] == 2:
                    pygame.draw.ellipse(surface,
                                        "red",
                                        (self.left + self.cell_size * j + 5,
                                         self.top + self.cell_size * i + 5,
                                         self.cell_size - 10, self.cell_size - 10),
                                        1
                                        )

                pygame.draw.rect(surface,
                                 "white",
                                 (self.left + self.cell_size * j,
                                     self.top + self.cell_size * i,
                                     self.cell_size, self.cell_size),
                                 1)

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
            if self.board[j][i] == 0:
                self.board[j][i] = self.player
                if self.player == 1:
                    self.player += 1
                elif self.player == 2:
                    self.player -= 1
                print(self.board)
        else:
            print(None)


pygame.init()
size = 500, 500
screen = pygame.display.set_mode(size)
board = Board(4, 7)
board.set_view(100, 100, 50)
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
