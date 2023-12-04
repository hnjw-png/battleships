import random
from random import randint

# hello message to player
print("Welcome to Battleships, this is a one player game. You have 20 turns, and guesses must be between 1-7")
print("Enter your name:")
x = input()
print("Hello, lets play Battleships " + x)

# create the board class for object orientation
class Board:
    def __init__(self, board):
     self.board = board


# create the battleship board, numbering columns and rows

    def print_board(self):
        print("  " + " ".join(["1", "2", "3", "4", "5", "6", "7"]))
        row_number = 1
        for row in self.board:
            print(f"{row_number} {'| '.join(row)}")
            row_number += 1


# make the ships and create 5 random ship coorindates 

class Ship:
    def __init__(self, board):
        self.board = board

    def make_ships(self):
        for i in range(5):
            self.x_row, self.y_column = random.randint(0,6), random.randint(0,6)
            while self.board[self.x_row][self.y_column] == 'p':
              self.x_row, self.y_column = random.randint(0,6), random.randint(0,6)
            self.board[self.x_row][self.y_column] = 'p'
        return self.board
            
# ask for the users input, and react if not within the board 
    @staticmethod
    def get_user_input():
      try:
          x_row = int(input("Type in the Ship row number:")) - 1
          while x_row not in range(0, 7):  
              print("Not in the right place.")
              x_row = int(input("Type in row of ship again:")) - 1

          y_column = int(input("Type in the Ship column NUMBER:")) - 1
          while y_column not in range(0, 7):  
              print("Not in the right place.")
              y_column = int(input("Type in column of ship again:")) - 1

          return x_row, y_column
      except ValueError:
          print("Invalid input. Please enter a valid row and column.")
          return Ship.get_user_input()



# count how many ships the user has found
    def count_found_ships(self):
      found_ships = 0
      for row in self.board:
          for column in row:
              if column == 'p':
                  found_ships += 1
      return found_ships


def RunGame():
    computer_board = Board([[""] * 8 for i in range(7)])
    user_guess_board = Board([[""] * 8 for i in range(7)])
    Ship.make_ships(computer_board)
    # begins 20 go's
    turns = 20
    while turns > 0:
        Board.print_board(user_guess_board)
        # what did the user choose?
        user_x_row, user_y_column = Ship.get_user_input()
        # stop the player picking the same place twice
        while user_guess_board.board[user_x_row][user_y_column] == "-" or user_guess_board.board[user_x_row][user_y_column] == "p":
          print("You have already chosen this spot, please pick another")
          user_x_row, user_y_column = Ship.get_user_input()
          # is it a hit or miss?
        if computer_board.board[user_x_row][user_y_column] == "p" :
          print("You managed to find one of my ships, what a hit!")
          # player missed the ship
          user_guess_board.board[user_x_row][user_y_column] = "p"
        else:
          print("You did not find my ship!")
          user_guess_board.board[user_x_row][user_y_column] = "-"
          # are all ships found?
        if Ship.count_found_ships(user_guess_board) == "5" :
          print("Well done you managed to find all the ships!")
          break
        else:
          turns -= 1
          # how many turns left?
          print(f"You got {turns} guesses left, Good Luck! " )
          if turns == 0:
            print("Oh looks like you sunk all you can today, you are out of turns")
            Board.print_board(user_guess_board)
            break
            

if __name__ == '__main__':
    RunGame()




