from silverware import Silverware
from abc import ABC, abstractmethod

class Fork(Silverware):
    """
    """

    NAME = "fork"
    def pin(self):
        pass

    def stab_someone(self):
        pass

    def curl_spaghetti(self):
        pass

    def eat_with(self):
        return "Curling pasta with a fork"