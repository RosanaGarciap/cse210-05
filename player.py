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
        self.__hider = Hider()
        self.__playing = True
    def startGame(self):
        while (self.__playing):
            val = int(input("Enter a location [1-1000]: "))
            self.compare(val)
    
    def compare(self,val):
        if(self.__hider.equalTo(val)):
            print("(;.;) You found me!")
            self.__playing = False
        else:
            if(self.__hider.closeTo(val)):
                print("(>.<) Getting warmer!\n")
            else:
                print("(^.^) Getting Colder!\n")
