import random, pygame
from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT


class Obstacles:
    Y_POS = 0
    SPEED_Y = 10
    WIDTH = 80
    HEIGHT = 80

    def __init__(self, image):
        self.image = image
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(
            self.image.get_width(), SCREEN_WIDTH - self.image.get_width()
        )
        self.rect.y = self.Y_POS
        self.is_visible = True

    def update(self):
        self.move()

        if self.rect.y > SCREEN_HEIGHT:
            self.is_visible = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move(self):
        self.rect.y += self.SPEED_Y
