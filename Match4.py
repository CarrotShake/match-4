def print_board():
    for i in range(7):
        print(i+1, end=" ")
    print("\n")
    for row in rows:
        for column in row:
            symbol = "O"
            if column == 1:
                symbol = "+"
            elif column == 2:
                symbol = "-"
            print(symbol, end=" ")
        print()
    print()


def turn(player, column):
    vacancy = len(rows) - 1
    for row in range(len(rows)):
        if rows[row][column] != 0:
            vacancy = row - 1
            rows[vacancy][column] = player
            return vacancy
    rows[vacancy][column] = player
    return vacancy


def sequence(player, length, row, column, direction):
    if (row == len(rows)) or (column == len(rows[0])) \
            or (row == -1) or (column == -1) \
            or (rows[row][column] != player):
        return False
    if length == 4:
        return True
    if direction == "right":
        return sequence(player, length + 1, row + 1, column, direction)
    elif direction == "down":
        return sequence(player, length + 1, row, column + 1, direction)
    elif direction == "right_diagonal":
        return sequence(player, length + 1, row + 1, column - 1, direction)
    else:
        return sequence(player, length + 1, row + 1, column + 1, direction)


def game_over():
    full_row = True
    for column in rows[0]:
        if column == 0:
            full_row = False

    if full_row:
        return -1
    for row in range(len(rows)):
        for column in range(len(rows[row])):
            if rows[row][column] == 0:
                continue
            if      sequence(rows[row][column], 1, row, column, "right") or \
                    sequence(rows[row][column], 1, row, column, "down") or \
                    sequence(rows[row][column], 1, row, column, "left_diagonal") or \
                    sequence(rows[row][column], 1, row, column, "right_diagonal"):
                return rows[row][column]

    return 0


def play(player):
    print("Player " + str(player) + ", Choose a row:", end=" ")
    return int(input()) - 1


def game():
    player = 2
    while not game_over():
        if player == 1:
            player = 2
        else:
            player = 1
        print_board()
        column = play(player)
        while turn(player, column) == -1:
            column = play(player)
    print_board()
    print("Player " + str(player) + " won!")
    return game_over()


rows = []
for ap in range(6):
    rows.append([0] * 7)

game()