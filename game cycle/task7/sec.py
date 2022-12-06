import pygame
import random


if __name__ == '__main__':
    pygame.init()
    size = width, height = random.randrange(
        500, 800), random.randrange(500, 800)
    screen = pygame.display.set_mode(size)

    running = True
    span = False
    clock = pygame.time.Clock()
    boxes = []
    mousepos = None
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mousepos = [event.pos[0], event.pos[1], 0, 0]

            if event.type == pygame.MOUSEBUTTONUP:
                boxes.append(mousepos)
                mousepos = None

            if event.type == pygame.MOUSEMOTION and mousepos != None:
                mousepos = [mousepos[0], mousepos[1], event.pos[0] -
                            mousepos[0], event.pos[1] - mousepos[1]]

            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if event.key == pygame.K_z and \
                        (event.mod & pygame.KMOD_CTRL):

                    if len(boxes) > 0:
                        del boxes[-1]
                    # print(0)

        for box in boxes:
            pygame.draw.rect(screen, (155, 155, 155), box, 1)

        if mousepos != None:
            pygame.draw.rect(screen, (155, 155, 155), mousepos, 1)

        pygame.display.flip()
        clock.tick(1000)

    pygame.quit()
