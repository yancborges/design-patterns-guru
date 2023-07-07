from abc import abstractmethod
from pokemon_attack_move import AttackMove

class DragonDance(AttackMove):

    def apply_stats(self):
        print("Increased user's speed")
        print("Increased user's attack")

    def apply_damage(self):
        pass