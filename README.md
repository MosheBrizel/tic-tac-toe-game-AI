# Tic Tac Toe with Learning AI

A tic tac toe game with a GUI and AI opponent that learns to play better

## Overview

This project implements a playable tic tac toe game with a graphical interface. It includes an AI opponent that progressively learns to make better moves based on past games. 

The purpose is to demonstrate basic reinforcement learning techniques to create an AI agent that improves its strategy through experience.

![tic-tac-toe-preview]./tic_tuc_to.gif)

## Features

- Graphical tic tac toe game board using Tkinter
- Single or two player modes  
- Adjustable board size
- AI opponent with progressive learning
- Saves learned data to a file
- Game reset and new game options

## How It Works 

The AI player uses a dictionary to store move data based on past game results. It tracks which moves lead to wins vs losses from every board configuration.

Using this data, the AI learns which moves have higher historical win rates. It progressively improves by favoring moves that are more likely to lead to a victory.

The learned move data persists between game sessions by saving to a JSON file. This allows the AI to build on past experience and keep improving.

## Code Details

- `press_bottom()` - Handle player moves  
- `computer_choice()` - Select AI moves    
- `check_all()` - Check for win/tie
- `clear_screen()` - Reset board  
- `add_value_dict()` - Update move data

The core gameplay loop is in `add_list()`, which processes turns and checks for a winner.

The AI learning happens in `add_value_dict()`, updating the move data dictionary after each game.

This implementation shows how basic reinforcement learning can be applied to create a game AI that learns from experience. The GUI and file persistence provide a complete playable game package.
