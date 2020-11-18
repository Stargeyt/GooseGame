from BoardManager.Board import Board
from player import Player
from ScreenManager.screenManager import ScreenManager
from Utils import Die
import pygame
from Utils import utils


class GooseGame:

    def __init__(self):

        self.initPlayers()
        self.board = Board()

    def initPlayers(self):

        canPlay = False
        nbrJoueur = 0
        WIDTH = 1350
        HEIGHT = 904
        pygame.init()
        pygame.display.set_caption("Jeu de l'oie")

        bg = pygame.image.load("Resources/select-players.jpg")

        screen = pygame.display.set_mode((WIDTH, HEIGHT))

        while not canPlay:

            screen.blit(bg, (0, 0))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    x, y = pygame.mouse.get_pos()
                    if 314 < x < 607 and 287 < y < 440:
                        utils.Utils.nbrJoueur = 2
                        nbrJoueur = 2
                        canPlay = True
                    elif 743 < x < 1035 and 287 < y < 440:
                        utils.Utils.nbrJoueur = 3
                        nbrJoueur = 3
                        canPlay = True
                    elif 529 < x < 820 and 513 < y < 666:
                        utils.Utils.nbrJoueur = 4
                        nbrJoueur = 4
                        canPlay = True

        colors = ["blue", "red", "green", "pink"]
        for i in range(nbrJoueur):
            utils.Utils.players.append(Player(0, colors[i], i))

    def gameLoop(self):
        Screen = ScreenManager()
        ScreenManager.update(Screen)
        while utils.Utils.play:

            for player in utils.Utils.players:
                hasPlay = False
                if utils.Utils.ending:
                    continue
                utils.Utils.playerTurn += 1
                if utils.Utils.playerTurn > utils.Utils.nbrJoueur:
                    utils.Utils.playerTurn = 1
                if player.wait:
                    player.wait = False
                    hasPlay = True
                while not hasPlay:
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONUP:
                            x, y = pygame.mouse.get_pos()
                            if 1235 < x < 1343 and 451 < y < 559:
                                move = Die.roll()
                                player.move(move)
                                hasPlay = True



        while utils.Utils.ending:
            ScreenManager.updateEnd(Screen)


if __name__ == '__main__':
    game = GooseGame()
    game.gameLoop()
