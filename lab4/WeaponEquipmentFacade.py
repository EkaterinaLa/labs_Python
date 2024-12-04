import sys
from lab3 import Equipments, Equipment


class WeaponEquipmentFacade:
    def __init__(self):
        self._equipment_chest = Equipment.EquipmentChest()

    def facade(self, character_class):
        if character_class == 'WIZARD':
            self._equipment_chest = Equipments.WizardEquipmentChest()
            sys.exit()
        elif character_class == 'WARRIOR':
            self._equipment_chest = Equipments.WarriorEquipmentChest()
            sys.exit()
        elif character_class == 'THIEF':
            self._equipment_chest = Equipments.ThiefEquipmentChest()
            sys.exit()
        else:
            raise Exception('такого игрового персонажа нет')

    def get_weapon(self):
        return self._equipment_chest.get_weapon()
