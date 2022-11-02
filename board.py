from car import Car
class Board:
    """
    Add a class description here.
    Write briefly about the purpose of the class
    """

    def __init__(self):
        self.row = 7
        self.col = 7
        self.board = []
        for line in range(self.row):
            self.boardhelp = []
            for col in range(self.col):
                if col ==6 and line ==3:
                    self.boardhelp.append('_')
                self.boardhelp.append('_')
            self.board.append(self.boardhelp)
        self.target = (3,7)
        self.list_of_car_names = []
        self.cell_list_ = self.cell_list()
        self.car_names = []



    def __str__(self):
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board
        """
        return str(self.board)

    def cell_list(self):
        """ This function returns the coordinates of cells in this board
        :return: list of coordinates
        """
        return [(i,j) for i in range(self.row) for j in range(self.col)] + [(3,7)]

    def possible_moves(self):
        """ This function returns the legal moves of all cars in this board
        :return: list of tuples of the form (name,movekey,description)
                 representing legal moves
        """
        self.pos_moves = []
        for car in self.list_of_car_names:
            possible_moves = car.possible_moves() #{u: "bla", d: :"bla"}
            for key in possible_moves:
                needed_pos = car.movement_requirements(key)
                if needed_pos[0] in self.cell_list_:
                    if not self.cell_content(needed_pos[0]):
                        self.pos_moves.append((car.get_name(),key, possible_moves.get(key)))
        return self.pos_moves


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
            car_name = pos
            return car_name
        else:
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
        if car.location in self.cell_list_ and car.get_name() not in self.car_names:
            self.list_of_car_names.append(car)
            self.car_names.append(car.get_name())
            positions = car.car_coordinates()
            for pos in positions:
                if pos in self.cell_list_:
                    if  self.cell_content((pos[0],pos[1])):
                        self.list_of_car_names.remove(car)
                        self.car_names.remove(car.get_name())
                        return False
                else:
                    self.car_names.remove(car.get_name())
                    self.list_of_car_names.remove(car)
                    return False
            for pos in positions:
                self.board[pos[0]][pos[1]] = car.get_name()
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
        pos_moves = self.possible_moves()
        for car in self.list_of_car_names:
            if name == car.get_name():
                for i in range(len(pos_moves)):
                    if name == self.possible_moves()[i][0]:
                        if movekey == self.possible_moves()[i][1]:
                            self.board[car.location[0]][car.location[1]] = "_"
                            self.board[car.movement_requirements(movekey)[0][0]][car.movement_requirements(movekey)[0][1]] = car.get_name()
                            car.move(movekey)
                            return True

        return False






    