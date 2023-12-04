
# Welcome to Battleships for 1 player! 

## Instructions and information: 

Here you will play a simple logical game of battleships, using python, and stored in a run.py. 
The game will consist of a instructions and then ask for the name of player. There after there will be a board, with 7 rows and 7 columns. Thereafter the player will be asked to choose a row number and a column number.
The general rules of battleships apply, is to hit all battleships within 12 turns, to win the game.
There wil be 5 ships to find, and 12 turns to find them. The game will keep track on how many ships have been found. The game will automatically end if the player does not find all ships within 12 turns. Again there will be prompts throughout the game to keep the player on track.
Its a challenging game for one player, a game of guessing and chance. 

## User Goals and stories

* The user should be able to play a one player game, the user should be able to keep track of their own guesses and amount of turns. The game will continously give prompts after turns to tell the user how they are doing and what to do.

* The board will appear again after each guess, it wil be updated with the users guesses. The board will be reappearing each time updated with all user guess each time, improves the user experience.

* The user should be able to see if they hit or miss a ship.

* The user cannot enter a value higher than 7, and cannot answer with a letter.


## Responsiveness


# Features and Data Models explained:

## Instructions and Hello prompt

* Firstly basic instructions will appear on how you should play the game.

* Thereafter there will be a message asking for the players name, and the next message that will appear with be welcome to battleships + the name.

* Then the board appears.

## The Board

* 7 rows, 7 columns, no way of clicking out of the board.

* Here I have created a board using object orinenatated programming, using the def_init_(self) method. This creates a object, then I create a computer board

* The board itself will reapppear updated with previous guesses for each turn. I do this by call

* I have hidden the ships in the computers board so to speak, and the user has to find them on their board.

* Here I have made rows and columns with numbering inline to 7. Inside the board is made up by these '|' to make up a visual board.



## The Ships

* There will be 5 boats in the game, there is a function that picks coordinates randomly, I used the random.randint method to get the computer to randomly place in the ships inside the board.

* You will be able to see where you have chosen, if you don't find the ship a '-' will appear where you have guessed. If you have guessed correctly a 'p' will appear in that place.

* You will not be able to guess the same place twice, or guess somewhere that is outside of the radius of the board (1-7)

* The game will automatically end after 8 turns, you will receive a message stating your ending game statement.

* I created the def make_ships(self) function, to create the ships in the game, using i in range statement and random.randint to place 5 ships in random places in the board. Following this down in the rungame() function, I call the make_ships function, within a computer board, the user can only see their user board.

* I created a function that counts how many ships have been found. Again I have utlised the self method, def_count_found_ships(self), the amount of found ships starts naturally on 0. I have then called this function in my rungame() function, it keeps track of all 5 ships have been found or not. 


## The guess row and column prompt

* After each turn, there will be a automatic prompt to ask for your guess, you will have 8 chances to find all the ships. 

* The user always will be asked by the prompt, to guess a row and then to guess a column.

* If you guess a letter or another key, you will get a prompt to guess again, due to your entry being invalid.

* The user will always receive printed prompts stating whats going on, for example: (f"You got this many guesss {turns} left, Good Luck! " ) or ("Well done you managed to find all the ships!").


## The function that stops you from selecting coordinates outside of the board game.

* I used a function called def get_user_input(self), and the the try, while in range method to read the users guesses and read if they are guessing a number inside the board.You will be prompted that you have not chosen a place on the board and asked to make another guess. 


## How many turns, and calculating amount of turns.

* You have 12 chances to choose correctly, before the game ends.

* The while method is used in my rungame function, to keep track of how turns the user has taken. The users turns will not exceed 12.

* A prompt keeps the user informed of how many turns they have remaining.

* If the user finds all the ships before the turns end the game will end, and you get a prompt that the user has found all ships.


## Automatic error is a letter is typed of instead of a number

* You will get a error message if you choose anything other than a number. This is using the except ValueError method.

## Hit, miss.

* In the Rungame function, I use 'if' statements to check if the user has hit or missed the ships.

* If the user has hit a ship, the user will see a prompt, stating they have a hit a ship. 

* If the user missed the ships, the user will see a prompt stating they have missed the ships.

* I call the count_ships function in rungame function, to, as its sounds, count how many ships have been found. If they have all been found, you will get a prompt that you have found all ships. Otherwise, I use the 'else' method to calculate how many turns are left. 

* You continue the game until your turns run out or win. The user will get a prompt is they find all ships and the game will end. Or they will get a prompt stating they didn't find the ships, when turns end.

## No guessing the same place twice

* In the rungame function, it will read if you have already guessed a place or not. It reads if the cooridinates are already in use or not, by reading if "-" or "p" are already there, due to a previous guess.

# Improvements

* A improvement could be to make it a two player game.

* Another improvement could be to add letters to the top row to make the game more user friendly.

## Solved Bugs & Testing

* Currently the board appears without problem in the console, the prompts work properly as well. It took a few tried to get the numbers to appear correctly on the board. But it is now fixed, though one improvement could be that the board doe not move to the right, when a p or -is added.

* I am having a error with reading the valueerror, if the user enters a letter the game throughs a error instead of a prompt that it was invalid and continuing. 

* I have manually tested the game to see if each function works : 
1. I have tested, if the user cannot guess the same guess twice, and that works and the user is prompted that they have guessed the same place twice, and then gets another turn.
2. I have tested if the user can guess outside the board or not, it works and the user is prompted to make another valid guess...if they guess a number which is not with 1-7.
3. I have tested if the ships appear on the board with 'p' when found and they do. As well as after each guess the board appears again with all guesses updated each time.
4. I have also tested if the - appears when there is a wrong guess and it does.
5. I have checked if the user can keep track of how many turns remaining and they can. They see a prompt stating how many guesses remaining.
6. I have looked to see if the game ends automatically after turns have been exceeded, and it does.
7. I have tried to find all ships to check to see if the game behaves correctly if the user finds all ships. And after many attempts of playing the game, I found them all and it worked correctly.
8. Lastly I am testing if the game can read a Value error, intially it was throwing a error, due to not get_user_input not being defined.. I have fixed this and now a user cannot type anything invalid such as A,D,F.

## Unsolved bugs & tests

* none
  
## Python Validator

* Currently only indentation errors in the validator, I will fix this before submission.

## Deployment

* Step one: Go to Heroku and log in.

* Create a new app directly in Heroku, give it a unique name.

* Attach you github repository to your heroku account.

* Go to the tab, deploy.

* Then choose method, this time its github.

* Then give access to your github repository to heroku.

* Press deploy branch manually.

* It can also work to select deploy branch automatically, this will update everytime you commit you editted repository to github.

## Credits

* w3schools for help understanding game creation.

* code institute for study material

