
# Welcome to Battleships! 

## Instructions and information: 

Here you will experience a simple game of battleships, using python, and stored in a run.py. 
The game will consist of a instructions and then ask for the name of player. There after there will be a board, with 7 rows and 7 columns.
The general rules of battleships apply, is to hit both battleships within 12 turns.
There wil be five ships to find, and eight turns to find them. The game will keep track on how many ships have been found.
Its a challenging game 

## Responsiveness


## Instructions and Hello prompt

* Firstly basic instructions will appear on how you should play the game.

* Thereafter there will be a message asking for the players name, and the next message that will appear with be welcome to battleships + the name.

* Then the board appears.

## The Board

* 7 rows, 7 columns, no way of clicking out of the board.

* Here I have created a board using object orinenatated programming, using the def_init_(self) method. 

* The board itself will reapppear updated with previous guesses for each turn.

* I have hidden the ships in the computers board so to speak, and the user has to find them on their board.

* Here I have made rows and columns with numbering inline to 7. Inside the board is made up by these '|' to make up a visual board.



## The Ships

* There will be 5 boats in the game, there is a function that picks coordinates randomly, I used the random.randint method to randomly place in the ships inside the board.

* You will be able to see where you have chosen, if you don't find the ship a '-' will appear where you have guessed. If you have guessed correctly a 'p' will appear in that place.

* You will not be able to guess the same place twice, or guess somewhere that is outside of the radius of the board (1-7)

* The game will automatically end after 8 turns, you will receive a message stating your ending game statement.

* I created the def make_ships(self) function, to create the ships in the game, using i in range statement and random.randint to place 5 ships in random places in the board. Following this down in the rungame() function, I call the make_ships function, within a computer board, the user can only see their user board.

* I created a function that counts how many ships. Again I have utlised the self method, def_count_found_ships(self), the amount of found ships starts naturally on 0. I have then called this function in my rungame() function, it keeps track of all 5 ships have been found or not. 


## The guess row and column prompt

* After each turn, there will be a automatic prompt to ask for your guess, you will have 8 chances to find all the ships. 

* If you guess a letter or another key, you will get a prompt to guess again, due to your entry being invalid.

* The user will always receive printed prompts stating whats going on, for example: (f"You got this many guesss {turns} left, Good Luck! " ) or ("Well done you managed to find all the ships!").


## The function that stops you from selecting coordinates outside of the board game.

* You will be prompted that you have not chosen a place on the board and asked to make another guess.

* I am using the while, not in range method. This reads if the user types in a number which is outside of the board.

## You didnt sink the ships

* You have 12 chances to choose correctly, before the game ends.

* The while method is used in my rungame function, to keep track of how turns the user has taken. The users turns will not exceed 12.

* If the user finds all the ships before the turns end the game will end and you get a prompt that the user has found all ships.



## Automatic error is a letter is typed of instead of a number

* You will get a error message if you choose anything other than a number. This is using the except ValueError method.

## Hit, miss.

* In the Rungame function, I use 'if' statements to check if the user has hit or missed the ships.

* Here I call the count_ships function, to as its sounds count how many ships have been found. If they have, you will get a prompt that you have found all ships. Otherwise, I use the 'else' method to calculate how turns are left. 

* You continue the game until your turns run out or win.

## No guessing the same place twice

# Improvements



## Testing

* Currently the board appears without problem in the console, the prompts work properly as well. 

* The next debug I am doing is to see why you do not see when you have hit and miss. 

* I am creating a piece of code to restart game, right now it looks like this:


while True:
        game()
        restart = input('Do you want to restart Yes please/No thanks?')
        if restart == 'N'
            break
        elif restart == 'Y':
            continue
  
  
## Python Validator


## Deployment

* Step one: Go to Heroku and log in.

* Create a new app directly in Heroku, give it a unique name.

* Attach you github repository to your heroku account.

* Go to the tab, deplpy.

* Then choose method, this time its github.

* Then give access to your github repository to heroku.

* Press deploy branch manually.

* It can also work to select deploy branch automatically, this will update everytime you commit you editted repository to github.

## Credits

* w3schools for help understanding game creation.

* code institute for study material

