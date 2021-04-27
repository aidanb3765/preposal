import random
import turtle

#sets variables for game board
def game_board():

    turtle.setup(700, 700)  # set size of window to size of game board

    wn = turtle.Screen()
    wn.title("Game Board")

    board_img = turtle.bgpic("images/board.png")

    t = turtle.Turtle()

    return (wn, board_img)

#sets variables for each player round
def spin():
    player = turtle.Turtle()
    player.shape("turtle")
    rounds = 0


    while True:
        player.color(random.random(), random.random(), random.random())
        num = 0
        
        spin = random.randint(1,4)
        num += spin
        spin -= 1


        if rounds == 0:
            player.speed(3)
            player.up()
            player.right(270)
            player.forward(160)
            player.up()
            player.down()
            player.stamp()
            rounds += 1

        else:
            for i in range(spin):
                player.right(270)
                player.right(positioning)
                player.up()
                player.backward(160)
                player.right(30)
                player.forward(160)
                player.down()
                player.stamp()
                player.up()
                player.backward(160)

        positioning = player.heading()
            
        player.clear()
        
        

        if (num >= 12):
            num = 1
            pieces(num)

        else:
            pieces(num)

#sets variables for pieces obtained
def pieces(num):

    player = turtle.Turtle()
    player.shape("turtle")
    position = turtle.heading()
    piece_library = []


    #variables to form white diamond ring symbol
    if num == 1:
        player.up()
        player.color("white")
        player.speed(3)
        player.goto(270,270)
        player.setheading(0)
        player.shape("square")
        player.down()
        player.stamp()
        player.up()
            
        player.goto(260,270)
        player.shape("arrow")
        player.right(180)
        player.down()
        player.stamp()
        player.up()
        player.forward(10)
        player.left(90)
        player.forward(10)
        player.left(180)
        player.down()
        player.stamp()
        player.up()
            
        player.goto(260,260)
        player.shape("arrow")
        player.right(180)
        player.down()
        player.stamp()
        player.up()
        player.forward(10)
        player.left(90)
        player.forward(10)
        player.left(180)
        player.down()
        player.stamp()
        player.up()
         
        player.goto(270,250)
        player.shape("arrow")
        player.right(180)
        player.down()
        player.stamp()
        player.up()
        player.forward(10)
        player.left(90)
        player.forward(10)
        player.left(180)
        player.down()
        player.stamp()
        player.up()
          
        player.goto(290,260)
        player.shape("arrow")
        player.right(180)
        player.down()
        player.stamp()
        player.up()
        player.forward(10)
        player.left(90)
        player.forward(10)
        player.left(180)
        player.down()
        player.stamp()
        player.up()
            
        player.setheading(0)
        player.goto(0,0)
        player.shape("turtle")
        player.right(position)
        piece_library.append("W")

    #variables to form the earring symbol
    if num == 2:
        player.up()
        player.speed(3)
        player.goto(220,250)
        player.setheading(0)
        player.shape("circle")
        player.down()
        player.stamp()
        player.up()
        player.goto(230, 250)
        player.shape("square")
        player.down()
        player.stamp()
        player.up()
        player.goto(0,0)
        player.shape("turtle")
        player.right(position)
        piece_library.append("E")

    #variables for forming the any piece
    if num == 3:
        player.up()
        player.speed(3)
        player.goto(190,250)
        player.setheading(0)
        player.shape("triangle")
        player.down()
        player.stamp()
        player.up()
        player.goto(0,0)
        player.shape("turtle")
        player.right(position)
        piece_library.append("Z")

    #variables for forming the color ring
    if num == 4:
        player.up()
        player.color("red")
        player.speed(3)
        player.goto(160,270)
        player.setheading(0)
        player.shape("square")
        player.down()
        player.stamp()
        player.up()
            
        player.goto(150,270)
        player.shape("arrow")
        player.right(180)
        player.down()
        player.stamp()
        player.up()
        player.forward(10)
        player.left(90)
        player.forward(10)
        player.left(180)
        player.down()
        player.stamp()
        player.up()
            
        player.goto(150,260)
        player.shape("arrow")
        player.right(180)
        player.down()
        player.stamp()
        player.up()
        player.forward(10)
        player.left(90)
        player.forward(10)
        player.left(180)
        player.down()
        player.stamp()
        player.up()
            
        player.goto(160,250)
        player.shape("arrow")
        player.right(180)
        player.down()
        player.stamp()
        player.up()
        player.forward(10)
        player.left(90)
        player.forward(10)
        player.left(180)
        player.down()
        player.stamp()
        player.up()
        
        player.goto(180,260)
        player.shape("arrow")
        player.right(180)
        player.down()
        player.stamp()
        player.up()
        player.forward(10)
        player.left(90)
        player.forward(10)
        player.left(180)
        player.down()
        player.stamp()
        player.up()
            
        player.setheading(0)
        player.goto(0,0)
        player.shape("turtle")
        player.right(position)
        piece_library.append("R")

        if len(piece_library) == 4:
            return "We have a winner!"

