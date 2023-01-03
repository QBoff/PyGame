import pygame as pg
from os.path import join


pg.init()
size = 500, 500
screen = pg.display.set_mode(size)
running = True
playerg = pg.sprite.Group()
player = pg.sprite.Sprite(playerg)
player.image = pg.image.load(join("data", "player.png"))
player.rect = player.image.get_rect()
player.rect.x = 0
player.rect.y = 0


while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                player.rect.x -= 10
            if event.key == pg.K_RIGHT:
                player.rect.x += 10
            if event.key == pg.K_UP:
                player.rect.y -= 10
            if event.key == pg.K_DOWN:
                player.rect.y += 10

    screen.fill((0, 0, 0))
    playerg.draw(screen)
    playerg.update()
    pg.display.flip()
pg.quit()
#  ссылка на гит https://github.com/QBoff/PyGame/tree/master/sprites/task2
#  картинка в папке data в корневой папке https://github.com/QBoff/PyGame
