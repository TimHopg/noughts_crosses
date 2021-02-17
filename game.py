from tabulate import tabulate as tab

# don't need all vars defined so early
turn_count = 0
game_count = 0
input_variable = ""
replay = "y"
winner = -1
players_list = [1, 2]


class Player:
    def __init__(self):
        self.name = None
        self.score = 0
        self.symbol = None

    def prompt_name(self, symbol):
        self.name = input("Enter your name: ")
        self.symbol = symbol

        print("Welcome %s, you are %ss."
              % (self.name, self.symbol))


def switch_players(player, players):
    if player not in players:
        print("Something went wrong")
    # following doesn't scale well
    if current_player == players[0]:
        return players[1]
    else:
        return players[0]


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
# can combine these into one function with methods
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
def turn(player):
    while True:
        try:
            player_guess = input(input_variable)

            guess_x = function_x(player_guess)
            guess_y = function_y(player_guess)

            if game_grid[guess_y][guess_x] in ("O", "X"):
                print("\nChoose empty field")
                continue
            elif game_grid[guess_y][guess_x] == "":
                game_grid[guess_y][guess_x] = player.symbol
                print_table()
                break
        except TypeError:
            print("\nInvalid grid reference")
        except IndexError:
            print("\nInvalid grid reference")
        else:
            break


# win check function
def win_check():
    for row in game_grid:  # check rows
        if row[0] == row[1] == row[2] and row[1] != "":
            return row[0]
    for x in range(3):  # check columns
        if game_grid[0][x] == game_grid[1][x] == game_grid[2][x] and game_grid[1][x] != "":
            return game_grid[0][x]
    if game_grid[0][0] == game_grid[1][1] == game_grid[2][2] and game_grid[0][0] != "":  # diagonal down
        return game_grid[0][0]
    elif game_grid[2][0] == game_grid[1][1] == game_grid[0][2] and game_grid[1][1] != "":  # diagonal up
        return game_grid[2][0]
    if turn_count == 9:
        return "draw"
    return -1


def score_display(player):
    player.score += 1
    print("\nScore:\n" +
          str(player_1.name) + " = " + str(player_1.score) + "\n" +
          str(player_2.name) + " = " + str(player_2.score))


player_1 = Player()
player_2 = Player()

# game
if __name__ == "__main__":
    print('\n'"Welcome to Noughts and Crosses" '\n')
    print("Player 1 ")
    player_1.prompt_name("O")
    print("\nPlayer 2 ")
    player_2.prompt_name("X")
    players_list = [player_1, player_2]
    current_player = player_1
    print_table()
    print("\nEnter grid reference in the form of a letter then number e.g. b2.")

    while replay == "y":
        input_variable = "\n" + current_player.name + ", take your turn: "
        turn(current_player)
        turn_count += 1
        winner = win_check()
        if winner != (-1 or "draw"):
            print("Game over! " + current_player.name + " wins!")
            game_count += 1
            turn_count = 0
            score_display(current_player)
            reset_grid(game_grid)
            winner = -1
            break
        elif winner == "draw":
            print("\nIt's a draw")
            game_count += 1
            turn_count = 0
            score_display(current_player)
            reset_grid(game_grid)
            winner = -1
            break
        current_player = switch_players(current_player, players_list)

    replay = input("\nWould you like to play again, y/n? ")

    while replay != ("y", "n"):
        if replay == "y":
            print_table()
            break
        elif replay == "n":
            exit()
        else:
            break