#creates a game run for the computer
def computer_rules():
    turnTotal = 0
    pieces = []

    #runs through the game board
    while True:
        spin = random.randint(1,4)
        print("You spun: ", spin)

        turnTotal += spin

        #loop verifies usage of a the board when a full turn is made
        if turnTotal > 12:
            turnTotal = turnTotal % 12

            if turnTotal == 1:
                if "white ring" not in pieces:
                    print("Uh oh! You got the white ring! Careful!")
                    pieces.append("white ring")

                else:
                    print("You have this piece already.")
            
            elif turnTotal == 2:
                if "earrings" not in pieces:
                    print("You got the earrings!")
                    pieces.append("earrings")

                else:
                    print("You have this piece already.")

            elif turnTotal == 3:
                while True:
                    if "earrings" not in pieces:
                        print("You chose the earrings!")
                        pieces.append("earrings")
                        break

                    elif "ring" not in pieces:
                        print("You chose the ring!")
                        pieces.append("ring")
                        break

                    elif "crown" not in pieces:
                        print("You chose the crown!")
                        pieces.append("crown")
                        break

                    elif "bracelet" not in pieces:
                        print("You chose the bracelet!")
                        pieces.append("bracelet")
                        break

                    elif "necklace" not in pieces:
                        print("You chose the necklace!")
                        pieces.append("necklace")
                        break

            elif turnTotal == 4:
                if "ring" not in pieces:
                    print("You got a ring!")
                    pieces.append("ring")

                else:
                    print("You have this piece already.")

            elif turnTotal == 5:
                if "bracelet" not in pieces:
                    print("You got a bracelet!")
                    pieces.append("bracelet")

                else:
                    print("You have this piece already.")

            elif turnTotal == 6:
                if not pieces:
                    print("No pieces left.")
                    
                while True:
                    if "earrings" in pieces:
                        print("You chose the earrings!")
                        pieces.remove("earrings")
                        break

                    elif "ring" in pieces:
                        print("You chose the ring!")
                        pieces.remove("ring")
                        break

                    elif "crown" in pieces:
                        print("You chose the crown!")
                        pieces.remove("crown")
                        break

                    elif "bracelet" in pieces:
                        print("You chose the bracelet!")
                        pieces.remove("bracelet")
                        break

                    elif "necklace" in pieces:
                        print("You chose the necklace!")
                        pieces.remove("necklace")
                        break

            elif turnTotal == 7:
                if "necklace" not in pieces:
                    print("You got a necklace!")
                    pieces.append("necklace")

                else:
                    print("You have this piece already.")

            elif turnTotal == 8:
                if "crown" not in pieces:
                    print("You got a crown!")
                    pieces.append("crown")

                else:
                    print("You have this piece already.")

            elif turnTotal == 9:
                if "white ring" not in pieces:
                    print("Uh oh! You got the white ring! Careful!")
                    pieces.append("white ring")

            elif turnTotal == 10:
                if not pieces:
                    print("No pieces left.")
                    
                while True:
                    if "earrings" in pieces:
                        print("You chose the earrings!")
                        pieces.remove("earrings")
                        break

                    elif "ring" in pieces:
                        print("You chose the ring!")
                        pieces.remove("ring")
                        break

                    elif "crown" in pieces:
                        print("You chose the crown!")
                        pieces.remove("crown")
                        break

                    elif "bracelet" in pieces:
                        print("You chose the bracelet!")
                        pieces.remove("bracelet")
                        break

                    elif "necklace" in pieces:
                        print("You chose the necklace!")
                        pieces.remove("necklace")
                        break

            elif turnTotal == 11:
                if "necklace" not in pieces:
                    print("You got a necklace")
                    pieces.append("necklace")

                else:
                    print("You have this piece already.")

            elif turnTotal == 12:
                while True:
                    if "earrings" not in pieces:
                        print("You chose the earrings!")
                        pieces.append("earrings")
                        break

                    elif "ring" not in pieces:
                        print("You chose the ring!")
                        pieces.append("ring")
                        break

                    elif "crown" not in pieces:
                        print("You chose the crown!")
                        pieces.append("crown")
                        break

                    elif "bracelet" not in pieces:
                        print("You chose the bracelet!")
                        pieces.append("bracelet")
                        break

                    elif "necklace" not in pieces:
                        print("You chose the necklace!")
                        pieces.append("necklace")
                        break

        #loop for run of the game without having to reset turn
        else:
            turnTotal = turnTotal % 12

            if turnTotal == 1:
                if "white ring" not in pieces:
                    print("Uh oh! You got the white ring! Careful!")
                    pieces.append("white ring")

                else:
                    print("You have this piece already.")
            
            elif turnTotal == 2:
                if "earrings" not in pieces:
                    print("You got the earrings!")
                    pieces.append("earrings")

                else:
                    print("You have this piece already.")

            elif turnTotal == 3:
                while True:
                    if "earrings" not in pieces:
                        print("You chose the earrings!")
                        pieces.append("earrings")
                        break

                    elif "ring" not in pieces:
                        print("You chose the ring!")
                        pieces.append("ring")
                        break

                    elif "crown" not in pieces:
                        print("You chose the crown!")
                        pieces.append("crown")
                        break

                    elif "bracelet" not in pieces:
                        print("You chose the bracelet!")
                        pieces.append("bracelet")
                        break

                    elif "necklace" not in pieces:
                        print("You chose the necklace!")
                        pieces.append("necklace")
                        break

            elif turnTotal == 4:
                if "ring" not in pieces:
                    print("You got a ring!")
                    pieces.append("ring")

                else:
                    print("You have this piece already.")

            elif turnTotal == 5:
                if "bracelet" not in pieces:
                    print("You got a bracelet!")
                    pieces.append("bracelet")

                else:
                    print("You have this piece already.")

            elif turnTotal == 6:
                if not pieces:
                    print("No pieces left.")
                    
                while True:
                    if "earrings" in pieces:
                        print("You chose the earrings!")
                        pieces.remove("earrings")
                        break

                    elif "ring" in pieces:
                        print("You chose the ring!")
                        pieces.remove("ring")
                        break

                    elif "crown" in pieces:
                        print("You chose the crown!")
                        pieces.remove("crown")
                        break

                    elif "bracelet" in pieces:
                        print("You chose the bracelet!")
                        pieces.remove("bracelet")
                        break

                    elif "necklace" in pieces:
                        print("You chose the necklace!")
                        pieces.remove("necklace")
                        break

            elif turnTotal == 7:
                if "necklace" not in pieces:
                    print("You got a necklace!")
                    pieces.append("necklace")

                else:
                    print("You have this piece already.")

            elif turnTotal == 8:
                if "crown" not in pieces:
                    print("You got a crown!")
                    pieces.append("crown")

                else:
                    print("You have this piece already.")

            elif turnTotal == 9:
                if "white ring" not in pieces:
                    print("Uh oh! You got the white ring! Careful!")
                    pieces.append("white ring")

            elif turnTotal == 10:
                if not pieces:
                    print("No pieces left.")
                    
                while True:
                    if "earrings" in pieces:
                        print("You chose the earrings!")
                        pieces.remove("earrings")
                        break

                    elif "ring" in pieces:
                        print("You chose the ring!")
                        pieces.remove("ring")
                        break

                    elif "crown" in pieces:
                        print("You chose the crown!")
                        pieces.remove("crown")
                        break

                    elif "bracelet" in pieces:
                        print("You chose the bracelet!")
                        pieces.remove("bracelet")
                        break

                    elif "necklace" in pieces:
                        print("You chose the necklace!")
                        pieces.remove("necklace")
                        break

            elif turnTotal == 11:
                if "necklace" not in pieces:
                    print("You got a necklace")
                    pieces.append("necklace")

                else:
                    print("You have this piece already.")

            elif turnTotal == 12:
                while True:
                    if "earrings" not in pieces:
                        print("You chose the earrings!")
                        pieces.append("earrings")
                        break

                    elif "ring" not in pieces:
                        print("You chose the ring!")
                        pieces.append("ring")
                        break

                    elif "crown" not in pieces:
                        print("You chose the crown!")
                        pieces.append("crown")
                        break

                    elif "bracelet" not in pieces:
                        print("You chose the bracelet!")
                        pieces.append("bracelet")
                        break

                    elif "necklace" not in pieces:
                        print("You chose the necklace!")
                        pieces.append("necklace")
                        break

        
        if ("earrings" in pieces and "crown" in pieces and "ring" in pieces and "bracelet"in pieces and "necklace" in pieces) or ("earrings" in pieces and "crown" in pieces and "ring" in pieces and "bracelet" in pieces and "necklace" in pieces and "white" in pieces):
            break


    return pieces

