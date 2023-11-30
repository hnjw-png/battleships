import random
from random import randint

# hello message to player
print("Welcome to Battleships, this is a one player game. You have 8 turns, and guesses must be between 1-8 and A nnd G")
print("Enter your name:")
x = input()
print("Hello, lets play Battleships " + x)

#create the board class for object orientation
class Board:
    def __init__(self, board):
     self.board = board


#create the battleship board.

    def print_board(self):
        print("  " + " ".join(["A", "B", "C", "D", "E", "F", "G", "H"]))
        row_number = 1
        for row in self.board:
            print(f"{row_number} {'| '.join(row)}")
            row_number += 1


#make the ships

class Ship:
    def __init__(self, board):
        self.board = board

    def make_ships(self):
        for i in range(5):
            self.x_row, self.y_column = random.randint(0,7), random.randint(0,7)
            while self.board[self.x_row][self.y_column] == 'p':
              self.x_row, self.y_column = random.randint(0,7), random.randint(0,7)
            self.board[self.x_row][self.y_column] == 'p'
        return self.board
            
       #ask for the users input, and react if not correct     
    def get_user_input(self):
      try:
        x_row = input("Type in the Ship row number:")
        while x_row not in '1234567':
            print("not in the right place.")
            x_row = input("Type in row of ship again:")

        y_column = input("Type in the Ship column letter:")
        while y_column not in 'ABCDEFG':
            print("not in the right place.")
            y_column = input("Type in column of ship again:")
        return int(x_row) -1, (y_column)
      except ValueError and KeyError:
        print("not valid")
        return self.get_user_input()


# randomly find ship coordinates
def count_found_ships(self):
    found_ships = 0
    for row in self.board:
        for column in row == 'p':
            found_ships += 1
    return found_ships


def RunGame():
    computer_board = Board([[""] * 8 for i in range(8)])
    user_guess_board = Board([[""] * 8 for i in range(8)])
    Ship.make_ships(computer_board)
    #begins 8 go's
    turns = 8
    while turns > 0:
        Board.print_board(user_guess_board)
        #what did the user choose?
        user_x_row, user_y_column = Ship.get_user_input(object)
        #stop the player picking the same place twice
        #while user_guess_board.board[user_x_row][user_y_column] == "-" or user_guess_board.board[user_x_row][user_y_column] == "p" :
         # print("You have already chose this spot, please pick another")
        user_x_row, user_y_column == Ship.get_user_input(object)
          #is it a hit or miss?
        if computer_board.board[user_x_row][user_y_column] == "p" :
          print("You managed to find one of my ships, what a hit!")
          #player missed the ship
          user_guess_board.board[user_x_row][user_y_column] = "p"
        else:
          print("You did not find my ship!")
          user_guess_board.board[user_x_row][user_y_column] = "1"
        if Ship.count_found_ships(user_guess_board) == "5" :
          print("Well done you managed to find all the ships!")
          break
        else:
          turns -= 1
          #how many turns left?
          print(f"You got this many guesss {turns} left, Good Luck! " )
          if turns == 0:
            print("Oh looks like you sunk all you can today, you are out of turns")
            Board.print_board(user_guess_board)
            break

if __name__ == '__main__':
    RunGame()




