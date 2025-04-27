from random import randrange

#class that manages the "computers" knowledge of noughts and crosses
class NoughtsAndCrossesComputerPlayer():

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