import random
from game.utils.constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    LEFT,
    RIGHT,
    BULLET_ENEMY_TYPE,
)


class Enemy:
    Y_POS = 0
    SPEED_X = 5
    SPEED_Y = 2
    MOVE_X = [LEFT, RIGHT]
    INTERVAL = 100
    SHOOTING_TIME = 30

    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(
            image.get_width(), SCREEN_WIDTH - image.get_width()
        )
        self.rect.y = self.Y_POS
        self.move_x = random.choice(self.MOVE_X)
        self.index = 0
        self.shooting_time = 0
        self.is_visible = True
        self.is_alive = True

    def update(self, bullet_handler):
        self.index += 1
        self.shooting_time += 1

        self.shoot(bullet_handler)
        self.move()

        if self.rect.y > SCREEN_HEIGHT:
            self.is_visible = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move(self):
        self.rect.y += self.SPEED_Y
        if self.move_x == LEFT:
            self.rect.x -= self.SPEED_X

            if self.rect.x <= 0 or self.index > self.INTERVAL:
                self.move_x = RIGHT
                self.index = 0
        else:
            self.rect.x += self.SPEED_X

            if (
                self.rect.x >= SCREEN_WIDTH - self.image.get_width()
                or self.index > self.INTERVAL
            ):
                self.move_x = LEFT
                self.index = 0

    def shoot(self, bullet_handler):
        if self.shooting_time % self.SHOOTING_TIME == 0:
            bullet_handler.add_bullet(BULLET_ENEMY_TYPE, self.rect.center)
