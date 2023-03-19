class Room:
 def __init__(self, description, north, east, south, west):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west
def main():
    room_list = []
    current_room = 0
    next_room = 0
    done = False
    room = Room("You are in the Kitchen, there is a door to the east.", None, 1, None, None)
    room_list.append(room)
    room = Room("You are in the North Hall, there is a door to the east, south, and west.", None, 2, 4, 0)
    room_list.append(room)
    room = Room("You are in the First Bedroom, there is a door to the west and south.", None, None, 4, 1)
    room_list.append(room)
    room = Room("You are in the South Hall, there is a door to the north, east, south, and west.", 1, 2, 4, 3)
    room_list.append(room)
    room = Room("You are in the Second Bedroom, there is a door to the east.", None, 4, None, None)
    room_list.append(room)
    room = Room("You are in the Third Bedroom, there is a door to the north..", 4, None, None, None)
    room_list.append(room)
    while not done:
        print(room_list[current_room].description)
        direction = input("Which way would you like to go? (n s e w)").lower()
        if direction[0] == 'n':
            next_room = room_list[current_room].north
        elif direction[0] == 's':
            next_room = room_list[current_room].south
        elif direction[0] == 'e':
            next_room = room_list[current_room].east
        elif direction[0] == 'w':
            next_room = room_list[current_room].west
        elif direction[0] == 'q':
            print("You have quit the game. GG")
            break
        else:
            print("You can only go n s e w or q to quit.")
            continue
        if next_room == None:
            print("Please pick a direction you actually can go :]")
            continue
        current_room = next_room

main()
