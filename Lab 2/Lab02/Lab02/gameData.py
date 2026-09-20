"""
Name: Cristofer Rojas
Last Updated: September 20, 2026
Description: This file contains the GameData class and methods for
managing the game board, player movement, food, and enemy movement.
"""

import random

from cell import Cell
import cell
from preferences import Preferences

class GameData:
    def __init__(self):
        # The current state of the board
        self.board = [[Cell(row, col) for col in range(Preferences.NUM_COLS)] 
                                      for row in range(Preferences.NUM_ROWS)]
        
        # Whether or not the game is over
        self.gameover = False

        # The current cell containing the player
        self.player = self.board[0][0]    # Start at the top left
        self.player.become_player()

        # The number of empty cells on the board, accounting for the player cell
        self.num_empty_cells = Preferences.NUM_CELLS - 1

        # A list of cells containing food
        self.food = []
        # Number of food eaten
        self.score = 0

        # A list of cells containing enemies
        self.enemies = []


    #######################
    # Game Limits Methods #
    #######################

    def at_max_food(self) -> bool:
        """ Check whether we can add more food """
        return len(self.food) / self.num_empty_cells > Preferences.MAX_FOOD
    
    def at_max_enemies(self) -> bool:
        """ Check whether we can add more enemies """
        return len(self.enemies) / self.num_empty_cells > Preferences.MAX_ENEMIES

    def set_game_over(self) -> None:
        """ Turn on the game over flag """
        self.gameover = True


    ##############################
    # Neighbor Retrieval Methods #
    ##############################

    def get_west_neighbor(self, cell: Cell) -> Cell:
        """ Returns the cell immediately to the left of the given cell.
        If we are at the edge of the map, return None. """

        row = cell.get_row()
        col = cell.get_col()

        if col == 0:
            return None

        return self.board[row][col - 1]

    def get_east_neighbor(self, cell: Cell) -> Cell:
        """ Returns the cell immediately to the right of the given cell.
        If we are at the edge of the map, return None. """

        row = cell.get_row()
        col = cell.get_col()

        if col == Preferences.NUM_COLS - 1:
            return None

        return self.board[row][col + 1]


    def get_north_neighbor(self, cell: Cell) -> Cell:
        """ Returns the cell immediately above the given cell.
        If we are at the edge of the map, return None. """

        row = cell.get_row()
        col = cell.get_col()

        if row == 0:
            return None

        return self.board[row - 1][col]


    def get_south_neighbor(self, cell: Cell) -> Cell:
        """ Returns the cell immediately below the given cell.
        If we are at the edge of the map, return None. """

        row = cell.get_row()
        col = cell.get_col()

        if row == Preferences.NUM_ROWS - 1:
            return None

        return self.board[row + 1][col]

        ###########################
        # Player Movement Methods #
        ###########################
        
    def move_player_right(self) -> None:
        """ Move the player one cell to the right if possible """
        cell = self.get_east_neighbor(self.player)

        if cell is not None:
            self.move_player_to_cell(cell)


    def move_player_left(self) -> None:
        """ Move the player one cell to the left if possible """
        cell = self.get_west_neighbor(self.player)

        if cell is not None:
            self.move_player_to_cell(cell)


    def move_player_up(self) -> None:
        """ Move the player one cell up if possible """
        cell = self.get_north_neighbor(self.player)

        if cell is not None:
            self.move_player_to_cell(cell)


    def move_player_down(self) -> None:
        """ Move the player one cell down if possible """
        cell = self.get_south_neighbor(self.player)

        if cell is not None:
            self.move_player_to_cell(cell)

    def move_player_to_cell(self, cell: Cell) -> None:
        """ Move the player to the given cell """

        # If there is food in this cell, eat it
        if cell.is_food():
            self.eat_food(cell)
            self.update_player_cell(cell)
        # If there is an enemy in this cell, game over!
        elif cell.is_enemy():
            self.player.become_empty()
            self.set_game_over()
        # Otherwise, update the player location
        else:
            self.update_player_cell(cell)

    def update_player_cell(self, new_cell: Cell) -> None:
        """ Move the player to the new cell """
    
        # Empty the cell the player just moved away from
        self.player.become_empty()
        # Update the player to the new cell
        self.player = new_cell
        # Change the new cell to be the player type
        self.player.become_player()


    ########################
    # Food Related Methods #
    ########################

    def add_food(self) -> None:
     """ Adds food to a random open spot on the board """

     #fine a row on the board
     row = random.randrange(0, Preferences.NUM_ROWS)
       
        # Find a col on the board
     col = random.randrange(0, Preferences.NUM_COLS)

     cell = self.board[row][col]

     if cell.is_empty():
            cell.become_food()
            self.food.append(cell)
            self.num_empty_cells -= 1

        

    def eat_food(self, cell: Cell) -> None:
        """ Behavior for when the player eats food """

        self.food.remove(cell)
        self.score += 1
        self.num_empty_cells += 1


    ##########################
    # Enemy Movement Methods #
    ##########################

    def add_enemy(self) -> None:
        """ Adds an enemy to the bottom right corner of the board """
        cell = self.board[Preferences.NUM_ROWS - 1][Preferences.NUM_COLS - 1]

        if cell.is_player():
            self.set_game_over()

        elif cell.is_food():
            self.food.remove(cell)
            cell.become_enemy()
            self.enemies.append(cell)

        elif cell.is_empty():
            cell.become_enemy()
            self.enemies.append(cell)
            self.num_empty_cells -= 1
       

    def move_enemy_to_cell(self, enemy_cell: Cell,
                       cell: Cell, idx: int) -> None:
        """ Moves the enemy cell to a new location.
            idx represents the index of that enemy in
            the enemies list. """

        if cell.is_player():
            enemy_cell.become_empty()
            self.set_game_over()

        elif cell.is_food():
            enemy_cell.become_empty()
            self.food.remove(cell)
            cell.become_enemy()
            self.enemies[idx] = cell
            self.num_empty_cells += 1

        elif cell.is_empty():
            enemy_cell.become_empty()
            cell.become_enemy()
            self.enemies[idx] = cell

        elif cell.is_enemy():
            return

    def move_enemy_left(self, idx: int) -> None:
        """ Move the enemy at index idx left one cell """

        enemy_cell = self.enemies[idx]
        cell = self.get_west_neighbor(enemy_cell)

        if cell is not None:
            self.move_enemy_to_cell(enemy_cell, cell, idx)


    def move_enemy_right(self, idx: int) -> None:
        """ Move the enemy at index idx right one cell """

        enemy_cell = self.enemies[idx]
        cell = self.get_east_neighbor(enemy_cell)

        if cell is not None:
            self.move_enemy_to_cell(enemy_cell, cell, idx)


    def move_enemy_up(self, idx: int) -> None:
        """ Move the enemy at index idx up one cell """

        enemy_cell = self.enemies[idx]
        cell = self.get_north_neighbor(enemy_cell)

        if cell is not None:
            self.move_enemy_to_cell(enemy_cell, cell, idx)


    def move_enemy_down(self, idx: int) -> None:
        """ Move the enemy at index idx down one cell """

        enemy_cell = self.enemies[idx]
        cell = self.get_south_neighbor(enemy_cell)

        if cell is not None:
            self.move_enemy_to_cell(enemy_cell, cell, idx)

