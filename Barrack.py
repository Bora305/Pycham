class Barracks:
    def __init__(self, player):
        self.player = player

    def produce(self):
        self.player.mineral -= 50
        self.player.gas -= 25
        f = open("log.csv", 'a')
        f.write(f"{self.player},파이어벳,생성,1\n\r")
        f.close()
        return Firebat(self.plyer)