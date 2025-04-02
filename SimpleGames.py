#abc is imported to enable abstract methods and classes
from abc import ABC
from random import randrange
import discord

#class which controls how the player interacts with the game and when the game starts and stops
class GameOrganiser:

    #initialises the GameOrganiser, confirms how the player will interact with the game
    #and then starts the game
    def __init__(self):
        self.__selectedGameNumber = 0
        self.__selectedResponseMode = 0
        self.__selectedPlayerNum = 2
        self.__active = True
        self.response = LocalResponse()
        if self.response.responseModeCheck()==1:
            self.__selectedResponseMode = 1
            self.response = DiscordResponse()
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

#class responsible for managing the turns in the game
class TurnOrganiser:

    #Initialises the TurnOrganiser and starts a game with
    #the selected game number, player number
    #and mode of communication with the game
    def __init__(self, gameNumber, responseMode, numOfPlayers):
        self.__player1Turn = True
        self.__gameRunning = True
        self.__computerPlaying = True
        #print("game number:"+str(gameNumber))
        #print("response mode:"+str(responseMode))
        #print("num of players:"+str(numOfPlayers))
        #sets selected game mode
        if gameNumber == 0:
            self.game = TicTacToe()
        #sets selected response type
        if responseMode == 0:
            self.response = LocalResponse()
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


#class which allows a user to interact with a game through the python shell
class LocalResponse():

    #initialises the class with a counter to keep track of the number of interactions the class has
    def __init__(self):
        self.__actionCounter = 0

    #prints a message asking what game the user wants
    #returns the response if it is a number, otherwise returns 0
    def selectGame(self):
        __gameResponse = input("What game do you want to play, please enter 0 for Noughts and Crosses")
        if __gameResponse.isdigit():
            return int(__gameResponse)
        return 0

    #prints a message asking how many players want to play
    #returns the response if it is a number, otherwise returns 2
    def selectNoOfPlayers(self):
        __numResponse = input("How many players want to play, please enter 1 or 2")
        if __numResponse.isdigit():
            return int(__numResponse)
        return 2

    #prints a message asking what response mode the user wants
    #returns the response if it is a number, otherwise returns 0
    def responseModeCheck(self):
        __startResponse = input("What response mode do you want to use, please enter 0 for python shell or 1 for discord bot")
        if __startResponse.isdigit():
            return int(__startResponse)
        return 0

    #prints a message asking if the player wants to stop playing
    #returns True if the response is "y", otherwise returns False
    def checkIfClose(self):
        __closeResponse = input("Do you want to stop playing simple games, please enter y or n")
        if __closeResponse=="y":
            return True
        return False

    #prints a given message to the python shell
    #divides messages containing /n onto different lines
    def message(self,text):
        for i in (text.split("/n")):
            print(i)

    #Prints a message asking player 1 for an x coordinate
    #returns the x coordinate given or a large negative number if the response wasn't a number
    def player1ActionX(self):
        self.__actionCounter += 1
        __playerResponse = input("Player 1, please enter the x coordinate for your next move")
        if __playerResponse.isdigit():
            return int(__playerResponse)
        return -10000000

    #Prints a message asking player 1 for a y coordinate
    #returns the y coordinate given or a large negative number if the response wasn't a number
    def player1ActionY(self):
        self.__actionCounter += 1
        __playerResponse = input("Player 1, please enter the y coordinate for your next move")
        if __playerResponse.isdigit():
            return int(__playerResponse)
        return -10000000

    #Prints a message asking player 2 for an x coordinate
    #returns the x coordinate given or a large negative number if the response wasn't a number
    def player2ActionX(self):
        self.__actionCounter += 1
        __playerResponse = input("Player 2, please enter the x coordinate for your next move")
        if __playerResponse.isdigit():
            return int(__playerResponse)
        return -10000000

    #Prints a message asking player 2 for a y coordinate
    #returns the y coordinate given or a large negative number if the response wasn't a number
    def player2ActionY(self):
        self.__actionCounter += 1
        __playerResponse = input("Player 2, please enter the y coordinate for your next move")
        if __playerResponse.isdigit():
            return int(__playerResponse)
        return -10000000


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

