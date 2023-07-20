import pygame

from game.components.obstacles.obstacles import Obstacles
from game.utils.constants import ENEMY_TRASH


class Trash(Obstacles):
    SPEED_Y = 15

    def __init__(self):
        self.image = ENEMY_TRASH
        super().__init__(self.image)

    def update(self, player):
        remove_lives = 1

        if self.rect.colliderect(player.rect):
            player.lives -= remove_lives
            self.is_visible = False

            if player.lives <= 0:
                player.is_alive = False

        super().update()
