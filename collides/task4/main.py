import pygame


class Mountain(pygame.sprite.Sprite):
    image = pygame.image.load("mountains.png")

    def __init__(self):
        super().__init__()
        self.image = Mountain.image
        self.rect = self.image.get_rect(topleft=(0, 0))
        # вычисляем маску для эффективного сравнения
        self.mask = pygame.mask.from_surface(self.image)
        # располагаем горы внизу
        self.rect.bottom = height


class Landing(pygame.sprite.Sprite):
    image = pygame.image.load("pt.png")
    m_im = pygame.image.load("mountains.png")

    def __init__(self, pos):
        super().__init__()
        self.image = Landing.image
        self.rect = self.image.get_rect()
        # вычисляем маску для эффективного сравнения
        self.mask = pygame.mask.from_surface(self.image)
        self.mn = pygame.mask.from_surface(self.m_im)
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.speed = 1

    def update(self):
        self.rect.y += self.speed
    
        if pygame.sprite.collide_mask(self, Mountain()):
            self.speed = 0
        


pygame.init()
size = width, height = 700, 500
screen = pygame.display.set_mode(size)
mountain = pygame.sprite.Group(Mountain())
fps = 100
clock = pygame.time.Clock()
running = True
lands = pygame.sprite.Group()
while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
         
        if event.type == pygame.MOUSEBUTTONDOWN:
            lands.add(Landing(event.pos))

    mountain.draw(screen)
    mountain.update()
    lands.draw(screen)
    lands.update()
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()
