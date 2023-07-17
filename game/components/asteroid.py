import pygame, random
from game.utils.constants import ENEMY_ASTEROID, SCREEN_WIDTH, SCREEN_HEIGHT


class Asteorid:
    Y_POS = 0
    SPEED_Y = 10
    WIDTH = 50
    HEIGHT = 50

    def __init__(self):
        self.image = ENEMY_ASTEROID
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(
            self.image.get_width(), SCREEN_WIDTH - self.image.get_width()
        )
        self.rect.y = self.Y_POS

    def update(self):
        self.move()

        if self.rect.y > SCREEN_HEIGHT:
            self.rect.y = self.Y_POS
            self.rect.x = random.randint(
                self.image.get_width(), SCREEN_WIDTH - self.image.get_width()
            )

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move(self):
        self.rect.y += self.SPEED_Y
