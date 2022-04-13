import os
import random


def update_board(board_location):
    board_print = (f" {board_location[0]} | {board_location[1]} | {board_location[2]}   \n"
                   f"---+---+---\n"
                   f" {board_location[3]} | {board_location[4]} | {board_location[5]}   \n"
                   f"---+---+---\n"
                   f" {board_location[6]} | {board_location[7]} | {board_location[8]}   \n"
                   )
    return board_print


def check_win(current_board):
    winner = False
    if current_board[0] == current_board[1] == current_board[2] and current_board[0] != " ":
        winner = True
    elif current_board[3] == current_board[4] == current_board[5] and current_board[3] != " ":
        winner = True
    elif current_board[6] == current_board[7] == current_board[8] and current_board[6] != " ":
        winner = True
    elif current_board[0] == current_board[3] == current_board[6] and current_board[0] != " ":
        winner = True
    elif current_board[1] == current_board[4] == current_board[7] and current_board[1] != " ":
        winner = True
    elif current_board[2] == current_board[5] == current_board[8] and current_board[2] != " ":
        winner = True
    elif current_board[0] == current_board[4] == current_board[8] and current_board[0] != " ":
        winner = True
    elif current_board[2] == current_board[4] == current_board[6] and current_board[2] != " ":
        winner = True
    return winner


def enter_selection(which_player, board_values):
    entry_valid = False
    while not entry_valid:
        try:
            cell_selection = int(input(f"Select a cell (1-9) for '{which_player}': "))
            if 0 < cell_selection <= 9 and board_values[cell_selection - 1] == " ":
                entry_valid = True
                return cell_selection
            else:
                raise ValueError
        except ValueError:
            print(f"Selection not valid.")


def computer_select(board_values):
    entry_valid = False
    while not entry_valid:
        cell_selection = random.randint(1, 9)
        if board_values[cell_selection - 1] == " ":
            return cell_selection
        else:
            entry_valid = False


def number_players():
    valid_players = False
    while not valid_players:
        num_of_players = int(input(f"How many player are playing 1 or 2: "))
        if num_of_players == 1 or num_of_players == 2:
            return num_of_players
        else:
            print("Selection not valid.")


board_composition = [" ", " ", " ",
                     " ", " ", " ",
                     " ", " ", " ",
                     ]

turn = 9
num_players = number_players()

while not check_win(board_composition) and turn > 0:
    os.system("cls")
    if turn % 2 != 0:
        player = "X"
    else:
        player = "O"

    print(update_board(board_composition))
    if num_players == 1 and player == "X":
        chosen_cell = enter_selection(player, board_composition)
    elif num_players == 1 and player == "O":
        chosen_cell = computer_select(board_composition)
    else:
        chosen_cell = enter_selection(player, board_composition)

    board_composition[chosen_cell - 1] = player
    check_win(board_composition)

    turn -= 1

os.system("cls")
print(update_board(board_composition))
if check_win(board_composition):
    print(f"Congratulations {player}!")
else:
    print(f"Tie Game!")
