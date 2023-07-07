from silverware import Silverware, SilverwareCreator
from chopsticks import Chopsticks
from fork import Fork

class ChineseFoodCreator(SilverwareCreator):
    def factory_method(self):
        return Chopsticks()
    

class ItalianFoodCreator(SilverwareCreator):
    def factory_method(self):
        return Fork()