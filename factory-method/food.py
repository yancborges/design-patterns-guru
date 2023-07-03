from silverware import Silverware, SilverwareCreator

class ChineseFoodCreator(SilverwareCreator):
    def factory_method(self):
        return ChineseFoodSilverware()
    

class ItalianFoodCreator(SilverwareCreator):
    def factory_method(self):
        return ItalianFoodSilverware()
    

class ChineseFoodSilverware(Silverware):
    def eat_with(self):
        return "Using chopsticks to eat"
    

class ItalianFoodSilverware(Silverware):
    def eat_with(self):
        return "Curling pasta with a fork"