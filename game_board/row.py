from game_board.space import Space
#class that represents each horizontal row on a game board
class Row:

    #initialises the row as a list of spaces of the specified size
    def __init__(self, width):
        self.__spaceList = []
        for i in range (0,width):
            self.__spaceList.append(Space())
    
    def rowAdjacentIdentical(self, adjacentSizeToFind):
        previousChar = " "
        charCount = 1
        for i in range (0,len(self.__spaceList)):
            if previousChar == self.__spaceList[i].getSpaceContents():
                charCount += 1
            else:
                charCount = 1
            previousChar = self.__spaceList[i].getSpaceContents()
            if (previousChar != " " and charCount== adjacentSizeToFind):
                return previousChar
        return " "

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
