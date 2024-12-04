from abc import ABC
import Enemies
import random
#from lab4 import WeaponEquipmentFacade
#from lab4 import WeaponToEnemyAdapter
import Character


class Location(ABC):

    @staticmethod
    def spawn_enemy():
        pass


class Forest(Location):

    @staticmethod
    def spawn_enemy():
        return Enemies.Goblin()


class DragonBarrow(Location):
    @staticmethod
    def spawn_enemy():
        return Enemies.Dragon()

'''class HauntedManor(Location):
    def __init__(self):
        self._random_class = random.choice(list(Character.Character))
        self._weapon_equipment_facade = WeaponEquipmentFacade.WeaponEquipmentFacade().facade(self._random_class)

    @staticmethod
    def spawn_enemy():
        weapon = WeaponEquipmentFacade.WeaponEquipmentFacade().get_weapon()
        enchanted_weapon = WeaponToEnemyAdapter.WeaponToEnemyAdapter(weapon)
        return enchanted_weapon'''





