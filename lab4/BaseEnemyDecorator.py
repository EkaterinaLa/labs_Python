from lab3 import Logger, Enemy


class BaseEnemyDecorator(Enemy):
    def __init__(self, wrapee):
        self._wrapee = wrapee
        self._logger = Logger.GameLog.get_instance()

    def get_name(self):
        return self._wrapee.get_name()

    def get_health(self):
        return self._wrapee.get_health()

    def is_alive(self):
        return self._wrapee.is_alive()

    def take_damage(self, damage):
        return self._wrapee.take_damage(damage)

    def attack(self, player):
        return self._wrapee.attack(player)


class LegendaryEnemyDecorator(BaseEnemyDecorator):
    def __init__(self, wrapee):
        super().__init__(wrapee)
        self._logger = Logger.GameLog.get_instance()
        self._additional_damage = 20

    def get_name(self):
        return f'Легендарный {self._wrapee.get_name()}'

    def attack(self, player):
        self._wrapee.attack(player)
        self._logger.log('Враг легендарный и наносит дополнительный урон!!!')
        player.take_damage(self._additional_damage)


class WindfuryEnemyDecorator(BaseEnemyDecorator):
    def __init__(self, wrapee):
        super().__init__(wrapee)
        self._logger = Logger.GameLog.get_instance()

    def get_name(self):
        return f'Обладающий Неистовством Ветра {self._wrapee.get_name()}'

    def attack(self, player):
        self._wrapee.attack(player)
        self._logger.log('Неистовство ветра позволяет врагу атаковать второй раз!!!')
        self._wrapee.attack(player)


