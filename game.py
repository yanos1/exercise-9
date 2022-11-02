from board import Board
from car import Car
import sys
from helper import *

class Game:
    """
    Runs the game according to the rules
    """

    def __init__(self, board):
        """
        Initialize a new Game object.
        :param board: An object of type board
        """
        #You may assume board follows the API
        # implement your code here (and then delete the next line - 'pass')
        self.board=board


    def __single_turn(self):
        """
        Note - this function is here to guide you and it is *not mandatory*
        to implement it.

        The function runs one round of the game :
            1. Get user's input of: what color car to move, and what
                direction to move it.
            2. Check if the input is valid.
            3. Try moving car according to user's input.

        Before and after every stage of a turn, you may print additional
        information for the user, e.g., printing the board. In particular,
        you may support additional features, (e.g., hints) as long as they
        don't interfere with the API.
        """
        # implement your code here (and then delete the next line - 'pass')
        while True:
            input_ = input('choose what to play:')
            if input_ == "!":
                return False

            elif valid_input_(input_) and self.board.move_car(input_[0],input_[2]):
                print(self.board)
                return True

            else:
                print("Bad Input!")

    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """
        print(self.board)
        while not self.board.cell_content(self.board.target_location()):
            if not self.__single_turn():
                break

def valid_car(name,lenght,orientation):
    if lenght > 4 or lenght < 2:
        if type(lenght) != int:
            return False

    elif orientation != 0 and orientation != 1:
        return False

    elif name not in ('R', 'G', 'W', 'O', 'B', 'Y'):
        return False

    return True

def valid_input_(input_):
    if len(input_) != 3:
        return False
    elif input_[0] not in ('R', 'G', 'W', 'O', 'B', 'Y'):
        return False
    elif input_[1] != ',':
        return False
    elif input_[2] not in ('r', 'l', 'u', 'd'):
        return False
    return True

if __name__== "__main__":
    #Your code here
    #All access to files, non API constructors, and such must be in this
    #section, or in functions called from this section.
    # Opening JSON file

    board = Board()
    json_p = sys.argv[1]
    json = load_json(json_p)

    for carname in json:
        length, location, orientation = json[carname]
        if valid_car(carname,length,orientation):
            board.add_car(Car(carname,length,tuple(location),orientation))

    game=Game(board)
    game.play()


#json_p=sys.argv[1]
#json_p='car_config.json