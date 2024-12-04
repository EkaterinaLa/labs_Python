from abc import ABC, abstractmethod
import random


class IAlive(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class Animal(IAlive, ABC):
    def __init__(self, name, age):
        if age < 0:
            age = 0
        self.__name = name
        self.__age = age

    @property
    @abstractmethod
    def shape(self):
        pass

    def make_sound(self):
        print(self.shape)

    @property
    def age(self):
        return self.__age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    @property
    def shape(self):
        return ""\
                "           ^\\\n"\
                " /        //o__o\n"\
                "/\\       /  __/\n"\
                "\\ \\______\\  /     -ARF!\n"\
                " \\         /\n"\
                "  \\ \\----\\ \\\n"\
                "   \\_\\_   \\_\\_"


class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    @property
    def shape(self):
        return '\n' \
               '    /\\___/\\\n' \
               '   /       \\\n' \
               '  l  u   u  l\n' \
               '--l----*----l--\n' \
               '   \\   w   /     - Meow!\n' \
               '     ======\n' \
               '   /       \\ __\n' \
               '   l        l\\ \\\n' \
               '   l        l/ /\n' \
               '   l  l l   l /\n' \
               '   \\ ml lm /_/'

    def make_sound(self):
        if random.choice([True, False]) is True:
            print(self.shape)
        else:
            print('Cat does not want to meow')


class Person:
    def __init__(self, name, animal):
        self.__name = name
        self.__animal = animal

    @property
    def name(self):
        return self.__name

    @property
    def animal(self):
        return self.__animal

    def get_companion_info(self):
        print('--------------------')
        print(f'Companion for {self.name} is named {self.animal.name}')
        print(f'It is {self.animal.age} years old')
        print(f'And it sounds like this:')
        print(self.animal.shape)
        print('--------------------')


if __name__ == '__main__':
    patric = Cat('Patric', 3)
    daniel = Dog('Daniel', 7)
    emily = Person('Emily', patric)
    kate = Person('Kate', daniel)
    print(patric.make_sound())
    print(emily.get_companion_info())
    print(daniel.make_sound())
    print(kate.get_companion_info())

