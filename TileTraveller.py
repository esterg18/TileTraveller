

#  Fall fyrir hverja tile ----- tile(1.2)
#  while lykkja sem útilokar 3.1
#  

#  prenta victory 
#

def tile_1.1():
   
    if direction == "n" or direction == "N":
        current_tile = 1.2

    else:
        return print("Not a valid direction!")   


current_tile = 1.1

if current_tile = 1.1:

    print("You can travel (N)orth.")
    
    direction = input("Direction: ")

    print(tile_1.1())






if current_tile == 1.1:

        
    elif current_tile == 1.2:
        print("You can travel (N)orth or (E)ast or (S)outh.")
        direction = input("Direction: ")
        if direction == "n" or direction == "N":
            current_tile = 1.3
        elif direction == "e" or direction == "E":
            current_tile = 2.2
        elif direction == "s" or direction == "S":
            current_tile = 1.1
        else:
            print("Not a valid direction!")

    elif current_tile == 1.3:
        print("You can travel (E)ast or (S)outh.")
        direction = input("Direction: ")
        if direction == "e" or direction == "E":
            current_tile = 2.3
        elif direction == "s" or direction == "S":
            current_tile = 1.2
        else:
            print("Not a valid direction!")

    elif current_tile == 2.1:
        print("You can travel (N)orth.")
        direction = input("Direction: ")
        if direction == "n" or direction == "N":
            current_tile = 2.2
        else:
            print("Not a valid direction!")

    elif current_tile == 2.2:
        print("You can travel (S)outh or (W)est.")
        direction = input("Direction: ")
        if direction == "w" or direction == "W":
            current_tile = 1.2
        elif direction == "s" or direction == "S":
            current_tile = 2.1
        else:
            print("Not a valid direction!")

    elif current_tile == 2.3:
        print("You can travel (E)ast or (W)est.")
        direction = input("Direction: ")
        if direction == "w" or direction == "W":
            current_tile = 1.3
        elif direction == "e" or direction == "E":
            current_tile = 3.3
        else:
            print("Not a valid direction!")

    elif current_tile == 3.3:
        print("You can travel (S)outh or (W)est.")
        direction = input("Direction: ")
        if direction == "w" or direction == "W":
            current_tile = 2.3
        elif direction == "s" or direction == "S":
            current_tile = 3.2
        else:
            print("Not a valid direction!")        

    elif current_tile == 3.2:
        print("You can travel (N)orth or (S)outh.")
        direction = input("Direction: ")
        if direction == "n" or direction == "N":
            current_tile = 3.3
        elif direction == "s" or direction == "S":
            current_tile = 3.1
        else:
            print("Not a valid direction!") 


print("Victory!")



