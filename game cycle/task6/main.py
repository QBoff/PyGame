import pygame
import sys
from math import sin, cos, radians


class Blade:
    def __init__(self, startX, startY, angle=0, radius=70) -> None:
        self.__startX = startX
        self.__startY = startY
        self.__radius = 70
        self.__angle = angle

    def calculateRotatedVectorEndPos(self) -> tuple[float, float]:
        rAngle = radians(self.__angle)
        x = self.__startX + self.__radius * cos(rAngle)
        y = self.__startY + self.__radius * sin(rAngle)

        return x, y

    def drawOn(self, screen):
        pygame.draw.polygon(screen, pygame.Color('Gray'), self.getCoords())

    def rotateBy(self, angle):
        self.__angle += angle

    def getCoords(self):
        self.__angle -= 15
        leftPoint = self.calculateRotatedVectorEndPos()

        self.__angle += 30
        rightPoint = self.calculateRotatedVectorEndPos()

        self.__angle -= 15

        return (self.__startX, self.__startY), leftPoint, rightPoint


class Game:
    FPS = 60

    def __init__(self, width, height) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Untitled')
        pygame.display.update()

        self.x0 = self.y0 = 100.5
        self.bladeRotationSpeed = 0
        self.blades = list()

        pygame.draw.circle(self.screen, pygame.Color('Gray'), (self.x0, self.y0), 10)
        for angle in (0, 120, 240):
            blade = Blade(self.x0, self.y0, angle)
            self.blades.append(blade)

    def run(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left
                        self.bladeRotationSpeed += 50
                    elif event.button == 3:  # Right
                        self.bladeRotationSpeed -= 50

            dt = self.clock.tick(self.FPS)
            self.screen.fill(0)
            pygame.draw.circle(self.screen, pygame.Color('Gray'), (self.x0, self.y0), 10)
            for blade in self.blades:
                blade.rotateBy(self.bladeRotationSpeed * dt / 1000)
                blade.drawOn(self.screen)

            pygame.display.update()


if __name__ == "__main__":
    mainWindow = Game(201, 201)
    mainWindow.run()