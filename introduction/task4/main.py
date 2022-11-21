import pygame


def draw(screen, a, n):
    screen.fill((0, 0, 0))

    if a % n != 0:
        print("Неправильный формат ввода")
        quit()
    else:
        r, step = a // n, a // n
        colors = ["red", "blue", "green"]
        r = a // 2
        for i in range(a // n):
            pygame.draw.circle(screen, pygame.Color(
                colors[i % 3]), (a // 2, a//2), r)
            r -= n


if __name__ == '__main__':
    # инициализация Pygame:
    pygame.init()
    # размеры окна:
    try:
        print("Введите толщину кольца: ")
        w = abs(int(input()))
        print("Введите кольчество колец: ")
        n = abs(int(input()))
        WIDTH = w * n * 2
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
