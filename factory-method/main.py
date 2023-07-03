from silverware import SilverwareCreator
from food import ChineseFoodCreator, ItalianFoodCreator

def eat_dinner(creator):
    return f"{creator.some_operation()}"


if __name__ == "__main__":
    print("I would like an karage and some shrimp tempura")
    print(eat_dinner(ChineseFoodCreator()))

    print("")

    print("For my wife she'll get a carbonara")
    print(eat_dinner(ItalianFoodCreator()))