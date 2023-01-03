import pygame
import random
import sys


class Cell:
    variants = {
        'Tile': 'Black',
        'Wall': 'Blue',
        'Ball': 'Red'
    }

    def __init__(self, state='Tile') -> None:
        self.setState(state)

    @classmethod
    def getRandom(cls):
        return cls(random.choice(cls.variants.keys()))

    def setState(self, state):
        self.state = state
        self.color = self.variants[state]

    def __eq__(self, other):
        return self.state == other.state

    def __ne__(self, other):
        return self.state != other.state

    def __repr__(self) -> str:
        return '-' if self.state == 'Tile' else '=' if self.state == 'Wall' else '*'


class Board:
    def __init__(self, rows, columns):
        self.left = 0
        self.top = 0
        try:
            self.width = abs(columns)
            self.height = abs(rows)
        except (ValueError, TypeError) as e:
            print("Input correct type!")
            print(e)
            quit()
        self.cell_size = 30
        self.board = self.getBoard()

    def getBoard(self):
        blocks = list()
        for _ in range(self.width):
            block = list()
            for _ in range(self.height):
                block.append(Cell())
            blocks.append(block)
        return blocks

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def get_click(self, pos):
        offsetPos = (pos[0] - self.left, pos[1] - self.top)
        coords = (offsetPos[0] // self.cell_size,
                  offsetPos[1] // self.cell_size)
        if 0 <= coords[0] < self.width and 0 <= coords[1] < self.height:
            return coords
        return None

    def getSurrouning(self, pos):
        posSet = set()

        posSet.add((pos[0] - 1, pos[1]))
        posSet.add((pos[0] + 1, pos[1]))
        posSet.add((pos[0], pos[1] - 1))
        posSet.add((pos[0], pos[1] + 1))

        return tuple(filter(lambda x: self.width > x[0] > -1 and self.height > x[1] > -1, posSet))

    def render(self, screen):
        for x in range(self.width):
            for y in range(self.height):
                xPos = self.left + self.cell_size * x
                yPos = self.top + self.cell_size * y
                rect = pygame.Rect(xPos, yPos, self.cell_size, self.cell_size)
                pygame.draw.rect(screen, 'Gray', rect, 1)


class Lines(Board):
    def __init__(self, rows, columns):
        super().__init__(rows, columns)
        self.traversed = list()
        self.found = False

    def has_path(self, x1, y1, x2, y2):
        self.traversed.clear()
        self.found = False
        cell1 = self.board[x1][y1]
        self.rec_path((x1, y1), (x2, y2))
        return self.found

    def render(self, screen):
        for x in range(self.width):
            for y in range(self.height):
                xPos = self.left + self.cell_size * x
                yPos = self.top + self.cell_size * y
                rect = pygame.Rect(xPos, yPos, self.cell_size, self.cell_size)
                pygame.draw.ellipse(screen, self.board[x][y].color, rect)
                pygame.draw.rect(screen, 'Gray', rect, 1)

    def rec_path(self, start, target):
        if self.found:
            return

        surrounding = self.getSurrouning(start)
        if target not in surrounding:
            for cell in surrounding:
                if cell not in self.traversed and self.board[cell[0]][cell[1]].state != 'Wall':
                    self.traversed.append(cell)
                    self.rec_path(cell, target)
        else:
            self.found = True


FPS = 30

pygame.init()
pygame.display.set_caption('Линеечки')
screen = pygame.display.set_mode((800, 800))
board = Lines(8, 7)
board.set_view(10, 10, 40)
board.render(screen)
red = None
clock = pygame.time.Clock()
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            cell_pos = board.get_click(event.pos)
            cell = board.board[cell_pos[0]][cell_pos[1]]

            if cell.state == 'Tile':
                if not red:
                    cell.setState('Wall')
                else:
                    if board.has_path(*red, *cell_pos):
                        board.board[red[0]
                                            ][red[1]].setState('Tile')
                        board.board[cell_pos[0]
                                            ][cell_pos[1]].setState('Wall')
                        red = None
            elif cell.state == 'Wall' and not red:
                cell.setState('Ball')
                red = cell_pos

    clock.tick(FPS)
    screen.fill(0)
    board.render(screen)
    pygame.display.update()
