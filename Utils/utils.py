class Utils:
    players = list()

    nbrJoueur = 0

    play = True
    ending = False
    hasWin = None
    dieNumber = 1
    playerTurn = 1

    def getPlayerAt(self, case, number):

        for player in self.players:
            if player.case == case and player.playerNbr != number:
                return player
