from ScreenManager.screenManager import ScreenManager
import time
from BoardManager import Board
from Utils import Die
from Utils.utils import Utils


class Player:

    def __init__(self, case, color, playerNbr):
        self.case = case
        self.color = color
        self.lastCase = case
        self.playerNbr = playerNbr
        self.wait = False

    def move(self, move):

        if Board.Board.getCase(Board.Board(), self.case).type is None:
            self.lastCase = self.case
        if self.wait:
            self.wait = False
            return

        if self.case + move > 47:
            self.case -= (self.case + move) - 47
        else:
            self.case += move
            Screen = ScreenManager()
            ScreenManager.update(Screen)
            board = Board.Board()
            caseType = Board.Board.getCase(board, self.case).type
            if caseType == "times2":
                self.case = self.case * 2
            elif caseType == "to41":
                self.case = 41
            elif caseType == "playAgain":
                self.case += (Die.roll())
            elif caseType == "backTo20":
                self.case = 20
            elif caseType == "restart":
                self.case = 0
            elif caseType == "wait":
                self.wait = True

        player = Utils.getPlayerAt(Utils(), self.case, self.playerNbr)
        if player is not None:
            player.case = player.lastCase
            ScreenManager.drawPlayer(ScreenManager(), player, player.case)
            print("Sur la même case")

        ScreenManager.update(ScreenManager())

        if self.case == 47:
            Utils.hasWin = self
            Utils.ending = True
            Utils.play = False


