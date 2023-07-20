import pygame
from game.utils.constants import (
    SPACESHIP,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    BULLET_PLAYER_TYPE,
    SPACESHIP_SHIELD,
)

from game.components.power_ups.shield import Shield
from game.components.power_ups.heart import Heart


class Spaceship:
    WIDTH = 40
    HEIGHT = 60
    X_POS = (SCREEN_WIDTH // 2) - WIDTH
    Y_POS = 500

    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.is_alive = True
        self.has_shield = False
        self.time_up = 0
        self.lives = 25

    def update(self, game_speed, user_input, handle_bullet):
        if user_input[pygame.K_LEFT]:
            self.move_left(game_speed)

        if user_input[pygame.K_RIGHT]:
            self.move_right(game_speed)

        if user_input[pygame.K_UP]:
            self.move_up(game_speed)

        if user_input[pygame.K_DOWN]:
            self.move_down(game_speed)

        if user_input[pygame.K_SPACE]:
            self.shoot(handle_bullet)

        if self.has_shield:
            time_to_show = round((self.time_up - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show < 0:
                self.deactivate_power_up()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move_left(self, game_speed):
        if self.rect.left < 0:
            self.rect.x = SCREEN_WIDTH
        self.rect.x -= game_speed

    def move_right(self, game_speed):
        if self.rect.right > SCREEN_WIDTH:
            self.rect.x = 0
        self.rect.x += game_speed

    def move_up(self, game_speed):
        if self.rect.top > SCREEN_HEIGHT / 2:
            self.rect.y -= game_speed

    def move_down(self, game_speed):
        if self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += game_speed

    def shoot(self, handle_bullet):
        handle_bullet.add_bullet(BULLET_PLAYER_TYPE, self.rect.center)

    def activate_power_up(self, power_up):
        self.time_up = power_up.time_up
        if type(power_up) == Shield:
            self.image = SPACESHIP_SHIELD
            self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
            self.has_shield = True

        if type(power_up) == Heart:
            self.lives += 5

    def deactivate_power_up(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        self.has_shield = False

    def reset(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.is_alive = True
        self.has_shield = False
        self.lives = 25
        self.time_up = 0
