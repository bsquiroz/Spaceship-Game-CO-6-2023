from game.components.power_ups.power_up import PowerUp
from game.utils.constants import BULLET_POWER_UP


class Missile(PowerUp):
    def __init__(self):
        self.image = BULLET_POWER_UP
        super().__init__(self.image)