#runs the game for the player
def rules():
    turnTotal = 0
    pieces = []

    #runs through the game board
    while True:
        spin = random.randint(1,4)
        print("You spun: ", spin)

        turnTotal += spin

        #loop verifies usage of a the board when a full turn is made
        if turnTotal > 12:
            turnTotal = turnTotal % 12

            if turnTotal == 1:
                if "white ring" not in pieces:
                    print("Uh oh! You got the white ring! Careful!")
                    pieces.append("white ring")

                else:
                    print("You have this piece already.")
            
            elif turnTotal == 2:
                if "earrings" not in pieces:
                    print("You got the earrings!")
                    pieces.append("earrings")

                else:
                    print("You have this piece already.")

            elif turnTotal == 3:
                proceed = input("You can choose: an earring, ring, crown, bracelet, or necklace! What do you want?")
                proceed = proceed.lower()

                while proceed != "earrings" and proceed != "ring" and proceed != "crown" and proceed != "bracelet" and proceed != "necklace":
                    print("Please enter a valid object such as earrings, ring, crown, bracelet, or necklace.")
                    proceed = input("What do you want?")
                    proceed = proceed.lower()
                    
                while proceed == "earrings" or proceed == "ring" or proceed == "crown" or proceed == "bracelet" or proceed == "necklace":
                    if proceed in pieces:
                        print("Try again! You already have this.")
                        proceed = input("What do you want?")
                        proceed = proceed.lower()

                    elif proceed == "earrings":
                        print("You chose the earrings!")
                        pieces.append("earrings")
                        break

                    elif proceed == "ring":
                        print("You chose the ring!")
                        pieces.append("ring")
                        break

                    elif proceed == "crown":
                        print("You chose the crown!")
                        pieces.append("crown")
                        break

                    elif proceed == "bracelet":
                        print("You chose the bracelet!")
                        pieces.append("bracelet")
                        break

                    elif proceed == "necklace":
                        print("You chose the necklace!")
                        pieces.append("necklace")
                        break

            elif turnTotal == 4:
                if "ring" not in pieces:
                    print("You got a ring!")
                    pieces.append("ring")

                else:
                    print("You have this piece already.")

            elif turnTotal == 5:
                if "bracelet" not in pieces:
                    print("You got a bracelet!")
                    pieces.append("bracelet")

                else:
                    print("You have this piece already.")

            elif turnTotal == 6:
                proceed = input("Uh oh! Put an item back! What do you want to give up?")
                proceed = proceed.lower()

                if not proceed:
                    print("No pieces left.")
            
                while proceed != "earrings" and proceed != "ring" and proceed != "crown" and proceed != "bracelet" and proceed != "necklace":
                    print("Please enter a valid object such as earrings, ring, crown, bracelet, or necklace.")
                    proceed = input("Uh oh! Put an item back! What do you want to give up?")
                    proceed = proceed.upper()

                while proceed == "earrings" or proceed == "ring" or proceed == "crown" or proceed == "bracelet" or proceed == "necklace":
                    if proceed not in pieces:
                        print("Try again! You don't have this piece.")
                        proceed = input("What do you want?")
                        proceed = proceed.lower()

                    elif proceed == "earrings":
                        print("You chose the earrings!")
                        pieces.remove("earrings")
                        break

                    elif proceed == "ring":
                        print("You chose the ring!")
                        pieces.remove("ring")
                        break

                    elif proceed == "crown":
                        print("You chose the crown!")
                        pieces.remove("crown")
                        break

                    elif proceed == "bracelet":
                        print("You chose the bracelet!")
                        pieces.remove("bracelet")
                        break

                    elif proceed == "necklace":
                        print("You chose the necklace!")
                        pieces.remove("necklace")
                        break
                        
            elif turnTotal == 7:
                if "necklace" not in pieces:
                    print("You got a necklace!")
                    pieces.append("necklace")

                else:
                    print("You have this piece already.")

            elif turnTotal == 8:
                if "crown" not in pieces:
                    print("You got a crown!")
                    pieces.append("crown")

                else:
                    print("You have this piece already.")

            elif turnTotal == 9:
                if "white ring" not in pieces:
                    print("Uh oh! You got the white ring! Careful!")
                    pieces.append("white ring")

            elif turnTotal == 10:
                proceed = input("Uh oh! Put an item back! What do you want to give up?")
                proceed = proceed.lower()

                if not proceed:
                    print("No pieces left.")
            
                while proceed != "earrings" and proceed != "ring" and proceed != "crown" and proceed != "bracelet" and proceed != "necklace":
                    print("Please enter a valid object such as earrings, ring, crown, bracelet, or necklace.")
                    proceed = input("Uh oh! Put an item back! What do you want to give up?")
                    proceed = proceed.upper()

                while proceed == "earrings" or proceed == "ring" or proceed == "crown" or proceed == "bracelet" or proceed == "necklace":
                    if proceed not in pieces:
                        print("Try again! You don't have this piece.")
                        proceed = input("What do you want?")
                        proceed = proceed.lower()

                    elif proceed == "earrings":
                        print("You chose the earrings!")
                        pieces.remove("earrings")
                        break

                    elif proceed == "ring":
                        print("You chose the ring!")
                        pieces.remove("ring")
                        break

                    elif proceed == "crown":
                        print("You chose the crown!")
                        pieces.remove("crown")
                        break

                    elif proceed == "bracelet":
                        print("You chose the bracelet!")
                        pieces.remove("bracelet")
                        break

                    elif proceed == "necklace":
                        print("You chose the necklace!")
                        pieces.remove("necklace")
                        break

            elif turnTotal == 11:
                if "necklace" not in pieces:
                    print("You got a necklace")
                    pieces.append("necklace")

                else:
                    print("You have this piece already.")

            elif turnTotal == 12:
                proceed = input("You can choose: an earring, ring, crown, bracelet, or necklace! What do you want?")
                proceed = proceed.lower()

                while proceed != "earrings" and proceed != "ring" and proceed != "crown" and proceed != "bracelet" and proceed != "necklace":
                    print("Please enter a valid object such as earrings, ring, crown, bracelet, or necklace.")
                    proceed = input("What do you want?")
                    proceed = proceed.lower()
                    
                while proceed == "earrings" or proceed == "ring" or proceed == "crown" or proceed == "bracelet" or proceed == "necklace":
                    if proceed in pieces:
                        print("Try again! You already have this.")
                        proceed = input("What do you want?")
                        proceed = proceed.lower()

                    elif proceed == "earrings":
                        print("You chose the earrings!")
                        pieces.append("earrings")
                        break

                    elif proceed == "ring":
                        print("You chose the ring!")
                        pieces.append("ring")
                        break

                    elif proceed == "crown":
                        print("You chose the crown!")
                        pieces.append("crown")
                        break

                    elif proceed == "bracelet":
                        print("You chose the bracelet!")
                        pieces.append("bracelet")
                        break

                    elif proceed == "necklace":
                        print("You chose the necklace!")
                        pieces.append("necklace")
                        break

        #loop for run of the game without having to reset turn
        else:
            turnTotal = turnTotal % 12

            turnTotal = turnTotal % 12

            if turnTotal == 1:
                if "white ring" not in pieces:
                    print("Uh oh! You got the white ring! Careful!")
                    pieces.append("white ring")

                else:
                    print("You have this piece already.")
            
            elif turnTotal == 2:
                if "earrings" not in pieces:
                    print("You got the earrings!")
                    pieces.append("earrings")

                else:
                    print("You have this piece already.")

            elif turnTotal == 3:
                proceed = input("You can choose: an earring, ring, crown, bracelet, or necklace! What do you want?")
                proceed = proceed.lower()

                while proceed != "earrings" and proceed != "ring" and proceed != "crown" and proceed != "bracelet" and proceed != "necklace":
                    print("Please enter a valid object such as earrings, ring, crown, bracelet, or necklace.")
                    proceed = input("What do you want?")
                    proceed = proceed.lower()
                    
                while proceed == "earrings" or proceed == "ring" or proceed == "crown" or proceed == "bracelet" or proceed == "necklace":
                    if proceed in pieces:
                        print("Try again! You already have this.")
                        proceed = input("What do you want?")
                        proceed = proceed.lower()

                    elif proceed == "earrings":
                        print("You chose the earrings!")
                        pieces.append("earrings")
                        break

                    elif proceed == "ring":
                        print("You chose the ring!")
                        pieces.append("ring")
                        break

                    elif proceed == "crown":
                        print("You chose the crown!")
                        pieces.append("crown")
                        break

                    elif proceed == "bracelet":
                        print("You chose the bracelet!")
                        pieces.append("bracelet")
                        break

                    elif proceed == "necklace":
                        print("You chose the necklace!")
                        pieces.append("necklace")
                        break

            elif turnTotal == 4:
                if "ring" not in pieces:
                    print("You got a ring!")
                    pieces.append("ring")

                else:
                    print("You have this piece already.")

            elif turnTotal == 5:
                if "bracelet" not in pieces:
                    print("You got a bracelet!")
                    pieces.append("bracelet")

                else:
                    print("You have this piece already.")

            elif turnTotal == 6:
                proceed = input("Uh oh! Put an item back! What do you want to give up?")
                proceed = proceed.lower()

                if not proceed:
                    print("No pieces left.")
            
                while proceed != "earrings" and proceed != "ring" and proceed != "crown" and proceed != "bracelet" and proceed != "necklace":
                    print("Please enter a valid object such as earrings, ring, crown, bracelet, or necklace.")
                    proceed = input("Uh oh! Put an item back! What do you want to give up?")
                    proceed = proceed.upper()

                while proceed == "earrings" or proceed == "ring" or proceed == "crown" or proceed == "bracelet" or proceed == "necklace":
                    if proceed not in pieces:
                        print("Try again! You don't have this piece.")
                        proceed = input("What do you want?")
                        proceed = proceed.lower()

                    elif proceed == "earrings":
                        print("You chose the earrings!")
                        pieces.remove("earrings")
                        break

                    elif proceed == "ring":
                        print("You chose the ring!")
                        pieces.remove("ring")
                        break

                    elif proceed == "crown":
                        print("You chose the crown!")
                        pieces.remove("crown")
                        break

                    elif proceed == "bracelet":
                        print("You chose the bracelet!")
                        pieces.remove("bracelet")
                        break

                    elif proceed == "necklace":
                        print("You chose the necklace!")
                        pieces.remove("necklace")
                        break
                        
            elif turnTotal == 7:
                if "necklace" not in pieces:
                    print("You got a necklace!")
                    pieces.append("necklace")

                else:
                    print("You have this piece already.")

            elif turnTotal == 8:
                if "crown" not in pieces:
                    print("You got a crown!")
                    pieces.append("crown")

                else:
                    print("You have this piece already.")

            elif turnTotal == 9:
                if "white ring" not in pieces:
                    print("Uh oh! You got the white ring! Careful!")
                    pieces.append("white ring")

            elif turnTotal == 10:
                proceed = input("Uh oh! Put an item back! What do you want to give up?")
                proceed = proceed.lower()

                if not proceed:
                    print("No pieces left.")
            
                while proceed != "earrings" and proceed != "ring" and proceed != "crown" and proceed != "bracelet" and proceed != "necklace":
                    print("Please enter a valid object such as earrings, ring, crown, bracelet, or necklace.")
                    proceed = input("Uh oh! Put an item back! What do you want to give up?")
                    proceed = proceed.upper()

                while proceed == "earrings" or proceed == "ring" or proceed == "crown" or proceed == "bracelet" or proceed == "necklace":
                    if proceed not in pieces:
                        print("Try again! You don't have this piece.")
                        proceed = input("What do you want?")
                        proceed = proceed.lower()

                    elif proceed == "earrings":
                        print("You chose the earrings!")
                        pieces.remove("earrings")
                        break

                    elif proceed == "ring":
                        print("You chose the ring!")
                        pieces.remove("ring")
                        break

                    elif proceed == "crown":
                        print("You chose the crown!")
                        pieces.remove("crown")
                        break

                    elif proceed == "bracelet":
                        print("You chose the bracelet!")
                        pieces.remove("bracelet")
                        break

                    elif proceed == "necklace":
                        print("You chose the necklace!")
                        pieces.remove("necklace")
                        break

            elif turnTotal == 11:
                if "necklace" not in pieces:
                    print("You got a necklace")
                    pieces.append("necklace")

                else:
                    print("You have this piece already.")

            elif turnTotal == 12:
                proceed = input("You can choose: an earring, ring, crown, bracelet, or necklace! What do you want?")
                proceed = proceed.lower()

                while proceed != "earrings" and proceed != "ring" and proceed != "crown" and proceed != "bracelet" and proceed != "necklace":
                    print("Please enter a valid object such as earrings, ring, crown, bracelet, or necklace.")
                    proceed = input("What do you want?")
                    proceed = proceed.lower()
                    
                while proceed == "earrings" or proceed == "ring" or proceed == "crown" or proceed == "bracelet" or proceed == "necklace":
                    if proceed in pieces:
                        print("Try again! You already have this.")
                        proceed = input("What do you want?")
                        proceed = proceed.lower()

                    elif proceed == "earrings":
                        print("You chose the earrings!")
                        pieces.append("earrings")
                        break

                    elif proceed == "ring":
                        print("You chose the ring!")
                        pieces.append("ring")
                        break

                    elif proceed == "crown":
                        print("You chose the crown!")
                        pieces.append("crown")
                        break

                    elif proceed == "bracelet":
                        print("You chose the bracelet!")
                        pieces.append("bracelet")
                        break

                    elif proceed == "necklace":
                        print("You chose the necklace!")
                        pieces.append("necklace")
                        break
                        

        if ("earrings" in pieces and "crown" in pieces and "ring" in pieces and "bracelet"in pieces and "necklace" in pieces) or ("earrings" in pieces and "crown" in pieces and "ring" in pieces and "bracelet" in pieces and "necklace" in pieces and "white" in pieces):
            break

    return pieces


