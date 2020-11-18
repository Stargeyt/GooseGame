from BoardManager.Board import Board
import pygame

import BoardManager
from BoardManager.CaseEnum import cases
from Utils import utils


class ScreenManager:

    def __init__(self):
        self.WIDTH = 1350
        self.HEIGHT = 904
        pygame.init()
        pygame.display.set_caption("Jeu de l'oie")

        bg = pygame.image.load("Resources/plate.jpg")

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.screen.blit(bg, (0, 0))

    def keyCheck(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or event.type == pygame.QUIT:
                    utils.Utils.play = False
                    return

    def update(self):

        if utils.Utils.play:

            police = pygame.font.Font("Resources/atwriter.ttf", 40)
            color = (0, 0, 0)
            playerColor = utils.Utils.players[utils.Utils.playerTurn-1].color
            if playerColor == "blue":
                color = (0, 0, 255)
            elif playerColor == "red":
                color = (255, 0, 0)
            elif playerColor == "green":
                color = (0, 255, 0)
            elif playerColor == "pink":
                color = (77, 11, 55)
            texte = police.render("Au tour du joueur " + str(utils.Utils.playerTurn), True, color)
            rectTexte = texte.get_rect()
            rectTexte.topright = self.screen.get_rect().topright

            self.screen.blit(texte, rectTexte)

        for player in utils.Utils.players:
            self.drawPlayer(player, player.case)

        self.drawDie()
        pygame.display.flip()

    def updateEnd(self):
        for player in utils.Utils.players:
            self.drawPlayer(player, player.case)

        police = pygame.font.Font("Resources/atwriter.ttf", 72)
        color = (0, 0, 0)
        if utils.Utils.hasWin.color == "blue":
            color = (0, 0, 255)
        elif utils.Utils.hasWin.color == "red":
            color = (255, 0, 0)
        elif utils.Utils.hasWin.color == "green":
            color = (0, 255, 0)
        elif utils.Utils.hasWin.color == "pink":
            color = (77, 11, 55)
        texte = police.render("Le joueur " + str(utils.Utils.hasWin.playerNbr+1) + " a gagne", True, color)
        rectTexte = texte.get_rect()
        rectTexte.center = self.screen.get_rect().center

        self.screen.blit(texte, rectTexte)

        pygame.display.flip()

    def drawPlayer(self, player, playerCase):

        if playerCase == 0:
            center = self.getStartLoc(player.playerNbr + 1)
        else:
            center = self.getLoc(playerCase)

        color = (255, 255, 255)

        if player.color == "blue":
            color = (0, 0, 255)
        elif player.color == "red":
            color = (255, 0, 0)
        elif player.color == "green":
            color = (0, 255, 0)
        elif player.color == "pink":
            color = (77, 11, 55)

        image = pygame.image.load("Resources/goose-head.png").convert_alpha()


        pygame.draw.circle(self.screen, color, center, 28)

        x,y= center
        self.screen.blit(image, (x-14,y-14))



    def getLoc(self, casenumber):

        return cases.dictionnaire["case" + str(casenumber)]

    def getStartLoc(self, playerNumber):

        return cases.dictionnaire["depart" + str(playerNumber)]

    def drawDie(self):

        image = pygame.image.load("Resources/die/" + str(utils.Utils.dieNumber) + ".png").convert_alpha()

        self.screen.blit(image, (1235, 450))

        pygame.display.flip()

    def setDie(self, number):
        utils.Utils.dieNumber = number

    def printTest(self):
        for i in range(63):
            toAdd = ""
            for player in utils.Utils.players:
                if player.case == i:
                    toAdd = "x"

            board = BoardManager.Board.Board()
            if Board.getCase(board, i).type == "End":
                toAdd = "Fin"

            print("[", toAdd, "]", end='', sep='')
