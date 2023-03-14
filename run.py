

















from random import randint
#hello message to player
print("Enter your name:")
x = input()
print("Hello, lets play Battleships!" + x)

#setting board rows and columns
class board:
   def __init__(self, size, num_ships):
    self.size = size
    self.board = board
    self.shipone_col = shipone_col
    self.shiptwo_col = shiptwo_col
    self.shipone_row = shipone_row
    self.shiptwo_row = shiptwo_row
    self.shipone_won = shipone_won
    self.shiptwo_won = shiptwo_won


board(size) = []  

for o in range(5):
    board.append(["0"] * 5 )

def board(board):
    for row in board:
        print(" ".join(row))

def print_board(board):
        print(" ", " ".join("12345"))
        for letter, row in zip("ABCDE", Board):
            print(letter, " ".join(row))

print_board(board)


#randomly find ship coordinates
def random_row(board):
    return randrange(0, len(board))

def random_row(board):
    return randrange(0, len(board))


#random coordinates to ship one

shipone_col = random_row(board)
shipone_col = random_col(board)

#randow coordinates for ship two

for i in range(6):
    shiptwo_row = random_row(board)
    shiptwo_col = randow_col(board)


shipone_won = False
shiptwo_won = False

for turn in range(6):

#receive the players guess

    print ("Round #" + str (turn + 1))
    guess_row = int(input("Guess Row:"))
    guess_col = int(input("Guess Col:"))

#this will check if the is users guesses match ships

    if (guess_row == shipone_row and guess_col == shipone_col and shipone_won == False):
        print("You have taken one ship, one  to go!")
        shipone_won = True

    #set the space to x, so we know where the last boat was hit

        board[guess_col][guess_row] = "x"

        if shipone_won and shiptwo_won == True:
            print("Congratulations, you have taken down both ships")
            break


    elif(guess_row == shiptwo_row and guess_col == shiptwo_col and shiptwo_won == False):
        print("Congrats! You have taken down one ship")
        board[guess_row][guess_col] = "x"
        if shiptwo_won == True and shiptwo_won == True:
            print("Congrats, You have taken down both ships!")


    else:
        if turn == 5:
            print "You did not sink all the battleships, GAME OVER!"

        elif([guess_row][guess_col] == "x")
            print "Oops, you hit the same place!"





