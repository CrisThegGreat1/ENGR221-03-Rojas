# ENGR 221 - Lab 02

## Author
Cristofer Rojas

## Date
September 20, 2026

## Description
This lab implements a grid-based game using Python. The program uses cells on a game board to represent the player, food, enemies, and empty spaces.

The lab includes functionality for:
- Finding neighboring cells in each direction
- Moving the player around the game board
- Preventing the player from moving outside the board
- Adding food to random empty cells
- Allowing the player to eat food
- Updating the player's score when food is eaten
- Adding enemies to the game board
- Moving enemies around the board
- Detecting interactions between the player, food, and enemies
- Ending the game when the player encounters an enemy

## Files

### `gameData.py`
Contains the `GameData` class and manages the state of the game. It includes the neighbor retrieval methods, player movement methods, food methods, and enemy movement methods.

### `cell.py`
Contains the `Cell` class. Cells can represent the player, food, an enemy, or an empty location on the board.

### `controller.py`
Runs the game and handles user input. The player can be controlled using the arrow keys.

### `boardDisplay.py`
Handles the visual display of the game board.

### `preferences.py`
Contains constants and settings used by the game, such as the number of rows and columns and display colors.

### `images/`
Contains image files used by the game.

## How to Run
Run the following file:

`controller.py` Im on PC windows which uses Powershell I think the command for linux 
is Python followed by the name of the file so "python "controller.py"" 

Once the game window opens, use the arrow keys to move the player around the board.

## Controls
- Up Arrow - Move up
- Down Arrow - Move down
- Left Arrow - Move left
- Right Arrow - Move right

## Game Behavior
Food is added to the board periodically. When the player moves onto a food cell, the food is removed and the player's score increases.

Enemies are also added periodically and move around the board. If the player encounters an enemy, the game ends.

## Testing
The program was tested to verify that:
- The player moves correctly in all four directions.
- The player cannot move beyond the boundaries of the board.
- Food is added correctly.
- Food disappears when eaten.
- The score increases when food is eaten.
- Enemies are added correctly.
- Enemies move correctly.
- Encountering an enemy triggers the game-over behavior.
