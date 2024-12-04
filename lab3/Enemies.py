from Enemy import Enemy
from Logger import GameLog
from playable_character import PlayableCharacter


class Goblin(Enemy):
    def __init__(self):
        super().__init__(name='', health=None, damage=None)
        self._name = 'Гоблин'
        self._health = 50
        self._damage = 10
        self._logger = GameLog.get_instance()


    @property
    def name(self):
        return self._name

    def take_damage(self, damage):
        self._logger.log(f'{self._name} получает {damage} урона!')
        self._health -= damage
        if self._health > 0:
            self._logger.log(f'У {self._name} осталось {self._health} здоровья!')

    def attack(self, player):
        self._logger.log(f'{self._name} атакует {player.name}!')
        player.take_damage(self._damage)


class Dragon(Enemy):
    def __init__(self):
        super().__init__(name='', health=None, damage=None)
        self._logger = GameLog.get_instance()
        self._resistance = 0.2
        self._name = 'Дракон'
        self._health = 100
        self._damage = 30

    def take_damage(self, damage):
        damage = round(damage * (1 - self._resistance))
        self._logger.log(f'{self._name} получает {damage} урона!')
        self._health -= damage
        if self._health > 0:
            self._logger.log(f'У {self._name} осталось {self._health} здоровья!')

    def attack(self, player):
        self._logger.log('Дракон дышит огнем!')
        player.take_damage(self._damage)


'''goblin = Goblin()
player = PlayableCharacter(builder)

goblin.attack(player)
player.take_damage(5)  # Пример урона, который игрок получает
goblin.take_damage(20)'''