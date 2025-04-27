from games.game_type import GameType
from games.noughts_and_crosses.nc_computer_player import NoughtsAndCrossesComputerPlayer
from game_board.board import Board

#class that enforces the rules of the game noughts and crosses
class NoughtsAndCrosses(GameType):

    #initialises the noughts and crosses board as a 3x3 empty board
    def __init__(self):
        self.__size = 5
        self.__gameBoard = Board(self.__size,self.__size)
        self.__lastPlayerMove = [0,0]
        self.__computerKnowledge = NoughtsAndCrossesComputerPlayer(self.__size)
        self.__noughtMark = "O"
        self.__crossMark = "X"
        self.__noughtsWin = False
        self.__crossesWin = False

    #returns a string of text containing instructions for playing
    def introMessage(self):
        return "You are playing noughts and crosses, player 1 is Os and player 2 is Xs. Player 1 has the first turn."

    #returns a string that acts as a text representation of the current game board
    def displayCurrentBoard(self):
        __textBoard = ""
        __currentBoard = self.__gameBoard.getBoard()
        for i in range (0, len(__currentBoard)):
            __textBoard = __textBoard + "|".join(__currentBoard[i]) + "/n"
        return __textBoard

    #decides where to place an X based on the current game board
    def computerAction(self):

        __currentBoard = self.__gameBoard.getBoard()
        __moveChoice = []
        #updates the information about the player with the players last move
        self.__computerKnowledge.updateKnowledge(self.__lastPlayerMove, True)


        #sets the first good move possible as the move choice
        if len(__moveChoice) == 0:
            __moveChoice = self.__computerKnowledge.goodMove()
            print("Good move choice:")
            print(__moveChoice)

        #if there was no good moves sets a random legal move as the move choice
        if len(__moveChoice) == 0:
            __moveChoice = self.__computerKnowledge.randomMove()
            print("Random move choice:")
            print(__moveChoice)

        print("Selected move choice:")
        print(__moveChoice)
        #updates the game board with the selected move
        __currentBoard[__moveChoice[1]][__moveChoice[0]]=self.__crossMark
        self.__gameBoard.setBoard(__currentBoard)

        #updates the information about the computer with the computers current move
        self.__computerKnowledge.updateKnowledge(__moveChoice, False)



    #marks space at coordinates (x,y) with input if the space is empty
    #x and y must be between 0 and 2
    #returns a boolean to confirm if the space was marked
    def playerAction(self,x,y,player):
        if x<0 or x>=self.__size or y<0 or y>=self.__size:
            return False
        __currentBoard = self.__gameBoard.getBoard()
        if __currentBoard[y][x]== " ":
            if player == 1:
                __currentBoard[y][x]=self.__noughtMark
                self.__lastPlayerMove = [x,y]
            if player == 2:
                __currentBoard[y][x]=self.__crossMark
            self.__gameBoard.setBoard(__currentBoard)
            return True
        return False

    #checks if the game should end
    def gameEndCheck(self):
        #checks for any lines of Xs
        if self.__gameBoard.anyRowSame()==self.__crossMark or self.__gameBoard.anyColumnSame()==self.__crossMark or self.__gameBoard.anyDiagonalSame()==self.__crossMark:
            self.__crossesWin = True
            return True
        #checks for any lines of Os
        if self.__gameBoard.anyRowSame()==self.__noughtMark or self.__gameBoard.anyColumnSame()==self.__noughtMark or self.__gameBoard.anyDiagonalSame()==self.__noughtMark:
            self.__noughtsWin = True
            return True
        #checks for the gameboard being full
        if self.__gameBoard.boardFullCheck():
            return True
        return False

    #returns the boolean value of the crossesWin variable
    def player1WinCheck(self):
        return self.__noughtsWin

    #returns the boolean value of the noughtsWin variable
    def player2WinCheck(self):
        return self.__crossesWin