#class that manages the "computers" knowledge of the game
class ComputerKnowledge():

    #initialises the computers knowledge of the game board
    def __init__(self, size):
        #varibles to track how close the computer is to winning
        self.__computerColumnScores = [0]*size
        self.__computerRowScores = [0]*size
        self.__computerDiagonalScores = [0,0]

        #varibles to track how close the player is to winning
        self.__playerColumnScores = [0]*size
        self.__playerRowScores = [0]*size
        self.__playerDiagonalScores = [0,0]

        self._possibleMoves = []

        #adds all spaces on the gameboard to possible moves
        for i in range(0,size):
            for j in range(0,size):
                self._possibleMoves.append([i,j])

    #updates possible moves list and scores to reflect the state of the board after newMove is played
    #isPlayer represents who is playing the move True = player and False = computer
    def updateKnowledge(self, newMove, isPlayer):
        if self._possibleMoves.count(newMove)>=1:
            self._possibleMoves.remove(newMove)

        if isPlayer:
            self.__playerColumnScores[newMove[0]] += 1
            self.__playerRowScores[newMove[1]] += 1

            if newMove[0]==newMove[1]:
                self.__playerDiagonalScores[0] += 1

            if newMove[0] == len(self.__computerColumnScores) - 1 - newMove[1]:
                self.__playerDiagonalScores[1] += 1
            print([self.__playerColumnScores,self.__playerRowScores,self.__playerDiagonalScores])
        else:
            self.__computerColumnScores[newMove[0]] += 1
            self.__computerRowScores[newMove[1]] += 1

            if newMove[0]==newMove[1]:
                self.__computerDiagonalScores[0] += 1

            if newMove[0] == len(self.__computerColumnScores) - 1 - newMove[1]:
                self.__computerDiagonalScores[1] += 1
            print([self.__computerColumnScores,self.__computerRowScores,self.__computerDiagonalScores])


    #if coordPos is 0 finds a coordinate in possible moves where x = location
    #if coordPos is 1 finds a coordinate in possible moves where y = location
    #returns the coordinate found, otherwise returns an empty list
    def findPossible(self, location, coordPos):
        __moves = []
        for move in self._possibleMoves:
            if move[coordPos] == location:
                return move
        return __moves


    #returns the index of the highest integer in line where the integer at the same index in other line is 0
    def bestNoContestLine(self, line, otherLine):
        __index = -1
        __highest = 0
        for i in range (0, len(line)):
            #if this index is zero in other line and value at this index is higher than previous best
            if (otherLine[i] == 0) and (line[i] >= __highest):
                __highest = line[i]
                __index = i
        return __index

    #recieves an index for each of the 4 line scores lists
    #finds the index that represents the highest score
    #returns a number representing the index found
    def bestGoodMove(self, computerColumn, computerRow, playerColumn, playerRow):
        if self.__computerColumnScores[computerColumn] >= self.__computerRowScores[computerRow] and self.__computerColumnScores[computerColumn] >= self.__playerColumnScores[playerColumn] and self.__computerColumnScores[computerColumn] >= self.__playerRowScores[playerRow] and computerColumn > -1:
            return 0
        if self.__computerRowScores[computerRow] >= self.__playerColumnScores[playerColumn] and self.__computerRowScores[computerRow] >= self.__playerRowScores[playerRow] and computerRow > -1:
            return 1
        if self.__playerColumnScores[playerColumn] >= self.__playerRowScores[playerRow] and playerColumn > -1:
            return 2
        return 3

    #finds which row or column has the most Xs without any Os or most Os without any Xs
    #returns a coordinate in that row
    def goodMove(self):
        __goodMove = []
        __computerColumnIndex = self.bestNoContestLine(self.__computerColumnScores, self.__playerColumnScores)
        __computerRowIndex = self.bestNoContestLine(self.__computerRowScores, self.__playerRowScores)
        __playerColumnIndex = self.bestNoContestLine(self.__playerColumnScores, self.__computerColumnScores)
        __playerRowIndex = self.bestNoContestLine(self.__playerRowScores, self.__computerRowScores)

        __movePick = self.bestGoodMove(__computerColumnIndex, __computerRowIndex, __playerColumnIndex, __playerRowIndex)

        if __movePick == 0:
            __goodMove = self.findPossible(__computerColumnIndex, 0)
        elif __movePick == 1:
            __goodMove = self.findPossible(__computerRowIndex, 1)
        elif __movePick == 2:
            __goodMove = self.findPossible(__playerColumnIndex, 0)
        else:
            __goodMove = self.findPossible(__playerRowIndex, 1)


        return __goodMove

    #returns a random coordinate form the list of possible moves
    def randomMove(self):
        if len(self._possibleMoves) > 1:
            return self._possibleMoves[randrange(len(self._possibleMoves)-1)]
        return self._possibleMoves[0]


#class that enforces the rules of the game noughts and crosses
class TicTacToe(GameType):

    #initialises the noughts and crosses board as a 3x3 empty board
    def __init__(self):
        self.__size = 5
        self.__gameBoard = Board(self.__size,self.__size)
        self.__lastPlayerMove = [0,0]
        self.__computerKnowledge = ComputerKnowledge(self.__size)
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

