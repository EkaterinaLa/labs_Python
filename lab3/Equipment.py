from abc import ABC, abstractmethod


class EquipmentChest(ABC):
    @abstractmethod
    def get_weapon(self):
        pass

    @abstractmethod
    def get_armor(self):
        pass
