import pygame


def draw(screen):
    screen.fill((255, 255, 255))

    brickw = 30
    brickh = 15
    step = 2
    xstart, ystart = 0, 0
    for i in range(13):
        if i % 2 == 0:
            for j in range(10):
                pygame.draw.rect(screen, pygame.Color("red"),
                                 (xstart, ystart, brickw, brickh))
                xstart += brickw + step
            ystart += brickh + step
            xstart = 0
        else:
            pygame.draw.rect(screen, pygame.Color("red"),
                             (xstart, ystart, brickw // 2, brickh))
            xstart += brickw // 2 + step
            for j in range(9):
                pygame.draw.rect(screen, pygame.Color("red"),
                                 (xstart, ystart, brickw, brickh))
                xstart += brickw + step
            ystart += brickh + step
            xstart = 0


if __name__ == '__main__':
    # инициализация Pygame:
    pygame.init()
    # размеры окна:
    try:
        WIDTH, HEIGHT = 300, 200
        SIZE = WIDTH, HEIGHT
    except ValueError:
        print("Неправильный формат ввода")
        quit()
    # WIDTH = 700
    # n = 100
    # SIZE = WIDTH, WIDTH
    # screen — холст, на котором нужно рисовать:
    screen = pygame.display.set_mode(SIZE)

    draw(screen)

    pygame.display.flip()
    # ожидание закрытия окна:
    while pygame.event.wait().type != pygame.QUIT:
        pass
    # завершение работы:
    pygame.quit()
