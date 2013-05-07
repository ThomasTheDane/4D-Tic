4D-Tic-Tac-Toe
==============

This is a program that allows you to play the fun game of 4D-Tic-Tac-Toe

Rules of 4D-Tic-Tac-Toe
=======================

There can be any number of players \n
The players each have a unique symbol, such as X or O or W \n
Each player takes turn placing their symbol on a 9x9 board \n
They can place anywhere that doesn't have another symbol on it
The board is set up as 3x3 grid of 3x3 boards
There are a few ways to win with the placement of pieces
First, you can win within any of the small boards by classic rules of Tic-Tac-Toe
Secondly, you can get the same spot in 3 connected large boards
Thirdly, you can get three connected spots on three connected boards

Setting up game:
================

Upon start, you will be prompted to enter number of players 
  The number can be any positive integer value and specifies the number of players
Afterwards, for each player you will be asked what type of player it is
  Monkey will place randomly on the board automatically when it becomes its turn
  AI will make intellegent moves to try to win automatically when it becomes its turn
  Human will prompt for input from the user when it becomes its turn
You will then be asked for the symbols of each player
  These symbols are signle characters that haven't already been taken
  They represent each player on the board

Playing the Game:
=================

The the beginning of every turn the board will be printed for reference
Both AI and Monkey will move automatically and it will become the next turn
For a human player's turn, it will ask to input a two piece number to place the persons's symbol
  The first number will refer to which board to play on, 1-9 going from top left to bottom right
  The second number will refer to which position in that board to play on, 1-9 going from top left to bottom right
The game will detect when someone wins and will congradulate them accordingly
