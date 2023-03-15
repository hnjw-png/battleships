
# Welcome to Battleships! 
Here you will experience a simple game of battleships, using python, and stored in a run.py. 
The game will consist of a a greeting and then ask for the name of player. There after there will be a board, with 5 rows and 5 columns.
The general rules of battleships apply, hit all your opponents ships, before they hit yours.
This game will generate a random guess from the computer. 
The game will restart when there is a winner. You can continue, another game thereafter.
>>>>>>> 8c3a9cfeebb59b6182a6e515754601c38303573a

## Hello Prompt

* To begin the game of battleships, there is will be  message asking you write you name, then the next message will appear saying welcome to battleships + X.

## The Board

* 5 rows, 5 colums, no way of clicking out of the board.
* Here I have created a simplifed version of battleships, the grd is made up of 5 rows and columns. These are made up with 0's.
* Do not edit any of the other files or your code may not deploy properly

## The Boats

* There will be two boats in the game, there is a function that picks coordinates randomly, they two more functions representing where the boats will be places at random. 

## The guess row and column prompt

* After each go, there will be a automatic prompt to ask for your guess, you will have 5 chances to guess correctly.

## The function that stops you from selecting coordinates outside of the board game.

* You will be prompted that you have clicked outside the board and asked to make another guess.
* You will be informed if you guess correctly.

## You didnt sink the ships

* You have 5 chances to choose correctly, before the game restarts.

# Improvements.

* This game was a great learning curve for me, as I have spend much time expereimenting with different ways of creating the game, ship placement and score collecting. In the end I decided on a simplier version of battleships, which better served its purpose. 

* I would have have numbered and lettered coordinates for my board like this: 

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!
