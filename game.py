from hider import Hider
from player import Player
class Game:
    '''An abstract template representation of a Games of Seeker.
    Each Game needs a Player and a Hider.
    '''


    def __init__(self):
        """
        Constructor of class Game
        Attributes:
            - hider: it represent the hidden item of the game which tha player doesn't know
            - player: represents the 
        """
        self.__hider = Hider()
        self.__player = Player()

    def startGame(self):
        """
        This functions starts tha game and keep the game active until the player guess right the 
        value of the Hider.
        """
        while (self.__player.playing):
            val = self.__player.guessHider()
            self.compare(val)

    def compare(self,val):
        if(self.__hider.equalTo(val)):
            print("(;.;) You found me!")
            self.__player.playing = False
        else:
            if(self.__hider.closeTo(val)):
                print("(>.<) Getting warmer!\n")
            else:
                print("(^.^) Getting Colder!\n")