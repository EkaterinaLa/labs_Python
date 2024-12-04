from abc import ABC, abstractmethod


class Armor(ABC):
    @abstractmethod
    def get_defense(self):
        pass

    @abstractmethod
    def use(self):
        pass

