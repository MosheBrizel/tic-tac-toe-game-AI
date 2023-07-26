# Importing required modules
import tkinter
from tkinter import *
from tkinter import messagebox
from random import randint
import json

# Creating the main application window
window = Tk()
window.title("tic tac")
window.configure(bg="#F5F5DC")

# Setting up the game board size
len_game = 3

# Initializing variables
str_computer = ""
counter = 0
tie = False

# Creating a frame for the game board
frame_bottom = tkinter.Frame(window, bg="#F5F5DC")
frame_bottom.pack(padx=20, pady=20)

# Creating a dictionary to store the game board values (o and x)
dict_o_x = {x: [" " for i in range(len_game)] for x in range(len_game)}

# Variable to keep track of the list of losing moves for the computer
list_lose = ""
list_lose_time = []

# Creating a dictionary to store the GUI buttons for the game board
dict_bottom = {x: [" " for y in range(len_game)] for x in range(len_game)}

# Attempting to load previous computer move information from a file, otherwise initializing an empty dictionary
try:
    file = "dict.txt"
    with open("file1.json", "r") as dict_file:
        computer_information = json.load(dict_file)

except:
    computer_information = {}
    with open('file1.json', 'w') as f:
        json.dump(computer_information, f)

# Printing the loaded computer information for debugging
print(computer_information)

# Dictionary to store the moves and corresponding counter for each level (board configuration)
level_dict = {}

# Dictionary to store the last move for each level (board configuration) made by the user
dict_lest_move = {}

# Counter for the number of times the user makes a move
counter_time = 0

# Function to add the value (move and counter) to the dictionary for the given level (board configuration)
def add_value_dict(dict_level, win_game):
    global level_dict

    # Increment the counter for the winning move
    if win_game:
        for table in dict_level:
            if table not in computer_information:
                computer_information[table] = {}
            if dict_level[table] not in computer_information[table]:
                computer_information[table][dict_level[table]] = 0
            computer_information[table][dict_level[table]] += 1

    # Decrement the counter for the losing move
    else:
        for table in dict_level:
            if table in computer_information:
                if dict_level[table] in computer_information[table]:
                    computer_information[table][dict_level[table]] -= 1

    level_dict = {}

# Function to change the background color of a button on the game board
def red_button(row_int, col_int, bg="red"):
    global button_game
    dict_bottom[row_int][col_int]["bg"] = bg

# Function to make a move for the computer based on the stored information (moves and counters) in computer_information
def computer_choice():
    global computer_move
    map_dict = str(dict_o_x)
    num_move = 0
    counter_move = 1

    try:
        # Checking if there is information available for the current game board configuration
        if len(computer_information[map_dict]) > 0:
            for move in computer_information[map_dict]:
                counter_move += 1
                if computer_information[map_dict][move] > num_move:
                    num_move = computer_information[map_dict][move]
                    computer_move = move
            if num_move > 0:
                # Making the computer move
                press_bottom(int(computer_move[0]), int(computer_move[1]), dict_bottom[int(computer_move[0])][int(computer_move[1])])
                return
    except:
        # If there is no information available for the current game board configuration, make a random move
        random_computer_one = randint(0, len_game - 1)
        random_computer_two = randint(0, len_game - 1)
        while dict_o_x[random_computer_one][random_computer_two] != " ":
            random_computer_one = randint(0, len_game - 1)
            random_computer_two = randint(0, len_game - 1)
        press_bottom(random_computer_one, random_computer_two, dict_bottom[random_computer_one][random_computer_two])

# Function to handle button press for user's move
def press_bottom(row_int, col_int, bottom):
    global counter
    counter += 1

    # Updating the game board data
    dict_o_x[row_int][col_int] = "o" if counter % 2 == 1 else "x"
    bottom["text"] = dict_o_x[row_int][col_int]
    bottom["disabledforeground"] = "black"
    bottom["state"] = "disabled"
    bottom["fg"] = "black"
    add_list(row_int, col_int)

# Function to handle the user's move and update the dictionary of last moves
def add_list(row_int, col_int):
    global counter, information, label_winner, str_computer, str_level, list_lose, counter_time, dict_lest_move, move_user
    win = check_all()

    if win and counter != len_game * len_game:
        # Displaying the winner if there is one
        label_winner = Label(window, text=f"The winner is : {'o' if counter % 2 == 1 else 'x'}", font=("Arial", 30), fg="green")
        label_winner.place(relx=0.5, rely=0.5, anchor=CENTER)

    if counter % 2 == 1 and counter != len_game * len_game and counter != 1:
        # Storing the last move made by the user
        dict_lest_move[str_level] = str(row_int) + str(col_int)

    # Check if the computer has lost and update the move information
    if win and counter % 2 == 1 and not tie:
        dict_lest_move[str_level] = str(row_int) + str(col_int)
        add_value_dict(level_dict, False)
        if str_level in list_lose_time:
            add_value_dict(level_dict, False)
            add_value_dict(level_dict, False)
            list_lose_time.remove(str_level)
        list_lose_time.append(str_level)
        add_value_dict(dict_lest_move, True)
        add_value_dict(dict_lest_move, True)
        dict_lest_move = {}
        print("win")

    if counter % 2 == 1 and counter != len_game * len_game:
        # Storing the user's move for the computer's next turn
        move_user = str(row_int) + str(col_int)
        str_level = str(dict_o_x)

    elif counter % 2 == 0:
        # Storing the level (board configuration) and user's move for the computer's turn
        level_dict[str_level] = str(row_int) + str(col_int)
        if counter > 2:
            list_lose = str_level

    if win or counter == len_game * len_game:
        # If there is a winner or the game is tied, update the move information
        add_value_dict(level_dict, True)

    if not win and counter % 2 == 1 and counter < len_game * len_game:
        # If there is no winner yet and it's the computer's turn, let the computer make a move
        computer_choice()

