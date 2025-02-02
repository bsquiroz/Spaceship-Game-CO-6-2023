import pygame
import os

# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Other/shield.png"))

BG = pygame.image.load(os.path.join(IMG_DIR, "Other/Track.png"))

HEART = pygame.image.load(os.path.join(IMG_DIR, "Other/SmallHeart.png"))
HEART_RED = pygame.image.load(os.path.join(IMG_DIR, "Other/iconHeart.png"))

DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(
    os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png")
)
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))
BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
BULLET_POWER_UP = pygame.image.load(os.path.join(IMG_DIR, "Bullet/missile.png"))

ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
ENEMY_2 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png"))
ENEMY_BOSS = pygame.image.load(os.path.join(IMG_DIR, "Enemy/boss.png"))

ENEMY_ASTEROID = pygame.image.load(os.path.join(IMG_DIR, "Obstacles/asteroid.png"))
ENEMY_TRASH = pygame.image.load(os.path.join(IMG_DIR, "Obstacles/trash.png"))
ENEMY_COMET = pygame.image.load(os.path.join(IMG_DIR, "Obstacles/comet.png"))

FONT_STYLE = "freesansbold.ttf"

LEFT = "left"
RIGHT = "right"

BULLET_ENEMY_TYPE = "enemy"
BULLET_PLAYER_TYPE = "player"
BULLET_MISSILE = "missile"

COLORS = {
    "WHITE": (255, 255, 255),
    "BLUE": (0, 0, 255),
    "RED": (255, 0, 0),
    "GREEN": (0, 255, 0),
    "YELLOW": (244, 209, 96),
}
