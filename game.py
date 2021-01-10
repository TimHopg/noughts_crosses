from tabulate import tabulate as tab

# sets blank game grid
game_grid = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]]
headers = ["a", "b", "c"]
rows = [1, 2, 3]


# functions to convert player input to int coordinates
def function_x(x):
    if x[0] == "a":
        return 0
    elif x[0] == "b":
        return 1
    elif x[0] == "c":
        return 2


def function_y(y):
    if y[1] == "1":
        return 0
    elif y[1] == "2":
        return 1
    elif y[1] == "3":
        return 2


# print table function
def print_table():
    print(tab(game_grid, headers=headers, tablefmt="fancy_grid", showindex=rows))


# turn function
def turn(player_guess, x_or_o):
    guess_x = function_x(player_guess)
    guess_y = function_y(player_guess)

    if game_grid[guess_y][guess_x] == "":
        game_grid[guess_y][guess_x] = x_or_o

    print_table()


def print_winner(x):
    print("Game over! Player " + x + " wins!")


# win check function
def win_check():
    if game_grid[0][0] == game_grid[0][1] == game_grid[0][2] and game_grid[0][0] != "":  # top
        return True
    elif game_grid[1][0] == game_grid[1][1] == game_grid[1][2] and game_grid[1][1] != "":  # middle
        return True
    elif game_grid[2][0] == game_grid[2][1] == game_grid[2][2] and game_grid[2][2] != "":  # bottom
        return True
    elif game_grid[0][0] == game_grid[1][0] == game_grid[2][0] and game_grid[0][0] != "":  # left
        return True
    elif game_grid[0][1] == game_grid[1][1] == game_grid[2][1] and game_grid[1][1] != "":  # middle
        return True
    elif game_grid[0][2] == game_grid[1][2] == game_grid[2][2] and game_grid[2][2] != "":  # right
        return True
    elif game_grid[0][0] == game_grid[1][1] == game_grid[2][2] and game_grid[0][0] != "":  # diagonal down
        return True
    elif game_grid[2][0] == game_grid[1][1] == game_grid[0][2] and game_grid[1][1] != "":  # diagonal up
        return True
    # elif game_grid[0][0],game_grid[0][1],game_grid[0][2],game_grid[1][0],game_grid[1][1],game_grid[1][2],game_grid[2][0],game_grid[2][1],game_grid[2][2] == "X" or "O":
    #     draw = True
    #     return True

# game
print('\n'
      "Welcome gamers to Noughts and Crosses" '\n'
      "Remember, the loser must rim the winner" '\n')

print_table()

player_input = input("\nPlayer 1 you are noughts.\n"
                     "Enter grid reference in the form of a letter then number e.g. """""b2" """ "to take your turn: ")
turn(player_input, "O")

player_input = input("\nPlayer 2 you are crosses.\n"
                     "Enter grid reference of empty field: ")
turn(player_input, "X")

while not win_check():
    player_input = input("\nPlayer 1, take your turn: ")
    turn(player_input, "O")
    if win_check():
        winner = "1"
        break
    player_input = input("\nPlayer 2, take your turn: ")
    turn(player_input, "X")
    if win_check():
        winner = "2"
        break

print_winner(winner)
