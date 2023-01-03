import pygame as pg
from os.path import join


class Car(pg.sprite.Sprite):
    def __init__(self, *group) -> None:
        super().__init__(*group)
        self.image = pg.image.load(join("data", "car2.png"))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.speed = 5

    def move(self):
        self.rect.x += self.speed

    def reverse(self):
        if (self.rect.x + self.rect.width) >= size[0] or \
                (self.rect.x + self.image.get_rect()[0]) <= self.image.get_rect()[0]:

            self.image = pg.transform.flip(self.image, True, False)
            self.speed *= -1

    def update(self) -> None:
        self.move()
        self.reverse()


pg.init()
size = 600, 95
screen = pg.display.set_mode(size)
park = pg.sprite.Group()
car = Car()
park.add(car)
running = True
clock = pg.time.Clock()
fps = 80


while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill((255, 255, 255))
    park.draw(screen)
    park.update()
    pg.display.flip()
    clock.tick(fps)

pg.quit()
#  ссылка на гит https://github.com/QBoff/PyGame/tree/master/sprites/task3
#  картинка в папке data в корневой папке https://github.com/QBoff/PyGame