# Function to initialize the game board buttons and output them on the GUI
def first_output():
    global button_game, clear_button
    for i in range(len_game):
        for x in range(len_game):
            button_rook = Button(frame_bottom, text=dict_o_x[i][x], bg="#F5F5DC", fg='black', font=("Helvetica", 50), width=3, height=1)
            button_rook.configure(command=lambda row=i, col=x, button_num=button_rook: press_bottom(row, col, button_num))
            button_rook.grid(row=i, column=x)
            dict_bottom[i][x] = button_rook

    clear_button.pack()

# Function to lock all the buttons on the game board after the game is over
def lock_buttons():
    for i in range(len_game):
        for x in range(len_game):
            dict_bottom[i][x]["state"] = "disabled"
            dict_bottom[i][x]["disabledforeground"] = "black"

# Function to check for a win or tie condition after each move
def check_all():
    global button_game, column, line, counter, tie
    # Check the rows.
    line_output = 0
    for line in dict_o_x:
        line_output = line
        for column in range(len_game - 1):
            if dict_o_x[line][column] != dict_o_x[line][column + 1] or (dict_o_x[line][column] != "o" and dict_o_x[line][column] != "x"):
                break
        else:
            # If a row has the same symbol for all cells, highlight the winning row and return True
            lock_buttons()
            for col in range(len_game):
                red_button(line_output, col, bg="green" if counter % 2 == 1 else 'red')
            return True

    # Check the columns.
    column_output = -1
    for column in range(len_game):
        column_output += 1
        for line in range(len_game - 1):
            if dict_o_x[line][column] != dict_o_x[line + 1][column] or (dict_o_x[line][column] != "o" and dict_o_x[line][column] != "x"):
                break
        else:
            # If a column has the same symbol for all cells, highlight the winning column and return True
            lock_buttons()
            for lin in range(len_game):
                red_button(lin, column_output, bg="green" if counter % 2 == 1 else 'red')
            return True

    # Check the diagonals.
    for line_daon in range(len_game - 1):
        if dict_o_x[line_daon][line_daon] != dict_o_x[line_daon + 1][line_daon + 1] or (dict_o_x[line_daon][line_daon] != "o" and dict_o_x[line_daon][line_daon] != "x"):
            break
    else:
        # If the main diagonal has the same symbol for all cells, highlight the winning diagonal and return True
        lock_buttons()
        for line_daon_output in range(len_game):
            red_button(line_daon_output, line_daon_output, bg="green" if counter % 2 == 1 else 'red')
        return True

    # Check the reverse diagonals.
    column = 0
    column_output = 0
    for line_revers in range(len_game - 1, 0, -1):
        if dict_o_x[line_revers][column] != dict_o_x[line_revers - 1][column + 1] or (dict_o_x[line_revers][column] != "o" and dict_o_x[line_revers][column] != "x"):
            break
        column += 1
    else:
        # If the reverse diagonal has the same symbol for all cells, highlight the winning diagonal and return True
        lock_buttons()
        for line_revers_output in range(len_game, 0, -1):
            red_button(line_revers_output - 1, column_output, bg="green" if counter % 2 == 1 else 'red')
            column_output += 1
        return True

    # Check if the game is tied (no empty cells left)
    for empty in dict_o_x:
        if " " in dict_o_x[empty]:
            break
    else:
        lock_buttons()
        tie = True
        # Highlight all cells in red to indicate the tie
        for row in range(len_game):
            for col in range(len_game):
                red_button(row, col, bg="red")
        return True

    return False

# Function to clear the game board and start a new game
def clear_screen():
    global dict_o_x, counter, label_winner, list_lose, tie, str_level, dict_bottom, clear_button
    if not check_all():
        # Ask for confirmation before resetting the game board if there is no winner yet
        answer = messagebox.askokcancel("massage", "Are you sure you want to reset?")
        if not answer:
            return
    if label_winner:
        label_winner.destroy()

    # Clear the game board data
    dict_o_x = {x: [" " for i in range(len_game)] for x in range(len_game)}
    dict_bottom = {x: [" " for y in range(len_game)] for x in range(len_game)}
    list_lose = " "
    counter = 0
    first_output()
    tie = False
    str_level = str(dict_o_x)

# Initialize the game board and start the main event loop
information = ""
clear_button = Button(window, text="Clear", command=clear_screen)
first_output()
button_game = None
label_winner = None
window.mainloop()

# After the main event loop ends, save the computer move information to a file
print(computer_information)
with open('file1.json', 'w') as f:
    json.dump(computer_information, f)
