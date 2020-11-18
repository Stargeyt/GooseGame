from random import *
from ScreenManager.screenManager import ScreenManager

def roll():

    number = randrange(1, 6)
    ScreenManager.setDie(ScreenManager(), number)
    return number



