import pygame

from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_BOSS


class Boss(Enemy):
    WIDTH = 200
    HEIGHT = 100
    SPEED_X = 10
    SPEED_Y = 0
    Y_POS = 50

    def __init__(self):
        self.image = ENEMY_BOSS
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        self.lives = 50
        super().__init__(self.image)
