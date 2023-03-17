from random import randint

# hello message to player
print("Enter your name:")
x = input()
print("Hello, lets play Battleships " + x)


board = []

for x in range(5):
    board.append(["0"] * 5)


def print_board(board):
    for row in board:
        print(" ".join(row))


print_board(board)


# randomly find ship coordinates
def random_row(board):
    return randint(0, len(board))

    
def random_col(board):
    return randint(0, len(board))


# random coordinates to ship one

shipone_row = random_row(board)
shipone_col = random_col(board)

# randow coordinates for ship two

for i in range(6):
    shiptwo_row = random_row(board)
    shiptwo_col = random_col(board)
    if shiptwo_row != shipone_row and shiptwo_col != shipone_col:
        break


shipone_won = False
shiptwo_won = False

for turn in range(6):

# receive the players guess

    print("Round #" + str(turn + 1))
    guess_row = int(input("Guess Row:"))
    guess_col = int(input("Guess Col:"))

# this will check if the is users guesses match ships

    if (guess_row == shipone_row and guess_col == shipone_col and shipone_won == False):
        print("You have taken one ship, one to go!")
        shipone_won = True

    # set the space to p, so we know where the last boat was hit

        board[guess_col][guess_row] = "p"

        if shipone_won and shiptwo_won is True:
            print("Congratulations, you have taken down both ships")
            break


        elif(guess_row == shiptwo_row and guess_col == shiptwo_col and shiptwo_won == False):
            print("Congrats! You have taken down one ship")
        board[guess_row][guess_col] = "p"
        if shiptwo_won == True and shiptwo_won == True:
            print("Congrats, You have taken down both ships!")
            break


    else:
        if turn == 5:
            print("You did not sink all the battleships, GAME OVER!")
            break

    elif:
        (guess_col < 0 or guess_col > 5) or (guess_row < 0 or guess_row > 5):
        print("Oh no! You did not choose a valid number!")
        break
