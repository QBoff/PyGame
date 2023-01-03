import pygame
from collections import deque


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.colors = ["white", "blue", "red", "magenta"]
        self.is_red = False
        self.start = False
        self.start_pos = None
        self.goal_pos = None
        self.can = True
        

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, surface):
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j] == 0:
                    pygame.draw.rect(surface,
                                     self.colors[self.board[i][j]],
                                     (self.left + self.cell_size * j,
                                      self.top + self.cell_size * i,
                                      self.cell_size, self.cell_size), 1)
                else:
                    pygame.draw.rect(surface,
                                     self.colors[self.board[i][j]],
                                     (self.left + self.cell_size * j,
                                      self.top + self.cell_size * i,
                                      self.cell_size, self.cell_size), 0, border_radius=50)
                    pygame.draw.rect(surface,
                                     "white",
                                     (self.left + self.cell_size * j,
                                      self.top + self.cell_size * i,
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
        i = cell_coords[0] // self.cell_size - self.left // self.cell_size
        j = cell_coords[1] // self.cell_size - self.top // self.cell_size
        if (i >= 0 and j >= 0) and (i < self.width and j < self.height):
            i = cell_coords[0] // self.cell_size - self.left // self.cell_size
            j = cell_coords[1] // self.cell_size - self.top // self.cell_size
            print((i, j))
            # if self.can:
            if self.is_red:
                self.can = False
                self.goal_pos = (j, i)
                return
            elif int(self.board[j][i] + 1) % 3 == 2 and not self.is_red:
                self.board[j][i] = int(self.board[j][i] + 1) % 3
                self.start_pos = (j, i)
            else:
                self.board[j][i] = int(self.board[j][i] + 1) % 2

            if self.board[j][i] == 2:
                self.is_red = True
                # self.start_pos = (j, i)
                self.goal_pos = (j, i)
            
            if self.is_red:
                self.start = True
                # self.board[j][i] = 3
        else:
            print(None)

    def get_next_nodes(self, x, y):
        check_next_node = lambda x, y: True if 0 <= x < self.width and 0 <= y < self.height and not self.board[y][x] else False
        ways = [-1, 0], [0, -1], [1, 0], [0, 1]
        return [(x + dx, y + dy) for dx, dy in ways if check_next_node(x + dx, y + dy)]

    def bfs(start, goal, graph):
        queue = deque([start])
        visited = {start: None}

        while queue:
            cur_node = queue.popleft()
            if cur_node == goal:
                break

            next_nodes = graph[cur_node]
            for next_node in next_nodes:
                if next_node not in visited:
                    queue.append(next_node)
                    visited[next_node] = cur_node
        return queue, visited


class Lines(Board):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.grid = self.board
    
    def get_rect(self, x, y):
        return x * TILE + 1, y * TILE + 1, TILE - 2, TILE - 2


    def get_next_nodes(self, x, y):
        check_next_node = lambda x, y: True if 0 <= x < cols and 0 <= y < rows and not self.grid[y][x] else False
        ways = [-1, 0], [0, -1], [1, 0], [0, 1]
        return [(x + dx, y + dy) for dx, dy in ways if check_next_node(x + dx, y + dy)]


    def get_click_mouse_pos(self):
        x, y = pygame.mouse.get_pos()
        grid_x, grid_y = x // TILE, y // TILE
        pygame.draw.rect(screen, pygame.Color('red'), self.get_rect(grid_x, grid_y))
        click = pygame.mouse.get_pressed()
        return (grid_x, grid_y) if click[0] else False


    def bfs(self, start, goal, graph):
        queue = deque([start])
        visited = {start: None}

        while queue:
            cur_node = queue.popleft()
            if cur_node == goal:
                break

            next_nodes = graph[cur_node]
            for next_node in next_nodes:
                if next_node not in visited:
                    queue.append(next_node)
                    visited[next_node] = cur_node
        return queue, visited
    
    def get_red(self):
        for i, row in enumerate(self.grid):
            for j, col in enumerate(row):
                if self.grid[i][j] == 2:
                    return [j, i]


def get_graph(grid):
    graph = {}
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if not col:
                graph[(x, y)] = graph.get((x, y), []) + lines.get_next_nodes(x, y)
    
    return graph


cols, rows = 35, 20
TILE = 20  # будет вводить пользователь

pygame.init()
screen = pygame.display.set_mode([cols * TILE, rows * TILE])
clock = pygame.time.Clock()
lines = Lines(cols, rows)
lines.set_view(0, 0, TILE)
# grid

# dict of adjacency lists


# # BFS settings
# start = (0, 0)
# goal = start
# queue = deque([start])
# visited = {start: None}

while True:
    # fill screen
    screen.fill(pygame.Color('black'))
    # draw grid
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            lines.on_click(pygame.mouse.get_pos())
            grid = lines.grid
            graph = get_graph(grid)
            start = lines.get_red()
            print("Start")
            print(start)
            
            if not lines.can:
                mouse_pos = lines.get_click_mouse_pos()
                if mouse_pos and not lines.grid[mouse_pos[1]][mouse_pos[0]]:
                    queue, visited = lines.bfs(tuple(start[::-1]), mouse_pos[::-1], graph)
                    goal = mouse_pos
                    
                    path_head, path_segment = goal, goal
                    while path_segment and path_segment in visited:
                        # lines.board[goal[0]][goal[1]] = 2
                        pygame.draw.rect(screen, pygame.Color('white'), lines.get_rect(*path_segment), TILE, border_radius=TILE // 3)
                        path_segment = visited[path_segment]
                    pygame.draw.rect(screen, pygame.Color('blue'), lines.get_rect(*start), border_radius=TILE // 3)
                    pygame.draw.rect(screen, pygame.Color('magenta'), lines.get_rect(*path_head), border_radius=TILE // 3)
    # draw BFS work
    # [pg.draw.rect(sc, pg.Color('forestgreen'), get_rect(x, y)) for x, y in visited]
    # [pg.draw.rect(sc, pg.Color('darkslategray'), get_rect(x, y)) for x, y in queue]

    # bfs, get path to mouse click

    # draw path
    # pygame necessary lines
    # pygame necessary lines
    lines.render(screen)
    pygame.display.flip()
    clock.tick(30)