def main():
    #runs the game without game board
    player = random.randint(0, 1)
    computer = 1 - player

    print("You are player %d" %(player + 1))
    
    scores = ["", ""]
    value = 0

    #Controls the system runs of the player's games
    while True:
        
        print("Player 1 score: ", scores[0])
        print("Player 2 score: ", scores[1])
        print("It is player %d's turn" %((value % 2) + 1))

        if value == player :
            print("Your turn!")
            pieces = rules()
            finalPieces = set(pieces)

            print()
            print("You got all the pieces:", *finalPieces)

            if "white ring" in finalPieces:
                print()
                print("You lost because you hold the white ring! Too bad!")
                print()
                value += 1
        
            else:
                print()
                print("Winner!")
                break

        else:
            print("Computer's turn!")
            pieces = computer_rules()
            finalPieces = set(pieces)
            
            print()
            print("You got all the pieces:", *finalPieces)

            if "white ring" in finalPieces:
                print()
                print("You lost because you hold the white ring! Too bad!")
                print()
                value += 1

            else:
                print()
                print("Computer has won!")
                break

    #runs the game with board interaction
    (wn, board_img) = game_board()
    count = 0

    while True:
        spin()
       
        if spin() == "We have a winner!":
            return False


if __name__ == "__main__":
    main()
        
