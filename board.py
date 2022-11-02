from car import Car
class Board:
    """
    Add a class description here.
    Write briefly about the purpose of the class
    """

    def __init__(self):
        self.row = 7
        self.col = 7
        self.board = [["_" for i in range(self.row)] for j in range(self.col)]
        self.target = (3,7)
        self.poss_moves = []
        self.list_of_car_names = []
        self.cell_list = board.cell_list()
        #self.board[0][0],self.board[1][0],self.board[2][3], self.board[2][4] =1,1,1,1

    def __str__(self):
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board
        """
        return self.board

    def cell_list(self):
        """ This function returns the coordinates of cells in this board
        :return: list of coordinates
        """
        return [(i,j) for i in range(self.row) for j in range(self.col)] #+[(3,7)]

    def possible_moves(self):
        """ This function returns the legal moves of all cars in this board
        :return: list of tuples of the form (name,movekey,description)
                 representing legal moves
        """
        #From the provided example car_config.json file, the return value could be
        #[('O','d',"some description"),('R','r',"some description"),('O','u',"some description")]
        memo = []
        for row in self.board:
            for item in row:
                if item != "_":
                    if item not in memo:
                        memo.append(item)
                        pos_moves = car.possible_moves() #{u: "bla", d: :"bla"}
                    else:
                        continue
                    for key in pos_moves:
                        move_requirment = car.movement_requirements(key) #[(1,4)]
                        if move_requirment[0] in self.cell_list:
                            self.poss_moves.append((item,key,pos_moves.get(key)))
        return self.poss_moves



    def target_location(self):
        """
        This function returns the coordinates of the location which is to be filled for victory.
        :return: (row,col) of goal location
        """
        return self.target

    def cell_content(self, coordinate):
        """
        Checks if the given coordinates are empty.
        :param coordinate: tuple of (row,col) of the coordinate to check
        :return: The name if the car in coordinate, None if empty
        """
        pos = self.board[coordinate[0]][coordinate[1]]
        if pos != "_":
            car_name = car.get_name()
            return car_name
        return None

    def add_car(self, car):
        """
        Adds a car to the game.
        :param car: car object of car to add
        :return: True upon success. False if failed
        """
        #Remember to consider all the reasons adding a car can fail.
        #You may assume the car is a legal car object following the API.
        # implement your code and erase the "pass"
        if car.name in "RGWOBY" and car.location in self.cell_list and car.name not in board.list_of_car_names:
            board.list_of_car_names.append(car.get_name())
            positions = car.car_coordinates()
            for pos in positions:
                if pos in self.cell_list:
                    if not self.cell_content((pos[0],pos[1])):
                        board.list_of_car_names.remove(car.get_name())
                        return False
                else:
                    board.list_of_car_names.remove(car.get_name())
                    return False
            for pos in positions:
                self.board[pos[0][pos[1]]] = car.get_name()
        else:
            return False
        return True

    def move_car(self, name, movekey):
        """
        moves car one step in given direction.
        :param name: name of the car to move
        :param movekey: Key of move in car to activate
        :return: True upon success, False otherwise
        """
        # implement your code and erase the "pass"
        # [('O','d',"some description"),('R','r',"some description"),('O','u',"some description")]
        #pos_moves = self.possible_moves()
        requeired_spot = car.movement_requirements(movekey)
        if requeired_spot[0] in self.cell_list():
            if self.board[[requeired_spot[0][0]][requeired_spot[0][1]]] == "_":
                self.board[[requeired_spot[0][0]][requeired_spot[0][1]]] = name
                self.board[[car.location[0]][car.location[1]]] = "_"
                return True
            else:
                return False
        return False




if __name__ == '__main__':
    car = Car("Red", 3, (0, 0), 0)
    board = Board()
    