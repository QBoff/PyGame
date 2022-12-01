import pygame
import random


class Ball:
    def __init__(self, screen, x, y) -> None:
        self.screen = screen
        self.x = x
        self.y = y
        self.radius = 10
        self.XA = -0.7
        self.YA = -0.7

    def draw(self):
        pygame.draw.circle(self.screen, pygame.Color(
            "white"), (self.x, self.y), self.radius)
        self.move()
        # pygame.display.flip()

    def move(self):
        self.x += self.XA
        self.y += self.YA

        if self.x - self.radius <= 0 or self.x + self.radius >= width:
            self.XA *= -1

        if self.y - self.radius <= 0 or self.y + self.radius >= height:
            self.YA *= -1


class Balls(Ball):
    def __init__(self) -> None:
        self.balls = []

    def append(self, ball):
        self.balls.append(ball)

    def drawAll(self):
        for elem in self.balls:
            elem.draw()


if __name__ == '__main__':
    pygame.init()
    size = width, height = random.randrange(
        500, 800), random.randrange(500, 800)
    screen = pygame.display.set_mode(size)

    running = True
    span = False
    clock = pygame.time.Clock()
    balls = Balls()
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                ball = Ball(screen, event.pos[0], event.pos[1])
                balls.append(ball)

        balls.drawAll()

        pygame.display.flip()

    pygame.quit()
