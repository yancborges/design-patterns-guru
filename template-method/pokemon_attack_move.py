from abc import ABC, abstractmethod
import random


class AttackMove(ABC):

    def template_method(self):
        self.remove_pp()
        self.roll_accuracy()
        self.hook1()
        self.apply_stats()
        self.hook2()
        self.apply_damage()

    def remove_pp(self):
        print("PP -1")

    def roll_accuracy(self):
        print("Accuracy: ", random.randint(0,100))

    @abstractmethod
    def apply_stats(self):
        print("Poisoned")

    @abstractmethod
    def apply_damage(self):
        print("Fainted")

    def hook1(self):
        pass

    def hook2(self):
        pass

    

    

    

        
