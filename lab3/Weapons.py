from weapon import Weapon
from Logger import GameLog
import random
import math


class Sword(Weapon):
    def __init__(self):
        self._damage = 20
        self._logger = GameLog.get_instance()

    def get_damage(self):
        return self._damage

    def use(self):
        return self._logger.log('Удар мечом!')


class Bow(Weapon):
    def __init__(self):
        self._damage = 15
        self._critical_chance = 0.3
        self._critical_modifier = 2
        self._logger = GameLog.get_instance()

    def get_damage(self):
        roll = random.random()
        if math.isclose(roll, self._critical_chance) <= 0:
            self._logger.log('Критический урон!')
            return self._damage * self._critical_modifier
        return self._damage

    def use(self):
        return self._logger.log('Выстрел из лука!')


class Staff(Weapon):
    def __init__(self):
        self._damage = 25
        self._scatter = 0.2
        self._logger = GameLog.get_instance()

    def get_damage(self):
        roll = random.random()
        factor = 1 + (roll * 2 * self._scatter - self._scatter)
        return int(round(self._damage * factor))

    def use(self):
        return self._logger.log('Воздух накаляется, из посоха вылетает огненный шар!')
