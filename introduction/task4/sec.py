import pygame
print('Введите N')
n = int(input())
print('Введите K')
k = int(input())

colors = [(0, 0, 255), (0, 255, 0),  (255, 0, 0)]

size = n
n += k * n

pygame.init()
sc = pygame.display.set_mode((300, 300))
z = 0
while k > z:
    pygame.draw.circle(sc, colors[z % 3], (150, 150), n - z * size)
    z = z + 1

pygame.display.update()

while 1:
    pygame.time.delay(1000)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
