from armor import Armor
from Logger import GameLog


class HeavyArmor(Armor):
    def __init__(self):
        self.__defense = 0.3
        self.__logger = GameLog.get_instance()

    def get_defense(self):
        return self.__defense

    def use(self):
        self.__logger.log('Тяжелая броня блокирует значительную часть урона')



class LightArmor(Armor):
    def __init__(self):
        self.__defense = 0.2
        self.__logger = GameLog.get_instance()

    def get_defense(self):
        return self.__defense

    def use(self):
        self.__logger.log('Легкая броня блокирует урон')


class Robe(Armor):
    def __init__(self):
        self.__defense = 0.1
        self.__logger = GameLog.get_instance()

    def get_defense(self):
        return self.__defense

    def use(self):
        self.__logger.log('Роба блокирует немного урона')
