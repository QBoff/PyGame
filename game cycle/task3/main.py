import pygame


if __name__ == '__main__':
    pygame.init()

    size = width, height = 300, 300
    screen = pygame.display.set_mode(size)
    x, y = 0, 0
    pygame.draw.rect(screen, pygame.Color("green"), (x, y, 100, 100))

    running, moving = True, False

    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if x < event.pos[0] < x + 100 and y < event.pos[1] < y + 100:
                    moving = True

            if event.type == pygame.MOUSEMOTION:
                if moving:
                    pos = event.rel
                    x, y = x + pos[0], y + pos[1]

            if event.type == pygame.MOUSEBUTTONUP:
                moving = False

        pygame.draw.rect(screen, pygame.Color("green"), (x, y, 100, 100))

        pygame.display.flip()
