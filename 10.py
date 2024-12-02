from collections import Counter
from ec import read_input


def get_word(grid):
    ls = []
    for y in range(2, 6):
        for x in range(2, 6):
            col = set(line[x] for line in grid)
            row = set(grid[y])
            for c in ["*", "."]:
                col.discard(c)
                row.discard(c)
            i = col.intersection(row).pop()
            ls.append(i)
    return "".join(ls)


lines = read_input(1)
grid = [[c for c in line] for line in lines]
print(get_word(grid))


def get_power(word):
    total = 0
    for i, c in enumerate(word):
        total += (i + 1) * (ord(c) - 64)
    return total


lines = read_input(2, split_lines=False)
rows = lines.split("\n\n")
grids = []
for row in rows:
    row_grids = []
    for l in row.splitlines():
        for i, part in enumerate(l.split(" ")):
            if i >= len(row_grids):
                row_grids.append([])
            row_grids[i].append([c for c in part])
    grids.extend(row_grids)

words = [get_word(g) for g in grids]
total = sum(get_power(w) for w in words)
print(total)


def fill_grid(grid):
    # fill in givens
    for y in range(2, 6):
        for x in range(2, 6):
            if grid[y][x] != ".":
                continue
            col = set(line[x] for line in grid)
            row = set(grid[y])
            for c in ["*", ".", "?"]:
                col.discard(c)
                row.discard(c)
            i = col.intersection(row)
            if len(i) == 1:
                grid[y][x] = i.pop()

    # now try to fill in blanks
    for y in range(2, 6):
        for x in range(2, 6):
            if grid[y][x] != ".":
                continue

            c = Counter()
            c.update(line[x] for line in grid)
            c.update(grid[y])
            if c["?"] != 1:
                continue
            unpaired = [
                k for (k, v) in c.items() if v == 1 and k not in ["?", "*", "."]
            ]
            if len(unpaired) == 1:
                grid[y][x] = unpaired[0]
                for r in range(len(grid[y])):
                    if grid[y][r] == "?":
                        grid[y][r] = unpaired[0]
                for c in range(len(grid)):
                    if grid[c][x] == "?":
                        grid[c][x] = unpaired[0]

    ls = []
    for y in range(2, 6):
        for x in range(2, 6):
            ls.append(grid[y][x])
    return "".join(ls)


def is_solved(grid):
    return all(c not in ["?", "."] for line in grid for c in line)


def fill_board(board):
    total = 0
    for i in range(0, len(board), 6):
        for j in range(0, len(board[i]), 6):
            grid = [line[j : j + 8] for line in board[i : i + 8]]
            if len(grid) != 8 or len(grid[0]) != 8:
                continue
            word = fill_grid(grid)
            if "." not in word:
                total += get_power(word)
            # ANNOYING: only update board if we solved this grid
            if is_solved(grid):
                for y in range(len(grid)):
                    for x in range(len(grid[y])):
                        board[i + y][j + x] = grid[y][x]
    return total


lines = read_input(3)
board = [[c for c in line] for line in lines]
fill_board(board)
print(fill_board(board))  # resolves after 2 iterations
