def wins(grid, player):
    lines = []
    lines += [[grid[i][j] for j in range(3)] for i in range(3)]      # rows
    lines += [[grid[i][j] for i in range(3)] for j in range(3)]      # columns
    lines.append([grid[i][i] for i in range(3)])                    # diagonal
    lines.append([grid[i][2 - i] for i in range(3)])                # anti-diagonal
    return any(all(cell == player for cell in line) for line in lines)


def solve():
    grid = [input() for _ in range(3)]

    count_x = sum(row.count('X') for row in grid)
    count_o = sum(row.count('0') for row in grid)

    x_won = wins(grid, 'X')
    o_won = wins(grid, '0')

    # Basic count validity: X goes first, so count_x == count_o or count_x == count_o + 1
    if count_x < count_o or count_x > count_o + 1:
        print("illegal")
        return

    # Both can't win at once
    if x_won and o_won:
        print("illegal")
        return

    # If X won, the move that won must have been X's -> counts differ by exactly 1
    if x_won and count_x != count_o + 1:
        print("illegal")
        return

    # If O won, the move that won must have been O's -> counts must be equal
    if o_won and count_x != count_o:
        print("illegal")
        return

    if x_won:
        print("the first player won")
        return
    if o_won:
        print("the second player won")
        return

    if count_x + count_o == 9:
        print("draw")
        return

    print("first" if count_x == count_o else "second")


solve()
