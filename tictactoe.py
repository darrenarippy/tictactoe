def tic_tac_toe():
    turns = 1
    grid = "_________"
    print_board(grid)
    while not any(get_game_state(grid)):
        grid = update_board(grid, get_move(), turns)
        print_board(grid)
        turns += 1
    print_game_state(get_game_state(grid))


def print_board(grid_state):
    # set horizontal border
    horizontal_border = "---------"

    # print grid as a tic-tac-toe board
    row_string = ""
    print(horizontal_border)
    for i in range(len(horizontal_border)):
        if i % 3 == 0:
            row_string = ""
            row_string += "| " + grid_state[i] + " "
        elif i % 3 == 1:
            row_string += grid_state[i] + " "
        else:
            row_string += grid_state[i] + " |"
            print(row_string)
    print(horizontal_border)


def print_game_state(game_state):
    print(game_state[0], game_state[1])


def get_game_state(grid_state):
    if not are_number_turns_valid(grid_state):
        state = ["Impossible", '']
    else:
        empty_cells_remain = are_there_empty_cells(grid_state)
        winners = get_winners(grid_state)

        # determine the state of the game based on the length of the
        # winners list
        # 1 winner --> winner
        # 0 winners --> not finished or draw
        # multiple winners --> impossible game
        if len(winners) > 0:
            state = [winners[0], "wins"] if len(winners) == 1 \
                else ["Impossible", '']
        else:
            state = [] if empty_cells_remain else ["Draw", '']
    return state


def are_number_turns_valid(grid_state):
    number_of_x = grid_state.count("X")
    number_of_o = grid_state.count("O")
    return not abs(number_of_x - number_of_o) > 1


def are_there_empty_cells(grid_state):
    return "_" in grid_state


def get_winners(grid_state):
    winners = list()
    winners = check_rows(grid_state, winners, "X")
    winners = check_rows(grid_state, winners, "O")
    winners = check_columns(grid_state, winners, "X")
    winners = check_columns(grid_state, winners, "O")
    winners = check_diagonals(grid_state, winners, "X")
    winners = check_diagonals(grid_state, winners, "O")
    return winners


def check_rows(grid_state, list_of_winners, player):
    list_of_winners = check_row(grid_state, list_of_winners, player, 1)
    list_of_winners = check_row(grid_state, list_of_winners, player, 2)
    list_of_winners = check_row(grid_state, list_of_winners, player, 3)
    return list_of_winners


def check_row(grid_state, list_of_winners, player, row):
    if grid_state.count(player, (row - 1) * 3, row * 3) == 3:
        list_of_winners.append(player)
    return list_of_winners


def check_columns(grid_state, list_of_winners, player):
    list_of_winners = check_column(grid_state, list_of_winners, player, 1)
    list_of_winners = check_column(grid_state, list_of_winners, player, 2)
    list_of_winners = check_column(grid_state, list_of_winners, player, 3)
    return list_of_winners


def check_column(grid_state, list_of_winners, player, column):
    column_state = ""
    for i in range(column - 1, 9, 3):
        column_state += grid_state[i]
    if column_state.count(player) == 3:
        list_of_winners.append(player)
    return list_of_winners


def check_diagonals(grid_state, list_of_winners, player):
    list_of_winners = check_diagonal(grid_state, list_of_winners, player, "L")
    list_of_winners = check_diagonal(grid_state, list_of_winners, player, "R")
    return list_of_winners


def check_diagonal(grid_state, list_of_winners, player, diagonal):
    start, stop, step = 0, 9, 4
    if diagonal == "R":
        start, stop, step = 2, 8, 2

    diagonal_state = ""
    for i in range(start, stop, step):
        diagonal_state += grid_state[i]
    if diagonal_state.count(player) == 3:
        list_of_winners.append(player)
    return list_of_winners


def update_board(board_state, coordinates, number_of_turns):
    row, column = coordinates[0], coordinates[1]
    cell = ((row - 1) * 3) + (column - 1)
    while board_state[cell] != "_":
        print("This cell is occupied! Choose another one!")
        coordinates = get_move()
        row, column = coordinates[0], coordinates[1]
        cell = ((row - 1) * 3) + (column - 1)
    # Player X plays on odd turns, Player O on even turns
    player = "X" if number_of_turns % 2 else "O"
    board_state = board_state[:cell] + player + board_state[cell + 1:]
    return board_state


def get_move():
    coordinates_input = get_numeric_input()
    coordinates = get_valid_coordinates(coordinates_input)
    row, column = int(coordinates[0]), int(coordinates[1])
    return [row, column]


def get_valid_coordinates(user_input):
    coordinates = user_input.split()
    while coordinates[0] not in "123" or coordinates[1] not in "123":
        print("Coordinates should be from 1 to 3!")
        user_input = get_numeric_input()
        coordinates = user_input.split()
    return coordinates


def get_numeric_input():
    coordinates_input = input("Enter the coordinates: ").strip()
    while not coordinates_input.replace(" ", "").isnumeric():
        print("You should enter numbers!")
        coordinates_input = input("Enter the coordinates: ").strip()
    return coordinates_input


tic_tac_toe()
