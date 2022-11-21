import pygame


def draw(screen, a, n):
    screen.fill((0, 0, 0))

    if a % n != 0:
        print("Неправильный формат ввода")
        quit()
    else:
        x, y, step = 0, 0, a // n
        black = True

        for i in range(n):
            for j in range(n):
                if black:
                    pygame.draw.rect(screen, pygame.Color(
                        "black"), (x, y, x + step, y + step))
                    x += step
                    black = False
                else:
                    pygame.draw.rect(screen, pygame.Color(
                        "white"), (x, y, x + step, y + step))
                    x += step
                    black = True
            y += step
            x = 0


if __name__ == '__main__':
    # инициализация Pygame:
    pygame.init()
    # размеры окна:
    try:
        WIDTH = abs(int(input()))
        n = abs(int(input()))
        SIZE = WIDTH, WIDTH
    except ValueError:
        print("Неправильный формат ввода")
        quit()
    # WIDTH = 700
    # n = 100
    # SIZE = WIDTH, WIDTH
    # screen — холст, на котором нужно рисовать:
    screen = pygame.display.set_mode(SIZE)

    draw(screen, WIDTH, n)

    pygame.display.flip()
    # ожидание закрытия окна:
    while pygame.event.wait().type != pygame.QUIT:
        pass
    # завершение работы:
    pygame.quit()
