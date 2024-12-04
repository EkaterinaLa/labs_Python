from enum import Enum


class Character(Enum):
    WARRIOR = 100
    THIEF = 90
    WIZARD = 80


class CharacterClass:
    @staticmethod
    def get_starting_health(character_class):
        if character_class == 'WARRIOR':
            return Character.WARRIOR.value

        elif character_class == 'THIEF':
            return Character.THIEF.value

        elif character_class == 'WIZARD':
            return Character.WIZARD.value

        elif character_class is None:
            return None

        else:
            raise Exception('Такого игрового персонажа нет')
