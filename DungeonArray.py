import Locations, random

map_of_dungeon = [[0] * 100 for i in range(100)]


# kind of fun but these rooms in no way line up (!)
# RANDOM dungeon time baby.  The rooms not at all lining up means you can't actually go back
# some of the time.   Really the random needs to see the other rooms around it and make rooms that fit
#  that is doable but more work. This code makes a 100 by 100 grid of locations.

def make_mega_dungeon():
    for x in range(100):
        for y in range(100):
            map_of_dungeon[x][y] = make_random_location()
            print("Added a room to (", x, ",", y, ":  ", map_of_dungeon[x][y].long_description())


# make a completely random location, it might make no sense. First define which exits are going to exist,
# then decide if it's a room or corridor randomly. All rooms are the same, but corridors come in types
# based on the number of exits - 1, 2, 3,4.  T-junctions have 3, dead ends have 1.

def make_random_location():
    exits = define_exits()
    rando = random.randint(0, 1)
    if rando == 0:
        # its-a-a-room
        return Locations.Room(exits)
    else:
        # it's a corridor
        if len(exits) == 1:
            return Locations.DeadEnd(exits)
        elif len(exits) == 3:
            return Locations.TJunction(exits)
        else:
            return Locations.Corridor(exits)


# randomly select how many exits (1-4 possible exits) then choose what direction they are in -
# the exits must all be in different directions
def define_exits():
    possible_exit_list = [Locations.NORTH, Locations.SOUTH, Locations.EAST, Locations.WEST]
    number_of_exits = random.randint(1, 4)
    actual_exit_list = []

    for x in range(0, number_of_exits):
        r = random.randint(0, len(possible_exit_list) - 1)
        direction_chosen = possible_exit_list[r]
        actual_exit_list.append(direction_chosen)
        possible_exit_list.remove(direction_chosen)

    return actual_exit_list


def get_location(x, y):
    return map_of_dungeon[x][y]


# This looks at where you are and prompts you to for which way to go. It checks if the choice is in the list
# of exits, if it is it moves you that way, if it isn't it tells you and makes you loop until you do.

def travel_in_dungeon(coordinates, current_location):

    while(1):
        print("Which direction do you want to go? (Type letter)")
        direction = str(input("Direction>")).upper()
        if direction == 'N':
            desired_direction = Locations.NORTH
        elif direction == 'S':
            desired_direction = Locations.SOUTH
        elif direction == 'E':
            desired_direction = Locations.EAST
        elif direction == 'W':
            desired_direction = Locations.WEST
        if desired_direction in current_location.get_exits():
            print("You set off walking")
            desired_direction.move(coordinates)
            return
        else:
            print("That is not a valid direction")

# The main loop of this mini demo - first we make a mega dungeon (100 by 100). Then start the player at 50, 50
# on the map. Then loop - showing them the location, then allowing them to travel.

def play_the_game():
    make_mega_dungeon()
    coordinates = [50, 50]
    current_location = get_location(coordinates[0], coordinates[1])

    while(1):
        print("You are in the dungeon. " + current_location.long_description())
        print("(co-ordinates are  ", coordinates[0], coordinates[1], ")")
        travel_in_dungeon(coordinates, current_location)
        current_location = get_location(coordinates[0], coordinates[1])


# fires up the game!

play_the_game()