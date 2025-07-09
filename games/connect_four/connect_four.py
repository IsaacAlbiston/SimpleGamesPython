from games.game_type import GameType
from game_board.board import Board

class ConnectFour(GameType):

    def __init__(self):
        self.__size = 6
        self.__gameBoard = Board(self.__size,self.__size)
        self.__lastPlayerMove = [0,0]
        self.__redToken = "R"
        self.__yellowToken = "Y"
        self.__redWin = False
        self.__yellowWin = False

    def introMessage(self):
        return "You are playing connect four, Player 1 is Red and Player 2 is Yellow. Player 1 has the first turn."

    def displayCurrentBoard(self):
        __textBoard = ""
        __currentBoard = self.__gameBoard.getBoard()
        for i in range (0, len(__currentBoard)):
            __textBoard = __textBoard + "|".join(__currentBoard[i]) + "/n"
        return __textBoard

    def playerAction(self,x,y,player):
        if x<0 or x>=self.__size:
            return False
        __currentBoard = self.__gameBoard.getBoard()
        yCoord = self.__gameBoard.lowestSpaceInColumn(x)
        if yCoord != -1:
            if player == 1:
                __currentBoard[yCoord][x]=self.__redToken
                self.__lastPlayerMove = [x,yCoord]
            if player == 2:
                __currentBoard[yCoord][x]=self.__yellowToken
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
        return self.__redWin

    #returns the boolean value of the noughtsWin variable
    def player2WinCheck(self):
        return self.__yellowWin