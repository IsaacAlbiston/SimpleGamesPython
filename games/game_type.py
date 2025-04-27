#abc is imported to enable abstract methods and classes
from abc import ABC

#abstract class that acts as the superclass for all game types
class GameType(ABC):

    #returns text to acknowledge the computer winning 
    def computerWin(self):
        return "The computer wins!"

    #returns text to acknowledge the player winning
    def playerWin(self,name):
        return name+" wins!"

    #returns text to acknowledge a draw
    def noWin(self):
        return "The game was a draw!"