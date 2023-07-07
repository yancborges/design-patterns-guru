from silverware import SilverwareCreator
from food import ChineseFoodCreator, ItalianFoodCreator

def start_dinner(creator):
    return f"{creator.pick_silverware()}"


def clean_silverware(creator):
    return f"{creator.clean()}"


if __name__ == "__main__":
    print("I would like an karage and some shrimp tempura")
    print(start_dinner(ChineseFoodCreator()))

    print("")

    print("For my wife she'll get a carbonara")
    print(start_dinner(ItalianFoodCreator()))

    print("")

    print(clean_silverware(ChineseFoodCreator()))
    print(clean_silverware(ItalianFoodCreator()))

