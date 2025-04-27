from game_board.row import Row

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
