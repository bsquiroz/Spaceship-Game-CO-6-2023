import pygame
from game.components.bullets.bullet import Bullet
from game.utils.constants import BULLET_POWER_UP


class BulletPowerUp(Bullet):
    WIDTH = 32
    HEIGHT = 32
    SPEED = 5

    def __init__(self, center):
        self.image = BULLET_POWER_UP
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image, center)

    def update(self, enemy):
        if self.rect.bottom < 0:
            self.is_visible = False

        self.rect.y -= self.SPEED
        super().update(enemy)
