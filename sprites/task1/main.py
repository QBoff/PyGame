import pygame as pg
from os.path import join


pg.init()
size = 500, 500
screen = pg.display.set_mode(size)
running = True
all_im = pg.sprite.Group()
sprite = pg.sprite.Sprite(all_im)
sprite.image = pg.image.load(join("data", "arrow.png"))
sprite.rect = sprite.image.get_rect()


while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if pg.mouse.get_focused():

            all_im = pg.sprite.Group()
            sprite = pg.sprite.Sprite(all_im)
            sprite.image = pg.image.load(join("data", "arrow.png"))
            sprite.rect = sprite.image.get_rect()
            sprite.rect.center = pg.mouse.get_pos()
        else:
            all_im = pg.sprite.Group()

        screen.fill((0, 0, 0))

        all_im.draw(screen)
        all_im.update()

        pg.display.flip()
pg.quit()
#  ссылка на гит https://github.com/QBoff/PyGame/tree/master/sprites/task1
#  картинка в папке data в корневой папке
