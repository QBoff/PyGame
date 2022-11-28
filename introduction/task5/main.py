import pygame


def draw(screen, n):
    screen.fill((0, 0, 0))

    outline = 1  # it's a const value in 1px
    freeSpace = WIDTH - outline * n
    step = freeSpace / 2 // n + 1
    yStart, yEnd = 0, 300
    xStart, xEnd = 0, 300
    for i in range(n):
        pygame.draw.ellipse(screen, pygame.Color("white"),
                            (0, yStart, 300, yEnd), width=outline)
        pygame.draw.ellipse(screen, pygame.Color("white"),
                            (xStart, 0, xEnd, 300), outline)
        pygame.display.flip()
        xStart += step
        xEnd -= 2 * step
        yStart += step
        yEnd -= 2 * step

    # for j in range(n):
    #     pygame.draw.ellipse(screen, pygame.Color("white"), (xStart, 0, xEnd, 300), outline)
    #     xStart += step
    #     xEnd -= 2 * step


if __name__ == '__main__':
    # инициализация Pygame:
    pygame.init()
    # размеры окна:
    try:
        WIDTH = 300
        SIZE = WIDTH, WIDTH
        n = input()
        while "." in n or "," in n or int(n) <= 0:
            print("Введите целое число!!!!!")
            n = input()
        n = int(n)

    except ValueError:
        print("Неправильный формат ввода")
        quit()
    # WIDTH = 700
    # n = 100
    # SIZE = WIDTH, WIDTH
    # screen — холст, на котором нужно рисовать:
    screen = pygame.display.set_mode(SIZE)

    draw(screen, n)

    pygame.display.flip()
    # ожидание закрытия окна:
    while pygame.event.wait().type != pygame.QUIT:
        pass
    # завершение работы:
    pygame.quit()
