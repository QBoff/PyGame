import pygame
import math


def draw_circle(screen):
    pygame.draw.circle(screen, pygame.Color("white"), (201 // 2, 201 // 2), 10)

def draw_triagls(screen):
    pygame.draw.polygon(screen, pygame.Color("white"), ((201 // 2,
                                                        201 // 2), 
                                                        (int(201//2 - 70 * math.sin(30) // 4),
                                                        int(201//2 + 70 * math.cos(15))),
                                                        (int(201//2 + 70 * math.sin(30) // 4),
                                                        int(201//2 + 70 * math.cos(15))),          
                                                        ))


if __name__ == '__main__':
    pygame.init()
    
    size = width, height = 201, 201
    screen = pygame.display.set_mode(size)
    
    running = True
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        draw_circle(screen)
        draw_triagls(screen=screen)
        pygame.display.update()
