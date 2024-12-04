from abc import ABC, abstractmethod


class Weapon(ABC):
    @abstractmethod
    def get_damage(self):
        pass

    @abstractmethod
    def use(self):
        pass
