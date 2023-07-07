from abc import abstractmethod
from pokemon_attack_move import AttackMove

class Surf(AttackMove):

    def apply_damage(self):
        print("-60 foe HP!")

    def apply_stats(self):
        pass