import pygame
import random

if __name__ == '__main__':
    global pos
    pygame.init()

    width, height = random.randrange(600, 900), random.randrange(600, 900)
    size = width, height
    screen = pygame.display.set_mode(size)
    running = True
    st1 = 0
    st2 = True
    clock = pygame.time.Clock()
    while running:
        screen.fill((0, 0, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                st1 = 0
                st2 = False
        while not st2:
            pygame.draw.circle(screen, (255, 255, 0), pos, st1)
            pygame.display.flip()
            st1 += 10
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    st2 = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    screen.fill((0, 0, 255))
                    pygame.display.flip()
                    pos = event.pos
                    st1 = 0
    pygame.quit()