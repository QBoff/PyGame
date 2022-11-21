import pygame


def draw(screen):
    screen.fill((0, 0, 0))

    pygame.draw.line(screen, pygame.Color("white"), (0, 0), (WIDTH, HEIGHT))
    pygame.draw.line(screen, pygame.Color("white"), (0, HEIGHT), (WIDTH, 0))


if __name__ == '__main__':
    # инициализация Pygame:
    pygame.init()
    # размеры окна:
    SIZE = WIDTH, HEIGHT = 800, 600
    # screen — холст, на котором нужно рисовать:
    screen = pygame.display.set_mode(SIZE)

    draw(screen)
    
    pygame.display.flip()
    # ожидание закрытия окна:
    while pygame.event.wait().type != pygame.QUIT:
        pass
    # завершение работы:
    pygame.quit()
