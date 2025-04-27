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