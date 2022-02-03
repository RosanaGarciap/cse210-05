from hider import Hider

class Player:
    """A player who directs the game.

    The responsibility of the Player is to control the game.

    Attributes:
        Please update comments  
    """

    def __init__(self):
        """Please update comments
        
        Args:
            Please update comments
        """
        self.playing = True

    def guessHider(self):
        """
        The player is asked to provide an answer
        """
        return int(input("Enter a location [1-1000]: "))