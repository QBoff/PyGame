import pygame


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Движущийся круг 2')
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)

    clock = pygame.time.Clock()
    running = True
    radius = 0
    can = False
    while running:
        screen.fill((0, 0, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                radius = 0
                can = True
                pos = event.pos

            while can:
                pygame.draw.circle(screen, pygame.Color("yellow"), pos, radius)
                pygame.display.flip()
                radius += 10
                clock.tick(30)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        can = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        screen.fill((0, 0, 255))
                        pygame.display.flip()
                        pos = event.pos
                        radius = 0

    pygame.quit()
