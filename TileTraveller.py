

#  Fall fyrir hverja tile ----- tile(1.2)
#  while lykkja sem útilokar 3.1
#  

#  prenta victory 
#

# fall fyrir tile_1.1
def tile_1.1():
   
    if direction == "n" or direction == "N":
        current_tile = 1.2

    else:
        return print("Not a valid direction!")   

# fall fyrir tile_1.2
def tile_1.2():
    
    if direction == "n" or direction == "N":
        current_tile = 1.3
    elif direction == "e" or direction == "E":
        current_tile = 2.2
    elif direction == "s" or direction == "S":
        current_tile = 1.1
    else:
        return print("Not a valid direction!")

# fall fyrir tile_1.3
def tile_1.3():

    if direction == "e" or direction == "E":
        current_tile = 2.3
    elif direction == "s" or direction == "S":
        current_tile = 1.2
    else:
        return print("Not a valid direction!")


# fall fyrir tile_2.1
def tile_2.1():
    
    if direction == "n" or direction == "N":
        current_tile = 2.2
    else:
        return print("Not a valid direction!")




# fall fyrir tile_2.2
def tile_2.2():

    if direction == "w" or direction == "W":
        current_tile = 1.2
    elif direction == "s" or direction == "S":
        current_tile = 2.1
    else:
        return print("Not a valid direction!")



#fall fyrir tile_2.3
def tile_2.3():

    if direction == "w" or direction == "W":
        current_tile = 1.3
    elif direction == "e" or direction == "E":
        current_tile = 3.3
    else:
        return print("Not a valid direction!")




#fall fyrir tile_3.3
def tile_3.3():

    if direction == "w" or direction == "W":
        current_tile = 2.3
    elif direction == "s" or direction == "S":
        current_tile = 3.2
    else:
        return print("Not a valid direction!") 

current_tile = 1.1

# skipanir ef við erum stödd á tile_1.1 sem kallar í viðeigandi fall
if current_tile = 1.1:

    print("You can travel (N)orth.")
    
    direction = input("Direction: ")

    print(tile_1.1())

# skipanir ef við erum stödd á tile_1.2 sem kallar í viðeigandi fall
if current_tile == 1.2:

    print("You can travel (N)orth or (E)ast or (S)outh.")

    direction = input("Direction: ")

    print(tile_1.2())

# skipanir ef við erum stödd á tile_1.3 sem kallar í viðeigandi fall
 if current_tile == 1.3:

    print("You can travel (E)ast or (S)outh.")

    direction = input("Direction: ")

    print(tile_1.3())


# skipanir ef við erum stödd á tile_2.1 sem kallar í viðeigandi fall
if current_tile == 2.1:
    
    print("You can travel (N)orth.")
    
    direction = input("Direction: ")

    print(tile_2.1())


# skipanir ef við erum stödd á tile_2.2 sem kallar í viðeigandi fall
if current_tile == 2.2:
    
    print("You can travel (S)outh or (W)est.")
    
    direction = input("Direction: ")

    print(tile_2.2())

#skipanir ef við erum stödd á tile_2.3 sem kallar í viðeigandi fall
if current_tile == 2.3:

    print("You can travel (E)ast or (W)est.")
    
    direction = input("Direction: ")

    print(tile_2.3())


#skipanir ef við erum stödd á tile_3.3 sem kallar í viðeigandi fall
if current_tile == 3.3:
    
    print("You can travel (S)outh or (W)est.")
    
    direction = input("Direction: ")
    
    print(tile_3.3())




        
   

   



       

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



