import pygame


if __name__ == '__main__':
    pygame.init()

    size = width, height = 200, 200
    screen = pygame.display.set_mode(size)

    running, moving = True, False
    count = 0

    font = pygame.font.Font(None, 25)
    text = font.render(str(count), True, pygame.Color("red"))
    text_rect = text.get_rect(center=(100, 100))
    screen.blit(text, text_rect)

    while running:
        # screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.WINDOWFOCUSLOST:
                count += 1
            if event.type == pygame.WINDOWFOCUSGAINED:
                screen.fill((0, 0, 0))

                font = pygame.font.Font(None, 25)
                text = font.render(str(count), True, pygame.Color("red"))
                text_rect = text.get_rect(center=(100, 100))
                screen.blit(text, text_rect)

        pygame.display.flip()
