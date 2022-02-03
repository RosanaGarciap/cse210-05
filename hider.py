import random
import math


class Hider:
    """A deck of cards. Cards included are 1-13.

    The value of the card is used for the main function of the game.
   
    Attributes:
        value (int): The number of the card drawn.
    """

    def __init__(self):
        """Constructs instances of Hider.

        Args:
            self (location): private instance that represent the Hider's position. 
        """
        self.__location = random.randint(1, 1000)
        self.__distance = 10000

    def closeTo(self, number):
        """Please update comments
        
        Args:
            self (card): an instance of a card.
        """
        if( abs(number - self.__location) < self.__distance):
            self.__distance = abs(number - self.__location)
            return True
        else:
            print(self.__location)
            return False
    def equalTo(self, number):
        """Please update comments
        
        Args:
            self (card): an instance of a card.
        """
        if(number == self.__location):
            return True
        else:
            return False
