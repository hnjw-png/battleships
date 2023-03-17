
# Welcome to Battleships! 

## Instructionsand information: 

Here you will experience a simple game of battleships, using python, and stored in a run.py. 
The game will consist of a a greeting and then ask for the name of player. There after there will be a board, with 5 rows and 5 columns.
The general rules of battleships apply, is to hit both battleships within 5 turns.
This game will generate a random guess from the computer. This function is not yet in the game, in future I will add the computers random choice too.
The game will restart when there is a winner. You can continue, another game thereafter. This function is not working, this is something to work out in the future. As the reason is that the function has not been written.
>>>>>>> 8c3a9cfeebb59b6182a6e515754601c38303573a

## Instructions and Hello prompt

* Firstly basic instructions will appear on how you should play the game.

* Thereafter there will be a message asking for the players name, and the next message that will appear with be welcome to battleships + the name.

* Then the board appear.

## The Board

* 5 rows, 5 colums, no way of clicking out of the board.
* 
* Here I have created a simplifed version of battleships, the grd is made up of 5 rows and columns. These are made up with 0's.
* 
* There is one board for one player, that only appears once.

## The Boats

* There will be two boats in the game, there is a function that picks coordinates randomly, they two more functions representing where the boats will be places at random. 

* Right now you cannot ot see what coordinates you have choose on the board, in future there will be more functionality on the board. As its highly important in the game that you know your hits and misses.

## The guess row and column prompt

* After each go, there will be a automatic prompt to ask for your guess, you will have 5 chances to guess correctly.

## The function that stops you from selecting coordinates outside of the board game.

* You will be prompted that you have clicked outside the board and asked to make another guess.
* 
* You will be informed if you guess correctly.
* 
* There are 2 ships to be found.

## You didnt sink the ships

* You have 5 chances to choose correctly, before the game restarts.

* Right now the user has to manually reset the game.

# Improvements.

* This game was a great learning curve for me, as I have spend much time experimenting with different ways of creating the game, ship placement and score collecting. In the end I decided on a simplier version of battleships, which better served my purpose. 

* I would have have numbered and lettered coordinates for my board something like this: 
 assign letters and numbers to board
    def print_board(Board):
        print(" ", " ".join("12345"))
        for letter, row in zip("ABCDE", Board):
            print(letter, " ".join(row))

* I would have more ships, which could look something like this, right now I have written the code in a simplier way to create two ships. But below you will see the sort of code I could use to add many, and to keep the code much more functional and practical: 
class Ship: 
    def__init__(self, col, row):
    self.col = col
    self.row = row
    
    num_of_ships = 4
    ships = []
    for i in range (num_of_ships)
    ships.append(ship)
    
  * I would have a more appealing visuals, this could work by chnaging colors when you hit or miss.
  * Another improvement would be to make sure the boards appears appended with each guess after each round. This is a in progress of being researched, and a example code will come:...
  

* use classes instead of only def, this would make the code more functional and object orientated.


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
  
 * Right now, I had to remove the function that stops you from clicking outside the board as it was causing a error, my idea for improving the project is the following code:


![image](https://user-images.githubusercontent.com/120515252/225852315-c3190bfa-6b60-4194-bb73-0db62f09caff.png)

The fact that the game doesnt tell you if you have clicked outside the board, although theres no error, its not clear if you pickign a coordinate or not, so a improvement would be to make the game more playable and understandable.

* A second error that has occured is that you are not told per guess if you have hit or miss, the code only runs 5times and then tells you if you won or not.

![image](https://user-images.githubusercontent.com/120515252/225856381-bd7d4f95-01a0-481c-b057-de07e82d933b.png)


* In a way to improve more, I would create a opposing player(the computer) and a two boards to show where you have hit, because right now its a one player game.

* Another improvement would be to create a scoring system. This be could be by appending the score every time the player loses or wins.

* Right now the game does not restart without being maually refreshed this is something I would look to improve further in this game, as in terms of usability its not ideal for the use to press the refrest button themselves.

* The game itself serves its purpoae, but does not have a higher gain, nothing that is going to make you stay. I would like to make it more interactive, by shwing the board everytime the user picks a coordinate. And work on the function that shows where you have already guessed.
* 
## Python Validator

* Unfortunately my code did not pass the validator test, there was some small errors such as too many blank lines. In the future, I edit the code to have no errors and to be honest, be a little more complicated. As someone who has picked up python for the first time, it had its own set of challenges, adn required a lot of additional homework, to understand how to actually create a game.
* 
![image](https://user-images.githubusercontent.com/120515252/225858387-f2bbc016-84a8-48cf-bc7a-a2594c48463b.png)


## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!
