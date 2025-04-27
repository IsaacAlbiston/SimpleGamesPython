from games.noughts_and_crosses.noughts_and_crosses import NoughtsAndCrosses
from shell_response import ShellResponse

#class responsible for managing the turns in the game
class TurnOrganiser:

    #Initialises the TurnOrganiser and starts a game with
    #the selected game number, player number
    #and mode of communication with the game
    def __init__(self, gameNumber, responseMode, numOfPlayers):
        self.__player1Turn = True
        self.__gameRunning = True
        self.__computerPlaying = True
        #sets selected game mode
        if gameNumber == 0:
            self.game = NoughtsAndCrosses()
        #sets selected response type
        if responseMode == 0:
            self.response = ShellResponse()
        #sets selected number of players
        if numOfPlayers == 2:
            self.__computerPlaying = False
        self.gameStart()


    #manages turns in the game and sends updates about
    #the games current state to the players
    def gameStart(self):
        #Sends intro message and starting board to the player(s)
        self.response.message(self.game.introMessage())
        self.response.message(self.game.displayCurrentBoard())
        #loops until the game ends
        while self.__gameRunning:
            #Accepts responses from player 1 on their turn
            if self.__player1Turn:
                self.response.message("Player 1's turn.")
                if self.game.playerAction(self.response.player1ActionX(),self.response.player1ActionY(),1):
                    self.__player1Turn = False
                    self.response.message(self.game.displayCurrentBoard())
                else:
                    self.response.message("Please enter a valid move.")
            #Accepts responses from player 2 on their turn
            #If player 2 is this python code
            elif self.__computerPlaying:
                self.response.message("Computer's turn.")
                self.game.computerAction()
                self.__player1Turn = True
                self.response.message(self.game.displayCurrentBoard())

            #If player 2 is not this python code
            else:
                self.response.message("Player 2's turn.")
                if self.game.playerAction(self.response.player2ActionX(),self.response.player2ActionY(),2):
                    self.__player1Turn = True
                    self.response.message(self.game.displayCurrentBoard())
                else:
                    self.response.message("Please enter a valid move.")

            #ends the game if gameEndCheck returns true
            if self.game.gameEndCheck():
                self.response.message(self.gameResult())
                self.__gameRunning = False

    #returns a string describing the result of the game
    def gameResult(self):
        if self.game.player1WinCheck():
            return self.game.playerWin("Player 1")
        if self.game.player2WinCheck():
            if self.__computerPlaying:
                return self.game.computerWin()
            return self.game.playerWin("Player 2")
        return self.game.noWin()
