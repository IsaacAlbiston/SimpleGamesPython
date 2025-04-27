#class which allows a user to interact with a game through the python shell
class ShellResponse():

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