from abc import ABC, abstractmethod


class Enemy(ABC):
    def __init__(self, name, health, damage):
        self._name = name
        self._health = health
        self._damage = damage

    def get_name(self):
        return self._name

    def get_health(self):
        return self._health

    def take_damage(self, damage):
        pass

    @abstractmethod
    def attack(self, player):
        pass

    def is_alive(self):
        return self._health > 0


