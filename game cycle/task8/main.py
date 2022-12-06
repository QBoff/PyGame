import pygame


def read_from_file(name) -> list:
    with open(name, "r", encoding="utf8") as file:
        cor = []
        s, f = 0, 0
        src = file.readline()
        
        for i in range(len(src)):
            if src[i] == '(':
                s = i
            if src[i] == ')':
                f = i
                line = src[s + 1: f].split(';')
                if ',' in line[0]:
                    line[0] = line[0].replace(',', '.')
                if ',' in line[1]:
                    line[1] = line[1].replace(',', '.')
                cor.append([(float(line[0])), (float(line[1]))])
                s, f = 0, 0
        
    return cor


if __name__ == '__main__':
        
    pygame.init()
    coords = read_from_file("points.txt")
    
    size = width, height = 501, 501
    screen = pygame.display.set_mode(size)
    white = pygame.Color('white')
    black = pygame.Color('black')
    k = 1
    coords1 = []
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP and event.button == 4:
                k *= 2
            if event.type == pygame.MOUSEBUTTONUP and event.button == 5:
                k /= 2
        for i in coords:
            x, y = i[1], i[0]
            coords1.append([float(x * k + 250.5), float(y * k + 250.5)])
        screen.fill(black)
        pygame.draw.polygon(screen, white, coords1, 1)
        coords1 = []
        pygame.display.flip()
    
    read_from_file("points.txt")