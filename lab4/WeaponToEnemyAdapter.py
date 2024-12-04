import math

from lab3 import Enemy, Logger, weapon
import random


class WeaponToEnemyAdapter(Enemy):
    def __init__(self, weapon):
        self._logger = Logger.GameLog.get_instance()
        self._name = 'Магическое оружие'
        self._health = 50
        self._weapon = weapon
        self._dispel_probability = 0.2

    def take_damage(self, damage):
        self._logger.log(f'{self._name} получает {damage} урона!')
        self._health -= damage
        dispel_roll = random.random()
        if math.isclose(dispel_roll, self._dispel_probability) <= 0:
            self._logger.log('Атака рассеяла заклятие с оружия!')
            self._health = 0

        if self._health > 0:
            self._logger.log(f'У {self._name} осталось {self._health} здоровья')

    def attack(self, player):
        self._logger.log(f'{self._name} атакует {player.name}')
        player.take_damage(self._weapon.get_damage())