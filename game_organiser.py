from shell_response import ShellResponse
from turn_organiser import TurnOrganiser

#class which controls how the player interacts with the game and when the game starts and stops
class GameOrganiser:

    #initialises the GameOrganiser, confirms how the player will interact with the game
    #and then starts the game
    def __init__(self):
        self.__selectedGameNumber = 0
        self.__selectedResponseMode = 0
        self.__selectedPlayerNum = 2
        self.__active = True
        self.response = ShellResponse()
        if self.response.responseModeCheck()==1:
            self.__selectedResponseMode = 1
        self.gameSelectionStart()

    #loops until checkIfClose returns true
    #sets up a game where game type and number of players are selected by the user
    def gameSelectionStart(self):

        while self.__active:
            self.__selectedGameNumber = self.response.selectGame()
            self.__selectedPlayerNum = self.response.selectNoOfPlayers()
            TurnOrganiser(self.__selectedGameNumber,self.__selectedResponseMode,self.__selectedPlayerNum)

            if self.response.checkIfClose():
                self.__active = False

#start the game organiser
GameOrganiser()
