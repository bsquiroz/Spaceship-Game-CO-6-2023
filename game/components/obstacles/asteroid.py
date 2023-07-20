import pygame

from game.components.obstacles.obstacles import Obstacles
from game.utils.constants import ENEMY_ASTEROID


class Asteroid(Obstacles):
    def __init__(self):
        self.image = ENEMY_ASTEROID
        super().__init__(self.image)

    def update(self, player):
        remove_lives = 2

        if self.rect.colliderect(player.rect):
            player.lives -= remove_lives
            self.is_visible = False

            if player.lives <= 0:
                player.is_alive = False

        super().update()
