from pokemon_attack_move import AttackMove
from dragon_dance import DragonDance
from surf import Surf


def perform_attack(attack):

    attack.template_method()


if __name__ == "__main__":
    print("Altaria used Dragon dance!")
    perform_attack(DragonDance())

    print("")

    print("Nidoking used Surf!")
    perform_attack(Surf())

