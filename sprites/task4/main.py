import pygame as pg
from random import randrange
import os.path


class Bomb(pg.sprite.Sprite):
    undetonated = pg.image.load(os.path.join('data', 'bomb.png'))
    detonated = pg.image.load(os.path.join('data', 'boom.png'))

    def __init__(self, x, y) -> None:
        super().__init__()
        self.image = self.undetonated.convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        self.isDetonated = False

    def detonate(self) -> None:
        if not self.isDetonated:
            self.isDetonated = True
            self.image = self.detonated.convert_alpha()
            self.rect = self.detonated.get_rect(center=self.rect.center)

    def update(self, pos) -> None:
        if self.rect.collidepoint(pos):
            self.detonate()


def make_bombs(amount):
    bombs = pg.sprite.Group()
    size = Bomb.undetonated.get_size()
    territory_for_sp = screen.get_rect().inflate(-size[0] // 2, -size[1] // 2)

    for i in range(amount):
        x = randrange(territory_for_sp.left,
                      territory_for_sp.left + territory_for_sp.width)
        y = randrange(territory_for_sp.top,
                      territory_for_sp.top + territory_for_sp.height)

        bomb = Bomb(x, y)
        bombs.add(bomb)

    return bombs


width, height = 600, 600
screen = pg.display.set_mode((width, height))
clock = pg.time.Clock()
bombs = make_bombs(10)

running = True
fps = 60

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            break
        if event.type == pg.MOUSEBUTTONDOWN:
            bombs.update(pg.mouse.get_pos())

    screen.fill((0, 0, 0))
    bombs.draw(screen)
    pg.display.flip()
    clock.tick(fps)
