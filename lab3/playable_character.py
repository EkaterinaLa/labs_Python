from Equipment import EquipmentChest
from Logger import GameLog
from Character import CharacterClass
from armor import Armor
from weapon import Weapon
import Weapons


class PlayableCharacter:
    def __init__(self):
        self._logger = GameLog.get_instance()
        self._name = None
        self._character_class = None
        self._health = None
        self._weapon = None
        self._armor = None

    @property
    def health(self):
        return self._health

    def take_damage(self, damage):
        reduced_damage = round(damage * (1 - self._armor.get_defense()))
        if reduced_damage < 0:
            reduced_damage = 0
        self._health -= reduced_damage
        self._armor.use()
        self._logger.log(f'{self._name} получил урон: {reduced_damage}')
        if self._health > 0:
            self._logger.log(f'у {self._name} осталось {self._health} здоровья')

    def attack(self, enemy):
        self._logger.log(f'{self._name} атакует врага {enemy.get_name()}')
        self._weapon.use()
        enemy.take_damage(self._weapon.get_damage())

    def is_alive(self):
        return self._health > 0

    @property
    def name(self):
        return self._name


class Builder:
    def __init__(self):
        self._playable = PlayableCharacter()

    def set_name(self, name):
        self._playable._name = name
        return self

    def set_character_class(self, character_class):
        self._playable._character_class = character_class
        #print(character_class)
        return self

    def set_health(self, character_class):
        self._playable._health = CharacterClass.get_starting_health(character_class)
        return self

    def set_weapon(self, weapon):
        self._playable._weapon = weapon
        return self

    def set_armor(self, armor):
        self._playable._armor = armor
        return self

    def build(self):
        return self._playable











