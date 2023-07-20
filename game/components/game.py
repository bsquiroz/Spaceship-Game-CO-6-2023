import pygame

from game.utils.constants import (
    BG,
    ICON,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    TITLE,
    FPS,
    COLORS,
    HEART_RED,
)

from game.components.spaceship import Spaceship
from game.components.enemies.enemy_handler import EnemyHandler
from game.components.asteroid import Asteorid
from game.components.bullets.bullet_handler import BulletHandler
from game.components.power_ups.power_up_handler import PowerUpHandler
from game.utils import text_utils


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = Spaceship()
        self.enemy_handler = EnemyHandler()
        self.asteroid = Asteorid()
        self.bullet_handler = BulletHandler()
        self.power_up_handler = PowerUpHandler()
        self.score = 0
        self.number_deaths = 0
        self.score_record = 0
        self.light_years = 0
        self.light_years_record = 0

    def run(self):
        # Game loop: events - update - draw
        self.running = True
        while self.running:
            self.events()
            self.update()
            self.draw()
        pygame.display.quit()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN and not self.playing:
                self.reset()

    def update(self):
        if self.playing:
            user_input = pygame.key.get_pressed()
            self.player.update(self.game_speed, user_input, self.bullet_handler)
            self.enemy_handler.update(self.bullet_handler)
            self.bullet_handler.update(self.player, self.enemy_handler.enemies)
            self.power_up_handler.update(self.player)
            self.score = self.enemy_handler.enemies_destroyed
            self.asteroid.update()

            self.light_years += 1

            if not self.player.is_alive:
                pygame.time.delay(500)
                self.playing = False
                self.number_deaths += 1

                self.history_game()

    def draw(self):
        self.draw_background()

        if self.playing:
            self.clock.tick(FPS)
            self.player.draw(self.screen)
            self.enemy_handler.draw(self.screen)
            self.bullet_handler.draw(self.screen)
            self.power_up_handler.draw(self.screen)
            self.draw_score()
            self.draw_light_years()
            self.draw_lifes()
            self.asteroid.draw(self.screen)
        else:
            self.draw_menu()

        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed

    def draw_menu(self):
        if self.number_deaths == 0:
            text, text_rect = text_utils.get_message(
                "Press any Key to Start", 30, COLORS["WHITE"]
            )
            self.screen.blit(text, text_rect)
        else:
            text, text_rect = text_utils.get_message(
                "Press any Key to play again", 30, COLORS["WHITE"]
            )
            score, score_rect = text_utils.get_message(
                f"Your score is: {self.score}",
                30,
                COLORS["WHITE"],
                height=SCREEN_HEIGHT // 2 + 50,
            )
            light_years, light_years_rect = text_utils.get_message(
                f"Your distance is: {self.light_years} light years",
                30,
                COLORS["WHITE"],
                height=SCREEN_HEIGHT // 2 + 80,
            )
            score_record, score_record_rect = text_utils.get_message(
                f"Your record score is: {self.score_record}",
                20,
                COLORS["YELLOW"],
                height=SCREEN_HEIGHT // 2 + 110,
            )
            light_years_record, light_years_record_rect = text_utils.get_message(
                f"Your record light years is: {self.light_years_record}",
                20,
                COLORS["YELLOW"],
                height=SCREEN_HEIGHT // 2 + 140,
            )

            self.screen.blit(text, text_rect)
            self.screen.blit(score, score_rect)
            self.screen.blit(score_record, score_record_rect)
            self.screen.blit(light_years, light_years_rect)
            self.screen.blit(light_years_record, light_years_record_rect)

    def draw_score(self):
        score, score_rect = text_utils.get_message(
            f"Your score is: {self.score}", 20, COLORS["WHITE"], 1000, 40
        )
        self.screen.blit(score, score_rect)

    def draw_light_years(self):
        light_years, light_years_rect = text_utils.get_message(
            f"Distance {self.light_years}", 15, COLORS["WHITE"], 1010, 80
        )
        self.screen.blit(light_years, light_years_rect)

    def draw_lifes(self):
        self.image = HEART_RED
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 10
        self.screen.blit(self.image, self.rect)
        info_lifes, info_lives_rect = text_utils.get_message(
            f"x {self.player.lives}", 15, COLORS["WHITE"], 50, 20
        )
        self.screen.blit(info_lifes, info_lives_rect)

    def history_game(self):
        if self.score > self.score_record:
            self.score_record = self.score

        if self.light_years > self.light_years_record:
            self.light_years_record = self.light_years

    def reset(self):
        self.player.reset()
        self.enemy_handler.reset()
        self.bullet_handler.reset()
        self.power_up_handler.reset()
        self.score = 0
        self.light_years = 0
        self.playing = True
