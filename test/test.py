import unittest
from lab3 import Logger


class GameLoggerTest(unittest.TestCase):
    def setUp(self):
        self.logger = Logger.GameLog()

    def test_get_instance(self):
        first_instance = self.logger.get_instance()
        second_instance = self.logger.get_instance()
        self.assertIs(first_instance, second_instance)


if __name__ == "__main__":
    unittest.main()
