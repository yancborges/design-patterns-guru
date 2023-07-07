from abc import ABC, abstractmethod

class SilverwareCreator(ABC):

    @abstractmethod
    def factory_method(self):
        pass

    def pick_silverware(self):
        silverware = self.factory_method()
        
        return f"{silverware.eat_with()}"
    
    def clean(self):
        silverware = self.factory_method()

        return f"{silverware.clean()}"


class Silverware(ABC):
    """
    """

    @abstractmethod
    def eat_with(self):
        pass

    def clean(self):
        return f"{self.NAME} was clean"