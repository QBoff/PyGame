import pygame


if __name__ == '__main__':
    pygame.init()

    size = width, height = 501, 501
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    fps = 90

    x, y = 251, 251
    x1, y1 = x, y
    running = True
    while running:
        screen.fill((0, 0, 0))
        pygame.draw.circle(screen, pygame.Color("red"), (x, y), 20)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                per = True
                x1, y1 = event.pos[0], event.pos[1]
            if event.type == pygame.QUIT:
                running = False

        if x1 > x:
            x += 1
        elif x1 < x:
            x -= 1

        if y1 > y:
            y += 1
        elif y1 < y:
            y -= 1

        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()
