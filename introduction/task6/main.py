import pygame


def draw(screen, n):
    screen.fill("yellow")
    
    newside = int(n * 1.4)
    yn = HEIGHT // newside
    xn = WIDTH // newside
    yl, yt, yr, yb = newside//2, 0, newside//2, newside
    xl, xt, xr, xb = 0, newside//2, newside, newside//2
    
    for j in range(xn):
        for i in range(yn):
            poly = [(xl, yl), (xt, yt), (xr, yr), (xb, yb)]
            pygame.draw.polygon(screen, pygame.Color("orange"), poly)
            
            yl += newside
            yt += newside
            yr += newside
            yb += newside
            
        yl, yt, yr, yb = newside//2, 0, newside//2, newside
        xl += newside
        xt += newside
        xr += newside
        xb += newside

    
    
    

if __name__ == '__main__':
    # инициализация Pygame:
    pygame.init()
    # размеры окна:
    try:
        WIDTH = 300
        HEIGHT = 724
        SIZE = WIDTH, HEIGHT
        n = input()  # size of my side
        while "." in n or "," in n or int(n) <= 0:
            print("Введите целое число!!!!!")
            n = input()
        n = int(n)

    except ValueError:
        print("Неправильный формат ввода")
        quit()
    
    screen = pygame.display.set_mode(SIZE)

    draw(screen, n)

    pygame.display.flip()
    # ожидание закрытия окна:
    while pygame.event.wait().type != pygame.QUIT:
        pass
    # завершение работы:
    pygame.quit()
