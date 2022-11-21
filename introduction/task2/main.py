import pygame


def draw(screen):
    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, pygame.Color("red"),
                     (1, 1, WIDTH - 2, HEIGHT - 2))


if __name__ == '__main__':
    # инициализация Pygame:
    pygame.init()
    # размеры окна:
    try:
        WIDTH, HEIGHT = abs(int(input())), abs(int(input()))
        SIZE = WIDTH, HEIGHT
    except ValueError:
        print("Неправильный формат ввода")
        quit()
    # screen — холст, на котором нужно рисовать:
    screen = pygame.display.set_mode(SIZE)

    draw(screen)

    pygame.display.flip()
    # ожидание закрытия окна:
    while pygame.event.wait().type != pygame.QUIT:
        pass
    # завершение работы:
    pygame.quit()
