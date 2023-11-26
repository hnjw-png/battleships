import random
from random import randint

# hello message to player
print("Welcome to Battleships, this is a one player game. You have 5 turns, and guesses must be between 0-5")
print("Enter your name:")
x = input()
print("Hello, lets play Battleships " + x)


class Board:
    def __init__(self, board):
     self.board = board


    def print_board(self):
      for row in board:
         print(" ".join(row))


    def print_board(self):
      row_number = 1
      for row in self.board:
          print("%d| %d|" % (row_number, "|" .join(row)))
          row_number += 1


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
            
            
    def get_user_input(self):
      try:
        x_row = input("Type in the Ship row number:")
        while x_row not in '12345':
            print("not in the right place, seems you hae sailed away.")
            x_row = input("Type in row of ship again:")


        y_column = input("Type in the Ship column number:")
        while y_column not in '12345':
            print("not in the right place, seems you hae sailed away.")
            y_column = input("Type in column of ship again:")
        return int(x_row) -1,(y_column)
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
    computer_board = Board([[""] * 5 for i in range(6)])
    user_guess_board = Board([[""] * 5 for i in range(6)])
    Ship.make_ships(computer_board)
    turns = 8
    while turns > 0:
        Board.print_board(user_guess_board)
        user_x_row, user_y_column = Ship.get_user_input(object)
        while user_guess_board.board[user_x_row][user_y_column] == "-" or user_guess_board:
         board[user_x_row][user_x_row] == "p"
         print("You have already chose this spot, please pick another")
         user_x_row, user_y_column == Ship.get_user_input(object)
        if computer_board.board[user_x_row][user_y_column] == "p" :
            print("You managed to find one of my ships, what a hit!")
            user_guess_board.board[user_x_row][user_y_column] = "p"
        else:
            print("You did not find my ship!")
            user_guess_board.board[user_x_row][user_y_column] = "-"
        if Ship.count_found_ships(user_guess_board) == "5" :
           print("Well done you managed to find all the ships!")
           break
        else:
            turns -= 1
            print(f"You got this many guesss {turns} left, Good Luck!")
            if turns == 0:
                print("Oh looks like you sunk all you can today, you are out of turns")
                Board.print_board(user_guess_board)
                break

if __name__ == '__main__':
    RunGame()




