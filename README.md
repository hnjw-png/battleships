![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

<<<<<<< HEAD
Welcome Holly Williams,
=======
# Welcome to Battleships! 
Here you will experience a simple game of battleships, using python, and stored in a run.py. 
The game will consist of a a greeting and then ask for the name of player. There after there will be a board, with 5 rows and 5 columns.
The general rules of battleships apply, hit all your opponents ships, before they hit yours.
This game will generate a random guess from the computer. 
The game will restart when there is a winner. You can continue, another game thereafter.
>>>>>>> 8c3a9cfeebb59b6182a6e515754601c38303573a

## The Board

* 5 rows, 5 colums, no way of clicking out of the board.
*
* Do not edit any of the other files or your code may not deploy properly




## The Boats

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
