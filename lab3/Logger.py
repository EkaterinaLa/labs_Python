class GameLog:
    __instance = None

    @staticmethod
    def get_instance():
        if GameLog.__instance is None:
            GameLog.__instance = GameLog()
        return GameLog.__instance

    @staticmethod
    def log(message):
        print(f'[GAME LOG] {message}')


'''s1 = GameLog.get_instance()
s2 = GameLog.get_instance()
print(s1 is s2)'''