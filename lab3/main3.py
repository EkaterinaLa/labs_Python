import math

import Equipments
import playable_character
import Logger
import Locations
import random
import sys
#from lab4 import BaseEnemyDecorator


if __name__ == '__main__':

    def getChest(characterClass):
        if characterClass == 'WARRIOR':
            return Equipments.WarriorEquipmentChest()
        elif characterClass == 'THIEF':
            return Equipments.ThiefEquipmentChest()
        elif characterClass == 'WIZARD':
            return Equipments.WizardEquipmentChest()
        else:
            raise Exception('недопустмый тип персонажа')

    def getLocation(location):
        if location == 'мистический лес':
            return Locations.Forest()
        elif location == 'логово дракона':
            return Locations.DragonBarrow()
        else:
            raise Exception('Такой локации нет')

    '''def addEnemyModifiers(enemy):
        decorator = BaseEnemyDecorator.BaseEnemyDecorator(enemy)
        modifier_probability = 0.3
        modifier_proc = math.isclose(modifier_probability, random.random()) <= 0
        if bool(random.getrandbits(1)) is True:
            decorator = BaseEnemyDecorator.LegendaryEnemyDecorator(decorator)
            if modifier_proc is True:
                decorator = BaseEnemyDecorator.WindfuryEnemyDecorator(decorator)
        else:
            decorator = BaseEnemyDecorator.WindfuryEnemyDecorator(decorator)
            if modifier_proc is True:
                decorator = BaseEnemyDecorator.LegendaryEnemyDecorator(decorator)
        return decorator'''


    char = input('Создайте своего персонажа: ')
    name = input('Введите имя: ')
    cl = input('Выберите класс из списка 【"WARRIOR"， "THIEF", "WIZARD"】')
    starting_equipment_chest = getChest(cl)
    starting_armor = starting_equipment_chest.get_armor()
    starting_weapon = starting_equipment_chest.get_weapon()

    player = playable_character.Builder().set_name(name)\
        .set_character_class(cl)\
        .set_weapon(starting_weapon)\
        .set_armor(starting_armor)\
        .set_health(cl)\
        .build()

    gameLogger = Logger.GameLog.get_instance()
    gameLogger.log(f'{player.name} очнулся на распутье!')

    loc = input('Куда вы двинетесь? Выберите локацию: (мистический лес, логово дракона, проклятый особняк) ')

    location = getLocation(loc)
    enemy = location.spawn_enemy()

    '''strong_enemy_name = bool(random.getrandbits(1))
    if strong_enemy_name is True:
        gameLogger.log(f'Боги особенно немилостивы к {player.name} , сегодня его ждет страшная битва...')
        enemy = addEnemyModifiers(enemy)'''

    gameLogger.log(f'У {player.name} на пути возникает {enemy.get_name()} , начинается бой!')

    while player.is_alive() is True and enemy.is_alive() is True:
        input('Введите что-нибудь чтобы атаковать! ')

        player.attack(enemy)

        stunned = bool(random.getrandbits(1))
        if stunned is True:
            gameLogger.log(f'{enemy.get_name()} был оглушен атакой {player.name}!')
            continue

        enemy.attack(player)

    print()

    if player.is_alive() is False:
        gameLogger.log(f'{player.name} был убит {enemy.get_name()}ом!')
        sys.exit()

    gameLogger.log(f'Злой {enemy.get_name()} был побежден! {player.name} отправился дальше по тропе судьбы...')














