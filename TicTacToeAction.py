class TicTacToeAction:
    def __init__(self,player,position):
        self.player=player
        self.position=position

    def getPosition(self):
        return self.position

    def getPlayer(self):
        return self.player