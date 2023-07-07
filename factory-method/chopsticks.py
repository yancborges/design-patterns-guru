from silverware import Silverware
from abc import ABC, abstractmethod

class Chopsticks(Silverware):
    """
    """

    NAME = "chopsticks"
    def tie_hair(self):
        pass

    def stir_paint(self):
        pass

    def eat_with(self):
        return "Using chopsticks to eat"