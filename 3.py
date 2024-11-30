from ec import read_input, DIRS, DIAG_DIRS


def count_levels(p, diag):
    p = read_input(p)
    levels = {}

    for y, line in enumerate(p):
        for x, c in enumerate(line):
            if c == "#":
                levels[(x, y)] = 1

    total = len(levels)
    while True:
        nxt = 0
        for (x, y), level in levels.items():
            good = True
            dirs = DIAG_DIRS if diag else DIRS
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if (nx, ny) not in levels or level - levels[(nx, ny)] >= 1:
                    good = False
                    break
            if good:
                nxt += 1
                levels[(x, y)] = level + 1

        total += nxt
        if nxt == 0:
            break

    return total


print(count_levels(1, False))
print(count_levels(2, False))
print(count_levels(3, True))
