#class that manages the "computers" knowledge of connect four
class ConnectFourComputerPlayer():

    #initialises the computers knowledge of the game board
    def __init__(self, size):
        #list of lists to track the board state
        self.__boardScore = [[0]*size for i in range(size)]
        self.__boardState = [[0]*size for i in range(size)]
        #self.__boardScore = [[0]*size]*size
        #self.__boardState = [[" "]*size]*size

    #updates boardScore and boardState to reflect the state of the board after newMove is played
    #isPlayer represents who is playing the move True = player and False = computer
    def updateKnowledge(self, newMove, isPlayer):
        self.__boardScore[newMove[0]][newMove[1]] = -1
        if isPlayer:
            self.__boardState[newMove[0]][newMove[1]] = "Player"
            #loops through the 9 spaces surronding the space where the new move was taken
            for i in range (-1, 2):
                for j in range (-1, 2):
                    additionalScore = 1
                    keepSearching = True
                    x=newMove[0]+i*additionalScore
                    y=newMove[1]+j*additionalScore
                    if x>=0 and x<len(self.__boardState) and y<len(self.__boardState) and y>=0:
                        if self.__boardScore[x][y]>=0:
                            while keepSearching:
                                if x>=0 and x<len(self.__boardState) and y<len(self.__boardState) and y>=0:
                                    if self.__boardState[x][y] == "Player":
                                        additionalScore += 1
                                        x -= i
                                        y -= j
                                    else:
                                        keepSearching = False
                                else: 
                                    keepSearching = False
                            self.__boardScore[newMove[0]+i][newMove[1]+j] += additionalScore
        else:
            self.__boardState[newMove[0]][newMove[1]] = "Computer"
            for i in range (-1, 2):
                for j in range (-1, 2):
                    additionalScore = 1
                    keepSearching = True
                    x=newMove[0]+i*additionalScore
                    y=newMove[1]+j*additionalScore
                    if x>=0 and x<len(self.__boardState) and y<len(self.__boardState) and y>=0:
                        if self.__boardScore[x][y]>=0:
                            while keepSearching:
                                if x>=0 and x<len(self.__boardState) and y<len(self.__boardState) and y>=0:
                                    if self.__boardState[x][y] == "Computer":
                                        additionalScore += 1
                                        x -= i
                                        y -= j
                                    else:
                                        keepSearching = False
                                else: 
                                    keepSearching = False
                            self.__boardScore[newMove[0]+i][newMove[1]+j] += additionalScore
        print(self.__boardScore)
        print(self.__boardState)
    
    def findFirstPositive(self, lst):
        index = 0
        for number in lst:
            if number >= 0:
                return [number,index]
            index += 1
        return [-1,0]

    def selectBestMove(self):
        bestMoveLocation = [0,0]
        bestMoveScore = -1
        for x in range (0, len(self.__boardScore)):
            columnScore = self.findFirstPositive(self.__boardScore[x])
            print(columnScore)
            if columnScore[0]>bestMoveScore:
                bestMoveScore = columnScore[0]
                bestMoveLocation[0] = x
                bestMoveLocation[1] = columnScore[1]
        print("best move located")
        print(bestMoveLocation)
        return bestMoveLocation
    