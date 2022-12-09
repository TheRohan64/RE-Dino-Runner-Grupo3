from dino_runner.components.power_ups.power_up import PowerUp
from dino_runner.utils.constants import THUNDERBOLT, THUNDERBOLT_TYPE

class Thunderbolt(PowerUp):
    def __init__(self):
        super().__init__(THUNDERBOLT, THUNDERBOLT_TYPE)