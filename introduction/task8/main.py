import os

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame


def draw_cube():
    nx = 130 - (k / 2)
    ny = 180 - (k / 2)
    k2 = k / 2

    color = pygame.Color(255, 255, 255)
    hsv = color.hsva
    color2 = pygame.Color(255, 255, 255)
    hsv2 = color2.hsva
    color3 = pygame.Color(255, 255, 255)
    hsv3 = color3.hsva

    color.hsva = (hue, hsv[1] + 100, hsv[2] - 25, hsv[3])
    color2.hsva = (hue, hsv2[1] + 100, hsv2[2], hsv[3])
    color3.hsva = (hue, hsv3[1] + 100, hsv3[2] - 50, hsv[3])

    pygame.draw.polygon(screen, color, ((nx, ny), (nx + k, ny),
                                        (nx + k, ny + k), (nx, ny + k)))

    pygame.draw.polygon(screen, color2, ((nx + k2, ny - k2), (nx + k2 + k, ny - k2),
                                         (nx + k, ny), (nx, ny)))

    pygame.draw.polygon(screen, color3,
                        ((nx + k, ny), (nx + k2 + k, ny - k2),
                         (nx + k2 + k, ny + k2), (nx + k, ny + k)))



while True:
    try:
        k, hue = [int(i) for i in input('Введите размер стороны куба и его оттенок через пробел: ').split()]
        break
    except:
        print('Произошла ошибка. Попробуйте еще раз')

pygame.init()
screen = pygame.display.set_mode((300, 300))
while pygame.event.wait().type != pygame.QUIT:
    draw_cube()
    pygame.display.flip()
pygame.quit()