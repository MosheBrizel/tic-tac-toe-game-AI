# tic-tac-toe-game-AI
Python Tic-Tac-Toe game using Tkinter. Play against AI player. The game logic checks for wins and ties. AI uses stored data for intelligent moves. Reset button for new games. Functional and can be improved on GitHub.

## Tic Tac Toe

This is a single player Tic Tac Toe game against the computer, implemented in Python with a graphical user interface using Tkinter.

## Game Description

- It's a classic Tic Tac Toe game on a 3x3 board. 

- The player plays against the computer who chooses moves randomly or based on analysis of previous moves.

- The computer learns and remembers successful and failed moves to improve its ability in future games.

- When there is a winner or tie, the board resets for a new game.

## Requirements

- Python 3
- Tkinter, random, json libraries

## Usage

Simply run the `tic_tac_toe_AI` file to start a new game:


~`~`
python tic_tac_toe_AI.py
~`~` 



## Code Structure

- `tic_tac_toe_AI.py` - Main code file containing the Tkinter GUI and game logic
- `dict.json` - File for saving computer move information from previous games

Main functions:

- `press_button` - Handles player's move
- `computer_choice` - Chooses a move for the computer  
- `check_all` - Checks if there is a winner or tie
- `add_value_dict` - Updates successful/failed move info for the computer
- `clear_screen` - Resets the board for a new game
