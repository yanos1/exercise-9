
class Car:
    """
    Add class description here
    """
    def __init__(self, name, length, location, orientation):
        """
        A constructor for a Car object
        :param name: A string representing the car's name
        :param length: A positive int representing the car's length.
        :param location: A tuple representing the car's head (row, col) location
        :param orientation: One of either 0 (VERTICAL) or 1 (HORIZONTAL)
        """
        # Note that this function is required in your Car implementation.
        # However, is not part of the API for general car types.
        self.name = name
        self.length = length
        self.location = location
        self.orientation = orientation
        self.requirements = []


    def car_coordinates(self):
        """
        :return: A list of coordinates the car is in
        """
        if self.orientation == 0:
            self.coordinates = [(i,self.location[1]) for i in range(self.location[0],self.location[0]+self.length)]
        else:
            self.coordinates = [(self.location[0],i) for i in range(self.location[1],self.location[1]+self.length)]
        return self.coordinates



    def possible_moves(self):
        """
        :return: A dictionary of strings describing possible movements permitted by this car.
        """
        self.moves_dict = {}
        if self.orientation == 0:
            self.moves_dict["u"] = "up to the skies"
            self.moves_dict["d"] = "down, but not for long"
        else:
            self.moves_dict["r"] = "right is right"
            self.moves_dict["l"] = "left isnt bad"
        return self.moves_dict



    def movement_requirements(self, movekey):
        """
        :param movekey: A string representing the key of the required move.
        :return: A list of cell locations which must be empty in order for this move to be legal.
        """
        print(self.location)
        if self.orientation == 0:
            if movekey == "u":
                self.requirements.append((self.location[0]-1,self.location[1]))
            elif movekey == "d":
                self.requirements.append((self.location[0]+self.length, self.location[1]))
        elif self.orientation == 1:
            if movekey == "l":
                self.requirements.append((self.location[0], self.location[1]-1))
            elif movekey == "r":
                self.requirements.append((self.location[0], self.location[1]+self.length))
        return self.requirements


    def move(self, movekey):
        """
        :param movekey: A string representing the key of the required move.
        :return: True upon success, False otherwise
        """
        empty_pos = car.movement_requirements(movekey)
        print("empty pos needed = :", empty_pos)
        if empty_pos[-1]:
            return True
        return False


    def get_name(self):
        """
        :return: The name of this car.
        """
        return self.name


#if __name__ == '__main__':
car = Car("Red", 3, (0, 0), 0)
