import pygame as pg
from os.path import join


class GameOver(pg.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pg.image.load(join("data", "gameover.png"))
        self.rect = self.image.get_rect(topright=(-1, 0))
        self.speed = 20
        self.show = False

    def update(self, fps) -> None:
        if not self.show:
            self.rect.x += self.speed * fps / 100
            if self.rect.right > 600:
                self.rect.right = 600
                self.show = True


width, height = 600, 300
screen = pg.display.set_mode((width, height))
clock = pg.time.Clock()
running = True
fps = 60

gr = pg.sprite.Group()
go = GameOver()
gr.add(go)

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            break

    dt = clock.tick(fps)
    screen.fill((0, 0, 0))
    go.update(dt)
    gr.draw(screen)
    pg.display.flip()
