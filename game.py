from tabulate import tabulate as tab

#
turn_count = 0
game_count = 0
play_mark = "X"
player_input = ""
next_player = ""
win_name = ""
input_variable = ""
again = "y"


class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score


player_1 = Player("", 0)
player_2 = Player("", 0)


# sets blank game grid
def reset_grid(grid):
    for row in grid:
        for i in range(3):
            row[i] = ""


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
def turn():
    # look to remove global vars
    global next_player
    global turn_count

    while True:
        try:
            # simplify following
            if (game_count % 2) == 0:
                if (turn_count % 2) == 0:
                    ox = "O"
                    next_player = player_2.name
                else:
                    ox = "X"
                    next_player = player_1.name
            else:
                if (turn_count % 2) == 0:
                    ox = "X"
                    next_player = player_1.name
                else:
                    ox = "O"
                    next_player = player_2.name

            player_guess = input(input_variable)

            guess_x = function_x(player_guess)
            guess_y = function_y(player_guess)

            if game_grid[guess_y][guess_x] in ("O", "X"):
                print("\nChoose empty field")
                continue
            elif game_grid[guess_y][guess_x] == "":
                game_grid[guess_y][guess_x] = ox
                break
        except TypeError:
            print("\nInvalid grid reference")
        except IndexError:
            print("\nInvalid grid reference")
        else:
            break

    print_table()

    turn_count += 1


# win check function
def win_check():
    for row in game_grid:  # check rows
        if row[0] == row[1] == row[2] and row[1] != "":
            return True
    for x in range(3):  # check columns
        if game_grid[0][x] == game_grid[1][x] == game_grid[2][x] and game_grid[1][x] != "":
            return True
    if game_grid[0][0] == game_grid[1][1] == game_grid[2][2] and game_grid[0][0] != "":  # diagonal down
        return True
    elif game_grid[2][0] == game_grid[1][1] == game_grid[0][2] and game_grid[1][1] != "":  # diagonal up
        return True


def draw_check():
    if turn_count == 9:
        return True


def print_winner():
    global win_name
    # also simplify the following
    if (game_count % 2) == 0:
        if (turn_count % 2) == 0:
            win_name = player_2.name
        else:
            win_name = player_1.name
    else:
        if (turn_count % 2) == 0:
            win_name = player_1.name
        else:
            win_name = player_2.name
    print("Game over! " + win_name + " wins!")


def score_display():
    if win_name == player_1.name:
        player_1.score += 1
    elif win_name == player_2.name:
        player_2.score += 1
    print("\nScore:\n" +
          str(player_1.name) + " = " + str(player_1.score) + "\n" +
          str(player_2.name) + " = " + str(player_2.score)
          )


# game

print('\n'"Welcome to Noughts and Crosses" '\n')

print_table()

while True:
    if turn_count == 0 and game_count == 0:
        player_1.name = input("Player 1, enter your name: ")
        next_player = player_1.name
        input_variable = "\n%s, you are noughts.\n" \
                         "Enter grid reference in the form of a letter then number e.g. """""b2" """ ": " \
                         % next_player
        turn()

    elif turn_count == 1 and game_count == 0:
        player_2.name = input("\nPlayer 2, enter your name: ")
        next_player = player_2.name
        input_variable = "\n%s, you are crosses.\n" \
                         "Enter grid reference of empty field: " \
                         % next_player
        turn()

    else:
        while again == "y":
            if turn_count > 1 or game_count >= 1:
                input_variable = "\n" + next_player + ", take your turn: "
                turn()
                win_check()

            if win_check():
                pass
            elif draw_check():
                pass

            if win_check():
                print_winner()
                game_count += 1
                turn_count = 0
                score_display()
                reset_grid(game_grid)
                break
            elif draw_check():
                print("\nIt's a draw")
                game_count += 1
                turn_count = 0
                score_display()
                reset_grid(game_grid)
                break

        again = input("\nWould you like to play again, y/n? ")

        while again != ("y", "n"):
            if again == "y":
                print_table()
                break
            elif again == "n":
                exit()
            else:
                break
