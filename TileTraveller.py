#  Fall fyrir hverja tile ----- tile(1.2)
#  while lykkja sem útilokar 3.1
#  prenta victory 

# fall fyrir tile_1.1
def tile_1_1(direction):
   
    if direction == "n" or direction == "N":
        current_tile = "1.2"
        return current_tile

    else:
        error = "Not a valid direction!"
        return error

# fall fyrir tile_1.2
def tile_1_2(direction):
    
    if direction == "n" or direction == "N":
        current_tile = "1.3"
        return current_tile
    elif direction == "e" or direction == "E":
        current_tile = "2.2"
        return current_tile
    elif direction == "s" or direction == "S":
        current_tile = "1.1"
        return current_tile
    else:
        error = "Not a valid direction!"
        return error


# fall fyrir tile_1.3
def tile_1_3(direction):

    if direction == "e" or direction == "E":
        current_tile = "2.3"
        return current_tile
    elif direction == "s" or direction == "S":
        current_tile = "1.2"
        return current_tile
    else:
        error = "Not a valid direction!"
        return error



# fall fyrir tile_2.1
def tile_2_1(direction):
    
    if direction == "n" or direction == "N":
        current_tile = "2.2"
        return current_tile
    else:
        error = "Not a valid direction!"
        return error

# fall fyrir tile_2.2
def tile_2_2(direction):

    if direction == "w" or direction == "W":
        current_tile = "1.2"
        return current_tile
    elif direction == "s" or direction == "S":
        current_tile = "2.1"
        return current_tile
    else:
        error = "Not a valid direction!"
        return error



#fall fyrir tile_2.3
def tile_2_3(direction):

    if direction == "w" or direction == "W":
        current_tile = "1.3"
        return current_tile
    elif direction == "e" or direction == "E":
        current_tile = "3.3"
        return current_tile
    else:
        error = "Not a valid direction!"
        return error

#fall fyrir tile_3.3
def tile_3_3(direction):

    if direction == "w" or direction == "W":
        current_tile = "2.3"
        return current_tile
    elif direction == "s" or direction == "S":
        current_tile = "3.2"
        return current_tile
    else:
        error = "Not a valid direction!"
        return error


#fall fyrir tile_3.2     
def tile_3_2(direction):
    if direction == "n" or direction == "N":
        current_tile = "3.3"
        return current_tile
    elif direction == "s" or direction == "S":
        current_tile = "3.1"
        return current_tile
    else:
        error = "Not a valid direction!"
        return error


current_tile = "1.1"

while current_tile != "3.1":

    # skipanir ef við erum stödd á tile_1.1 sem kallar í viðeigandi fall
    if current_tile == "1.1":

        print("You can travel: (N)orth.")
        
        direction = input("Direction: ")

        answer = tile_1_1(direction)

        if answer == "Not a valid direction!":
            print(answer)
            

        else:      
            current_tile = answer

    # skipanir ef við erum stödd á tile_1.2 sem kallar í viðeigandi fall
    elif current_tile == "1.2":

        print("You can travel: (N)orth or (E)ast or (S)outh.")

        direction = input("Direction: ")
       
        answer = tile_1_2(direction)

        if answer == "Not a valid direction!":
            print(answer)
            
        else:      
            current_tile = answer
                


    # skipanir ef við erum stödd á tile_1.3 sem kallar í viðeigandi fall
    elif current_tile == "1.3":

        print("You can travel: (E)ast or (S)outh.")

        direction = input("Direction: ")

        answer = tile_1_3(direction)

        if answer == "Not a valid direction!":
            print(answer)
        else:      
            current_tile = answer


    # skipanir ef við erum stödd á tile_2.1 sem kallar í viðeigandi fall
    elif current_tile == "2.1":
        
        print("You can travel: (N)orth.")
        
        direction = input("Direction: ")
        
        answer = tile_2_1(direction)

        if answer == "Not a valid direction!":
            print(answer)
           
        else:      
            current_tile = answer
    

    # skipanir ef við erum stödd á tile_2.2 sem kallar í viðeigandi fall
    elif current_tile == "2.2":
        
        print("You can travel: (S)outh or (W)est.")
        
        direction = input("Direction: ")
       
        answer = tile_2_2(direction)

        if answer == "Not a valid direction!":
            print(answer)
          
        else:      
            current_tile = answer

    #skipanir ef við erum stödd á tile_2.3 sem kallar í viðeigandi fall
    elif current_tile == "2.3":

        print("You can travel: (E)ast or (W)est.")
        
        direction = input("Direction: ")
        
        answer = tile_2_3(direction)

        if answer == "Not a valid direction!":
            print(answer)
            
        else:      
            current_tile = answer


    #skipanir ef við erum stödd á tile_3.3 sem kallar í viðeigandi fall
    elif current_tile == "3.3":
        
        print("You can travel: (S)outh or (W)est.")
        
        direction = input("Direction: ")
        
        answer = tile_3_3(direction)

        if answer == "Not a valid direction!":
            print(answer)
            
        else:      
            current_tile = answer



    #skipanir ef við erum stödd á tile_3.2 sem kallar í viðeigandi fall
    elif current_tile == "3.2":
        print("You can travel: (N)orth or (S)outh.")

        direction = input("Direction: ")

        answer = tile_3_2(direction)

        if answer == "Not a valid direction!":
            print(answer)
            
        else:      
            current_tile = answer



    #direction = input("Direction: ")



print("Victory!")



