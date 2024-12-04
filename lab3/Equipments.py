from Equipment import EquipmentChest
from Weapons import Sword, Bow, Staff
from Armors import HeavyArmor, LightArmor, Robe


class WarriorEquipmentChest(EquipmentChest):
    def get_weapon(self):
        return Sword()

    def get_armor(self):
        return HeavyArmor()


class ThiefEquipmentChest(EquipmentChest):
    def get_weapon(self):
        return Bow()

    def get_armor(self):
        return LightArmor()


class WizardEquipmentChest(EquipmentChest):
    def get_weapon(self):
        return Staff()

    def get_armor(self):
        return Robe()
