from random import randint
player = 0
computer = 0

#hello message to player
print("Enter your name:")
x = input()
print("Hello, lets play Battleships!" + x)

#setting board rows and columns
class Board:
   def __init__(self, size, num_ships):
    self.size = size
    self.board = board
    self.num_ships = num_ships

def board in range:
    for row in range(5):
    for col in range(5):
            #or for x in range(5)??
    board.append(["_"] * 5)

    
#assign letters and numbers to board
    def print_board(Board):
         for row in range(5):
         for col in range(5):
        print(" ", " ".join("12345"))
        for letter, row in zip("ABCDE", Board):
            print(letter, " ".join(row))
   

#setting the random placement of ships

    def random_row(self, num_ships):
    return randint(0, len(Board) - 1 )

    def random_col(self, num_ships):
    return randint(0, len(Board[0]) - 1 )

ship_row = rand_row(Board)
ship_col = random_col(Board)

print(ship_row)
print(ship_col)

def game():
    print_board(Board)

#asking the player to guess a spot
print("Type you guess, between 1-5")
x = input()
print("You typed:" + x)

print("Guess a letter")
x =  input()
print("You typed: " + x)
   
print(Board)

#seeing if you sunk the oppenants battleship
#control that the player cannot chose outside of the board
#print x for a guess
if ship_row == guess_row and ship_col == guess_col:
    print("Well done! You sunk my Battleship!")
else:
    if guess_row not in range(5) or guess_col not in range(5):
    print("You missed the board!")
    elif Board[guess_row][guess_col] == "X"
    print_board(Board)

#restart game upon first ship being sunk
if ship_row == guess_row and ship_col == guess_col:
    start()


#add more ships to the board
