import pygame

from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_2


class ShipSmall(Enemy):
    WIDTH = 20
    HEIGHT = 30
    SPEED_X = 10
    SPEED_Y = 4

    def __init__(self):
        self.image = ENEMY_2
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image)
