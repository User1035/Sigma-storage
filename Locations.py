class Location:

    def __init__(self, list_of_exits):
        self.available_exits = list_of_exits

    def description(self):
        return "Some weird generic location"

    def get_exits(self):
        return self.available_exits

    def long_description(self):
        description = self.description() + " with exits leading to the"
        for this_exit in self.available_exits:
            description = description + " " + this_exit.name
        return description


class Room(Location):

    def description(self):
        return "A stone floored room"


class Corridor(Location):

    def description(self):
        return "A long corridor"


class TJunction(Location):

    def description(self):
        return "A T-Junction"


class DeadEnd(Corridor):

    def description(self):
        return "A dead end"


class CompassPoint:

    def __init__(self):
        self.name = "undefined"

    def move(self, coordinates):
        print("Abstract class, why call?")


class North(CompassPoint):

    def __init__(self):
        self.name = "North"

    # increment Y position by one
    def move(self, coordinates):
        coordinates[1] = coordinates[1] + 1


class South(CompassPoint):

    def __init__(self):
        self.name = "South"

    # decrement Y position by one
    def move(self, coordinates):
        coordinates[1] = coordinates[1] - 1


class East(CompassPoint):

    def __init__(self):
        self.name = "East"

    # increment x position by one
    def move(self, coordinates):
        coordinates[0] = coordinates[0] + 1


class West(CompassPoint):

    def __init__(self):
        self.name = "West"

    # decrement x position by one
    def move(self, coordinates):
        coordinates[0] = coordinates[0] - 1


NORTH = North()
SOUTH = South()
EAST = East()
WEST = West()
