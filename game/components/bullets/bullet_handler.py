from game.utils.constants import BULLET_ENEMY_TYPE, BULLET_PLAYER_TYPE
from game.components.bullets.bullet_enemy import BulletEnemy
from game.components.bullets.bullet_player import BulletPlayer


class BulletHandler:
    def __init__(self):
        self.bullets = []

    def update(self, player, enemies):
        for bullet in self.bullets:
            if type(bullet) == BulletEnemy:
                bullet.update(player)
            elif type(bullet) == BulletPlayer:
                for enemy in enemies:
                    bullet.update(enemy)

            if not bullet.is_alive or not bullet.is_visible:
                self.remove_bullet(bullet)

    def draw(self, screen):
        for bullet in self.bullets:
            bullet.draw(screen)

    def add_bullet(self, typeBullet, center):
        if typeBullet == BULLET_ENEMY_TYPE:
            self.bullets.append(BulletEnemy(center))

        if typeBullet == BULLET_PLAYER_TYPE:
            self.bullets.append(BulletPlayer(center))

    def remove_bullet(self, bullet):
        self.bullets.remove(bullet)
