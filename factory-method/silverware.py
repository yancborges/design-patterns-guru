from abc import ABC, abstractmethod

class SilverwareCreator(ABC):
    """
    """

    @abstractmethod
    def factory_method(self):
        """
        """

        pass

    def some_operation(self):
        silverware = self.factory_method()
        
        return f"{silverware.eat_with()}"


class Silverware(ABC):
    """
    """

    def eat_with(self):
        pass