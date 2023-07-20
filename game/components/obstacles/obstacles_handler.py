import random

from game.components.obstacles.asteroid import Asteroid
from game.components.obstacles.comet import Comet
from game.components.obstacles.trash import Trash


class ObstaclesHandler:
    def __init__(self):
        self.obstacles = []

    def update(self, player):
        self.add_obstacle()

        for obstacle in self.obstacles:
            obstacle.update(player)

            if not obstacle.is_visible:
                self.remove_obstacle(obstacle)

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def add_obstacle(self):
        if len(self.obstacles) < 1:
            self.obstacles.append(random.choice([Asteroid(), Comet(), Trash()]))

    def remove_obstacle(self, obstacle):
        self.obstacles.remove(obstacle)

    def reset(self):
        self.obstacles = []