#class that represents the game board
class Board:

    #initialises the board as a list of rows of the specified size
    def __init__(self, width, height):
        self.__rowList = []
        for i in range (0,height):
            self.__rowList.append(Row(width))

    #checks if any row on the board has identical characters in all spaces
    #returns the characters in the spaces of the row if found, otherwise returns " "
    def anyRowSame(self):
        for row in self.__rowList:
            if not row.rowSame()==" ":
                return row.rowSame()
        return " "

    #checks if any column on the board has identical characters in all spaces
    #returns the characters in the spaces of the column if found, otherwise returns " "
    def anyColumnSame(self):
        #iterates through the columns on the board
        for i in range (0,len(self.__rowList)):
            __currentRow = self.__rowList[0].getRow()
            __columnContents = __currentRow[i]
            #iterates through the spaces of each column
            for j in range (1,len(__currentRow)):
                __currentRow = self.__rowList[j].getRow()
                if __columnContents != __currentRow[i]:
                    __columnContents=" "

            #check if column contained identical non blank characters
            if __columnContents != " ":
                return __columnContents
        return __columnContents

    #checks if any diagonal on the board has identical characters in all spaces
    #returns the characters in the spaces of the diagonal if found, otherwise returns " "
    def anyDiagonalSame(self):
        #checks the top left to bottom right diagonal
        __currentRow = self.__rowList[0].getRow()
        __diagonalContents = __currentRow[0]
        for i in range (1,len(self.__rowList)):
            __currentRow = self.__rowList[i].getRow()
            if __diagonalContents != __currentRow[i]:
                __diagonalContents=" "
        #check if diagonal contained identical non blank characters
        if __diagonalContents != " ":
            return __diagonalContents

        #checks the bottom left to top right diagonal
        __currentRow = self.__rowList[0].getRow()
        __diagonalContents = __currentRow[len(self.__rowList)-1]
        for i in range (1,len(self.__rowList)):
            __currentRow = self.__rowList[i].getRow()
            if __diagonalContents != __currentRow[len(self.__rowList)-(i+1)]:
                __diagonalContents=" "
        return __diagonalContents

    #returns true if the board has no empty spaces, otherwise returns false
    def boardFullCheck(self):
        for i in range (0,len(self.__rowList)):
            if not self.__rowList[i].rowFullCheck():
                return False
        return True

    #returns the current contents of the game board
    def getBoard(self):
        __tempList = []
        for i in range (0,len(self.__rowList)):
            __tempList.append(self.__rowList[i].getRow())
        return __tempList

    #sets the current contents of the game board
    #will not change the board if the new board is a different height than the current one
    def setBoard(self, newBoard):
        #checks if the new board is the same height as the old board
        if len(newBoard) == len(self.__rowList):
            for i in range (0,len(self.__rowList)):
                self.__rowList[i].setRow(newBoard[i])



#class that represents each horizontal row on a game board
class Row:

    #initialises the row as a list of spaces of the specified size
    def __init__(self, width):
        self.__spaceList = []
        for i in range (0,width):
            self.__spaceList.append(Space())

    #checks if the row has identical characters in all spaces
    #if True returns the identical characters, otherwise returns " "
    def rowSame(self):
        __tempChar = self.__spaceList[0].getSpaceContents()
        for i in range (1,len(self.__spaceList)):
            if __tempChar != self.__spaceList[i].getSpaceContents():
                __tempChar = " "
        return __tempChar

    #returns true if the row has no empty spaces, otherwise returns false
    def rowFullCheck(self):
        for i in range (0,len(self.__spaceList)):
            if self.__spaceList[i].spaceIsEmpty():
                return False
        return True

    #returns the current contents of a row
    def getRow(self):
        __tempList = []
        for i in range (0,len(self.__spaceList)):
            __tempList.append(self.__spaceList[i].getSpaceContents())
        return __tempList

    #sets the current contents of a row
    #will not change the row if the new row is a different width than the current one
    def setRow(self, newRow):
        #checks if the new row is the same width as the old row
        if len(newRow) == len(self.__spaceList):
            for i in range (0,len(self.__spaceList)):
                self.__spaceList[i].setSpaceContents(newRow[i])



#class that represents each space on a game board
class Space:

    #initialises the space
    def __init__(self):
        self.__contains = " "

    #returns true if space is empty otherwise returns false
    def spaceIsEmpty(self):
        if self.__contains == " ":
            return True
        return False

    #returns the current contents of a space
    def getSpaceContents(self):
        return self.__contains

    #sets the current contents of a space
    def setSpaceContents(self, newContents):
        self.__contains = newContents

#start the game organiser
GameOrganiser()
